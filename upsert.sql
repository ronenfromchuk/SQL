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
