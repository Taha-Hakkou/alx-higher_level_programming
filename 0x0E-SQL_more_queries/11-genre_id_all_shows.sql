-- 11-genre_id_all_shows.sql
-- lists all shows contained in the database hbtn_0d_tvshows
SELECT title, genre_id FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = show_id ORDER BY title, genre_id;
