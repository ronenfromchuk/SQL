-- return movies not the cheapest and not the most expansive
drop function sp_get_movies_mid;
CREATE or replace function sp_get_movies_mid()
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

select * from sp_get_movies_mid() order by release_date;


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

CREATE or replace function sp_get_max(_x integer, _y integer, _z integer)
returns integer
language plpgsql AS
	$$
		BEGIN if _x > _y and _x > _z then
			return _x;
			end if;
			if _y > _x and _y > _z then
			return _y;
			else
				return _z;
			end if;
		end;
		
	$$;
	
select * from sp_get_max(6, 7, 5);
