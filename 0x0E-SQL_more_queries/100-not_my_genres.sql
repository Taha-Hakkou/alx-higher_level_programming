-- 100-not_my_genres.sql
-- uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = genre_id
LEFT JOIN tv_shows ON tv_shows.id = show_id AND tv_shows.title = 'Dexter'
ORDER BY name;