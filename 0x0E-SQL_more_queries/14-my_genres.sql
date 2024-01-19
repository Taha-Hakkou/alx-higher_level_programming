-- 14-my_genres.sql
-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name FROM tv_genres
INNER JOIN tv_show_genres ON genre_id = tv_genres.id
INNER JOIN tv_shows ON tv_shows.id = show_id AND title = 'Dexter'
ORDER BY name;
