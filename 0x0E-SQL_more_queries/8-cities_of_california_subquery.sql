-- 8-cities_of_california_subquery.sql
-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT * FROM cities
WHERE id IN (
SELECT id FROM states
WHERE name = 'California')
ORDER BY cities.id;
