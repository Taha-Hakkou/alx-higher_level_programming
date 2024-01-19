-- 13-count_shows_by_genre.sql
-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres RIGHT JOIN tv_show_genres ON genre_id = id GROUP BY genre ORDER BY number_of_shows DESC;
