-- 8-cities_of_california_subquery.sql
-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = states.id AND states.name = 'California';
