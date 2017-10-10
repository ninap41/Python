SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM actor
	JOIN film_actor ON actor.actor_id = film_actor.actor_id
	JOIN film ON film_actor.film_id = film.film_id
	JOIN film_category ON film.film_id = film_category.film_id
	JOIN category ON film_category.category_id = category.category_id WHERE actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer' AND category.name = 'Action';