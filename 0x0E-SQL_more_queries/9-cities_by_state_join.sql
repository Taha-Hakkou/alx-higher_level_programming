-- 9-cities_by_state_join.sql
-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON state_id = states.id ORDER BY cities.id
