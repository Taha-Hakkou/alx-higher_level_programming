-- 101-not_a_comedy.sql
-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
INNER JOIN tv_show_genres ON show_id = tv_shows.id
LEFT JOIN tv_genres ON genre_id = tv_genres.id AND tv_genres.name = 'Comedy'
ORDER BY title;
