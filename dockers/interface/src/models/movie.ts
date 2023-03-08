export default class Movie {
    id: number;
    title: string;
    year: number;
    genres: string[];
    poster: string;
    rating: number;
    runtime: number;
    synopsis: string;
    directors: string[];
    actors: string[];
    constructor(id: number, title: string, year: number, genres: string[], poster: string, rating: number, runtime: number, synopsis: string, directors: string[], actors: string[]) {
        this.id = id;
        this.title = title;
        this.year = year;
        this.genres = genres;
        this.poster = poster;
        this.rating = rating;
        this.runtime = runtime;
        this.synopsis = synopsis;
        this.directors = directors;
        this.actors = actors;
    }
}