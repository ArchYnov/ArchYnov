import { useState } from 'react'
import { FaChevronUp } from 'react-icons/fa'
import { MoviesCarousel } from '../components'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

const Movies = () => {
    const [showScroll, setShowScroll] = useState(false)

    const checkScrollTop = () => {
        if (!showScroll && window.pageYOffset > 400) {
            setShowScroll(true)
        } else if (showScroll && window.pageYOffset <= 400) {
            setShowScroll(false)
        }
    }

    const scrollTop = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    window.addEventListener('scroll', checkScrollTop)

    const {
        isLoading: newMoviesLoading,
        error: newMoviesError,
        data: new_movies,
    } = useQuery({
        queryKey: ['newMovies'],
        queryFn: async () =>
            await axios
                .get(
                    'http://localhost:5000/api/v1/movies?sort=-release_date&limit=12'
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
                    'http://localhost:5000/api/v1/movies?sort=vote_average&limit=12'
                )
                .then((res) => res.data.result),
    })

    // const new_movies = data ? data : []

    return (
        <main className="bg-background pt-[104px] pb-10 px-9 min-h-full">
            <div className="py-4">
                <h2
                    className="text-white
                    font-newake text-6xl pb-1 text-center"
                >
                    DERNIÈRES SORTIES
                </h2>
                {/* <MoviesCarousel movies={newMovies} /> */}
                {!newMoviesLoading && new_movies && (
                    <MoviesCarousel movies={new_movies} />
                )}
            </div>
            <div className="py-4">
                <h2
                    className="text-white
                    font-newake text-6xl pb-1 pt-4 text-center"
                >
                    LES PLUS APPRECIES
                </h2>
                {!mostPopularLoading && most_popular_movies && (
                    <MoviesCarousel movies={most_popular_movies} />
                )}
            </div>
            <button
                className={
                    'scrollTop bg-primary text-white rounded-full text-center fixed bottom-4 right-4 h-12 w-12 flex justify-center items-center cursor-pointer shadow-md transition-opacity duration-300' +
                    (showScroll ? ' opacity-100' : ' opacity-0')
                }
                onClick={scrollTop}
                style={{ display: showScroll ? 'flex' : 'none' }}
            >
                <FaChevronUp size={20} className="mt-[-2px]" />
            </button>
        </main>
    )
}

export default Movies
