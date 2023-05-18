-- Query that lists all shows from hbtn_0c_tvshows_rate by their rating
SELECT tv-shows.title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_rating ON tv_shows.id = tv_show_rating.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
