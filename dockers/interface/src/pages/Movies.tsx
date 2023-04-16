import { MoviesCarousel, ScrollTopButton } from '../components'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { Link } from 'react-router-dom'

const Movies = () => {
    const {
        isLoading: newMoviesLoading,
        error: newMoviesError,
        data: new_movies,
    } = useQuery({
        queryKey: ['newMovies'],
        queryFn: async () =>
            await axios
                .get(
                    'https://localhost:5000/api/v1/movies?sort=-release_date&limit=12'
                )
                .then((res) => res.data.result),
    })

    const {
        isLoading: mostPopularLoading,
        error: mostPopularError,
        data: most_popular_movies,
    } = useQuery({
        queryKey: ['popularMovies'],
        queryFn: async () =>
            await axios
                .get(
                    'https://localhost:5000/api/v1/movies?sort=-vote_average&limit=12'
                )
                .then((res) => res.data.result),
    })

    return (
        <main className="bg-background pt-[90px] pb-10 px-9 min-h-screen">
            <div className="py-4">
                <h2
                    className="text-white
                    font-newake text-6xl pb-1 text-center"
                >
                    LATEST RELEASES
                </h2>
                {!newMoviesLoading && new_movies && (
                    <MoviesCarousel movies={new_movies} />
                )}
            </div>
            <div className="py-4">
                <h2
                    className="text-white
                    font-newake text-6xl pb-1 pt-4 text-center"
                >
                    THE MOST APPRECIATED
                </h2>
                {!mostPopularLoading && most_popular_movies && (
                    <MoviesCarousel movies={most_popular_movies} />
                )}
            </div>
            <div className="py-4">
                <div className="pt-9 flex justify-center">
                    <Link to="/movies/all">
                        <button className="text-4xl cursor-pointer decoration-none text-neon border-4 border-neon py-4 px-3 font-josefin rounded-lg btn-shadows neon-btn">
                            All movies
                        </button>
                    </Link>
                </div>
            </div>
            <ScrollTopButton />
        </main>
    )
}

export default Movies
