import { useState } from 'react'
import { FaChevronUp } from 'react-icons/fa'
import { MoviesCarousel } from '../components'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

const News = () => {
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

    const { isLoading, error, data } = useQuery({
        queryKey: ['newMovies'],
        queryFn: async () =>
            await axios
                .get('http://localhost:5000/api/v1/movies/new?limit=12')
                .then((res) => res.data.result),
    })

    const movies = data ? data : []

    return (
        <main className="bg-background pt-[104px] pb-10 px-9 min-h-screen">
            <h2
                className="text-white
                    font-newake text-4xl pb-1"
            >
                News{' '}
            </h2>
        </main>
    )
}

export default News
