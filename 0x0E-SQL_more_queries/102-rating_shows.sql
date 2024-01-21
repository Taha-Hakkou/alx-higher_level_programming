-- 102-rating_shows.sql
-- lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows
INNER JOIN tv_show_ratings ON tv_shows.id = show_id
GROUP BY title
ORDER BY rating DESC;
