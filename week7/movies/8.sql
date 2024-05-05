SELECT name FROM people

JOIN stars on stars.person_id = people.id JOIN movies ON movies.id = stars.movie_id

WHERE movies.title = "Toy Story";