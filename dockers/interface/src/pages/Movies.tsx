import { useState } from 'react'
import { FaChevronUp } from 'react-icons/fa'
import { MovieCard, MoviesCarousel } from '../components'
import { useQuery } from '@tanstack/react-query'

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

    const movie = {
        adult: false,
        backdrop_path: '/2rVkDZFLN6DI5PAoraoe9m4IRMN.jpg',
        genre_ids: [12, 14, 35],
        id: 493529,
        original_language: 'en',
        original_title: 'Dungeons & Dragons: Honor Among Thieves',
        overview:
            'A charming thief and a band of unlikely adventurers undertake an epic heist to retrieve a lost relic, but things go dangerously awry when they run afoul of the wrong people.',
        popularity: 560.108,
        poster_path: '/6LuXaihVIoJ5FeSiFb7CZMtU7du.jpg',
        release_date: '2023-03-23',
        title: 'Dungeons & Dragons: Honor Among Thieves',
        video: false,
        vote_average: 7.6,
        vote_count: 222,
    }

    const { isLoading, error, data } = useQuery({
        queryKey: ['repoData'],
        queryFn: () => fetch('http://localhost:3000').then((res) => res.json()),
    })

    return (
        <main className="h-screen bg-background pt-[104px]">
            <h2
                className="text-white
                    font-newake text-4xl pb-1"
            >
                DERNIÈRES SORTIES
            </h2>
            <div className="flex">
                <MovieCard movie={movie} />
                <MovieCard movie={movie} />
                <MovieCard movie={movie} />
            </div>

            <h2
                className="text-white
                    font-newake text-4xl pb-1"
            >
                LES PLUS APPRECIES
            </h2>
            <MoviesCarousel />
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
