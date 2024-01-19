-- 16-shows_by_genre.sql
-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name FROM tv_show_genres
INNER JOIN tv_shows ON show_id = tv_shows.id
INNER JOIN tv_genres ON genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
