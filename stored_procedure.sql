drop function hello_world();
CREATE or replace function hello_world() returns varchar
language plpgsql AS
    $$
        BEGIN
            return CONCAT('hello', 'world', ' ', current_timestamp);
        end;
    $$;

select hello_world result from hello_world();

CREATE or replace function sp_sum(m double precision, n double precision)
returns double precision
language plpgsql AS
    $$
        DECLARE
            x integer := 0;
        BEGIN
            return m + n + x;
        end;
    $$;

select sp_sum result from sp_sum(2.2, 3.5);

drop function sp_product;
CREATE or replace function sp_product(x double precision, y double precision,
    OUT prod double precision,
    OUT div_res double precision)
language plpgsql AS
    $$
        DECLARE
            z double precision := 1.0;
        BEGIN
            prod = x * y * z;
            div_res = x / y;
        end;
    $$;

select * from sp_product(2.2, 3.5);

-- create table movies
-- title, release_date, price, country_id
-- text, timestamp, double precision
-- create table countries

-- create table countries
-- (
--     id   bigserial not null
--         constraint countries_pk
--             primary key,
--     name text      not null
-- )
-- create table movies
-- (
--     id           bigserial                  not null
--         constraint movies_pk
--             primary key,
--     title        text,
--     release_date timestamp                  not null,
--     price        double precision default 0 not null,
--     country_id   bigint
--         constraint movies_countries_id_fk
--             references countries
-- );
-- insert into countries(name) values ('Israel');
-- insert into countries(name) values ('USA');
-- insert into countries(name) values ('JAPAN');
-- insert into movies (title, release_date, price, country_id)
-- values ('batman returns', '2020-12-16 20:21:00', 45.5, 3);
-- insert into movies (title, release_date, price, country_id)
-- values ('wonder woman', '2018-07-11 08:12:11', 125.5, 3);
-- insert into movies (title, release_date, price, country_id)
-- values ('matrix resurrection', '2021-01-03 09:10:11', 38.7, 4);

drop function sp_movies_stat;
CREATE or replace function sp_movies_stat(out min_price double precision,
    out max_price double precision,
    out avg_price double precision)
language plpgsql AS
    $$
        BEGIN
            select min(price), max (price), avg(price)::numeric(5, 2)
            into min_price, max_price, avg_price
            from movies;
        end;
    $$;

select * from sp_movies_stat();

-- targil:
-- 1. create sp returns name of the most expansive movie

drop function sp_movies_expensive_name;
CREATE or replace function sp_movies_expensive_name(out most_expensive_movie_name text)
language plpgsql AS
    $$
        DECLARE
            max_price double precision := 0;
        BEGIN
            select max (price)
            into max_price
            from movies;

            select title from movies
            where price = max_price
            into most_expensive_movie_name;
        end;
    $$;

select * from sp_movies_expensive_name();
-- 2. create sp_num_of_movies return the number of movies + number of countries

drop function sp_count_movies_and_countries;
CREATE or replace function sp_count_movies_and_countries(out count_movies_and_countries bigint)
language plpgsql AS
    $$
        DECLARE
            count_movies bigint := 0;
            count_countries bigint := 0;
        BEGIN
            select count (*)
            into count_movies
            from movies;

            select count (*)
            into count_countries
            from countries;

            count_movies_and_countries = count_movies +  count_countries;
        end;
    $$;

select * from sp_count_movies_and_countries();

drop function sp_insert_movie;
-- each parameter starts with _ (i.e. _title) to avoid ambiguity with the table columns
CREATE or replace function sp_insert_movie(_title text, _release_date timestamp,
    _price double precision, _country_id bigint)
    returns bigint
language plpgsql AS
    $$
        DECLARE
            new_id bigint := 0;
        BEGIN
            INSERT INTO movies(title, release_date, price, country_id)
            values (_title, _release_date, _price, _country_id)
            returning id into new_id;

            return new_id; -- returning the id of the newly created record
        end;
    $$;

select * from sp_insert_movie('Queen gambit', cast('2020-08-12' as timestamp)
    , 87.1, 3);
select * from sp_insert_movie('Eternals', cast('2020-05-21' as timestamp)
    , 101.3, 1);

-- sp_update_movie (movie_details, _id => update ) return 0
-- execute func
-- *etgar: write it without return value
-- sp_get_movies_in_range(_min, _max) => count number of movies

drop function sp_update_movie;
-- procedure does not return a value
CREATE or replace procedure sp_update_movie(_title text, _release_date timestamp,
    _price double precision, _country_id bigint, _update_id bigint)
language plpgsql AS
    $$
        BEGIN
            UPDATE movies
            set title = _title, release_date = _release_date,
                price = _price, country_id = _country_id
            where id = _update_id;
        end;
    $$;

call sp_update_movie('Queen gambit 2', cast('2020-08-12' as timestamp)
    , 87.1, 3, 5);

drop function sp_get_movies_in_range;
-- procedure does not return a value
CREATE or replace function  sp_get_movies_in_range(_min double precision, _max double precision)
returns TABLE(id bigint, title text, release_date timestamp,
    price double precision, country_id bigint, country_name text)
language plpgsql AS
    $$
        BEGIN
            return QUERY
            select m.id, m.title, m.release_date, m.price, m.country_id, c.name from movies m
            join countries c on m.country_id = c.id
            where m.price between _min and _max;
        end;
    $$;

select * from sp_get_movies_in_range(100, 150) order by release_date;
