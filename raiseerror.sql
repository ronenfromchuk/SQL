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
