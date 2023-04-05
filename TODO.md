<h1>Idées sur comment fetch des tweets pour les films qu'on récupère</h1>

L'idée est de mettre une propriété pour chaque document de film qui serait "fetchTwitterCount" qui pourrait être incrémentée quand on fetch des tweets pour un film.
Cela permettrait une fois tous les films fetch une fois d'itérer sur les suivants jusqu'a avoir fait toute la base, puis de refaire une passe sur ceux qui ont deja un fetch.