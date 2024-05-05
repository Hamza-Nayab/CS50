--SELECT title FROM movies JOIN ratings on ratings.movie_id = movies.id WHERE ratings.rating = 10;

SELECT COUNT(movie_id) FROM ratings

WHERE rating = 10.0;