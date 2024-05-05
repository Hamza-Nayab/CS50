--SELECT DISTINCT(title) FROM movies JOIN stars ON stars.movie_id = movies.id JOIN people ON people.name ="Chadwick Boseman" JOIN ratings ON ratings.movie_id = movies.id ORDER BY rating DESC LIMIT 5;
SELECT DISTINCT(title) FROM movies

JOIN stars ON stars.movie_id = movies.id JOIN people ON people.id = stars.person_id

WHERE people.name = "Chadwick Boseman"

ORDER BY (SELECT rating FROM ratings WHERE ratings.movie_id = stars.movie_id)

DESC LIMIT 5;