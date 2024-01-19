-- 15-comedy_only.sql
-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT title FROM tv_shows
INNER JOIN tv_show_genres ON show_id = tv_shows.id
INNER JOIN tv_genres ON genre_id = tv_genres.id AND name = 'Comedy'
ORDER BY title;
