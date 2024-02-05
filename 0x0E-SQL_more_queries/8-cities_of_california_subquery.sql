-- 8-cities_of_california_subquery.sql
-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM cities
WHERE state_id = states.id AND states.name = 'California'
ORDER BY cities.id;
