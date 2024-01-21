-- 12-no_genre.sql
-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT title, genre_id FROM tv_shows
RIGHT JOIN tv_show_genres ON genre_id = tv_shows.id WHERE tv_shows.id IS NULL
ORDER BY title, genre_id;
