-- 10-genre_id_by_show.sql
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre_id FROM tv_shows
RIGHT JOIN tv_show_genresON tv_shows.id = show_id
ORDER BY title, genre_id;
