-- return movies not the cheapest and not the most expansive
drop function sp_get_movies_mid;
CREATE or replace function sp_get_movies_mid()
returns TABLE(id bigint, title text, release_date timestamp,
    price double precision, country_id bigint, country_name text)
language plpgsql AS
    $$
        BEGIN
            return QUERY
            WITH cheapest_movie AS
                (
                    select * from movies
                    where movies.price = (select min(movies.price)from movies)
                ),
            expensive_movie AS
                (
                    select * from movies
                    where movies.price = (select max(movies.price)from movies)
                )
            select m.id, m.title, m.release_date, m.price, m.country_id, c.name from movies m
            join countries c on m.country_id = c.id
            where m.id <> (select cheapest_movie.id from cheapest_movie)
              and m.id <> (select expensive_movie.id from expensive_movie);
        end;
    $$;

select * from sp_get_movies_mid() order by release_date;

drop function sp_get_max;
CREATE or replace function sp_get_max(_x integer, _y integer)
returns integer
language plpgsql AS
    $$
        BEGIN
            if _x > _y then
                return _x;
            -- ELSEIF
            else
                return _y;
            end if;
        end;
    $$;

select * from sp_get_max(3, 2);

drop function sp_get_max3;
CREATE or replace function sp_get_max3(_x integer, _y integer, _z integer)
returns integer
language plpgsql AS
    $$
        BEGIN
            if _x >_y and _x > _z then
                return _x;
            elseif _y > _z then
                return _y;
            else
                return _z;
            end if;
        end;
    $$;

select * from sp_get_max3(3, 2, -1);

drop function sp_get_movies_country_id;
CREATE or replace function sp_get_movies_country_id(_id_type text)
returns TABLE(id bigint, title text)
language plpgsql AS
    $$
        BEGIN
            return QUERY
            select case when _id_type = 'M' then m.id
                                  else m.country_id end, m.title
            from movies m;
        end;
    $$;

select * from sp_get_movies_country_id('M');

drop function sp_get_movies_price_or_pow2;
CREATE or replace function sp_get_movies_price_or_pow2(_pow boolean)
returns TABLE(id bigint, title text, price double precision)
language plpgsql AS
    $$
        BEGIN
            return QUERY
            select m.id, m.title, case when _pow then pow(m.price, 2)
                                  else m.price end
            from movies m;
        end;
    $$;

select * from sp_get_movies_price_or_pow2(true);
select * from sp_get_movies_price_or_pow2(false);

drop function sp_get_random;
CREATE or replace function sp_get_random(_max integer)
returns integer
language plpgsql AS
    $$
        BEGIN
            return random() * (_max - 1) + 1;
        end;
    $$;

select * from sp_get_random(3);
select * from random(); -- 0 .. 0.999999

drop function sp_get_sum_loop;
CREATE or replace function sp_get_sum_loop()
returns double precision
language plpgsql AS
    $$
        declare
            sum double precision := 0.0;
        BEGIN
            for i in 1..(select max(movies.id) from movies)
                loop
                    if (select count(*) from movies m where m.id = i) > 0 then
                        sum := sum + (select m.price from movies m where m.id = i);
                    end if;
                end loop;
            return sum;
        end;
    $$;

select * from sp_get_sum_loop();

create table grades
(
    id bigserial constraint grades_pk primary key,
    class_id bigint not null,
    student_id bigint not null,
    grade double precision default 0 not null
);

drop function sp_populate_grades;
CREATE or replace function sp_populate_grades(_classes int, _students int)
returns integer
language plpgsql AS
    $$
        DECLARE
            counter int := 0;
            _grade double precision := 0;
        BEGIN
            for i in 1.._classes
                loop
                    for j in 1.._students
                        loop
                            counter := counter + 1;
                            _grade = random() * 100;
                            INSERT INTO grades(class_id, student_id, grade)
                                values (i, j, _grade);
                        end loop;
                end loop;
            return counter;
        end;
    $$;

select * from sp_populate_grades(5, 30);

select * from (
select *,
       row_number() over (partition by class_id order by class_id, grade desc) row_num
from grades) c
where c.row_num between 1 and 2;

select * , (grade - class_avg) diff from (
select student_id, class_id, grade,
       count(*) over (partition by class_id) students_in_class,
       avg(grade) over (partition by class_id) class_avg
from grades ) c;

select class_id, avg(grade)
from grades
group by class_id;

-- upsert
drop function sp_upsert_movie;
CREATE or replace function sp_upsert_movie(_title text, _release_date timestamp,
    _price double precision, _country_id bigint)
    returns bigint
language plpgsql AS
    $$
        DECLARE
            record_id bigint := 0;
        BEGIN
            SELECT movies.id
                into record_id from movies
                    where movies.title = _title;
            if not found then
                INSERT INTO movies(title, release_date, price, country_id)
                values (_title, _release_date, _price, _country_id)
                returning id into record_id;
            else
                update movies
                    set release_date = _release_date, price = _price, country_id = _country_id
                    where movies.id = record_id;
            end if;
            return record_id; -- returning the id of the newly created record
        end;
    $$;

select * from movies order by id;
select * from sp_upsert_movie('batman returns', '2020-12-17 20:21:00.000000', 48, 3);
select * from sp_upsert_movie('spiderman home', '2022-01-02 07:10:03.000000', 98.03, 1);

drop function sp_div;
create or replace function sp_div(x integer, y integer) returns double precision
language plpgsql as
    $$
        begin
            if y = 0 then
                raise division_by_zero;
            end if;
            return x::double precision / y::double precision ;
        end;
    $$;
select * from sp_div(2, 4);
