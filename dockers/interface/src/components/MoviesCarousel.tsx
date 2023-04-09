import React, { useState, useEffect } from 'react'
// import axios from 'axios'
import MovieCard from './MovieCard'

const Carousel = () => {
    // const [movies, setMovies] = useState([])
    const [position, setPosition] = useState(0)
    const movies = [
        {
            id: 1,
            title: 'The Shawshank Redemption',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/51E7N1vHmxL._AC_SY450_.jpg',
        },
        {
            id: 2,
            title: 'The Godfather',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/91q+wjRliML._AC_SY741_.jpg',
        },
        {
            id: 3,
            title: 'The Dark Knight',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/81vvgZqCskL._AC_SY679_.jpg',
        },
        {
            id: 4,
            title: '12 Angry Men',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/81v%2Bb69uOQL._AC_SY679_.jpg',
        },
        {
            id: 5,
            title: "Schindler's List",
            poster: 'https://images-na.ssl-images-amazon.com/images/I/81nwnHTC3RL._AC_SY741_.jpg',
        },
        {
            id: 6,
            title: 'The Lord of the Rings: The Return of the King',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/81s%2B7+4GXjL._AC_SY741_.jpg',
        },
        {
            id: 7,
            title: 'Pulp Fiction',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/91jZc0GZBLL._AC_SY741_.jpg',
        },
        {
            id: 8,
            title: 'The Lord of the Rings: The Fellowship of the Ring',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/81by8zHdMhL._AC_SY741_.jpg',
        },
        {
            id: 9,
            title: 'Forrest Gump',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/91lMV%2BKtPRL._AC_SY741_.jpg',
        },
        {
            id: 10,
            title: 'Inception',
            poster: 'https://images-na.ssl-images-amazon.com/images/I/91%2BUte5r5EL._AC_SY741_.jpg',
        },
    ]

    const visibleMovies = movies.slice(position, position + 3)

    const handleNext = () => {
        setPosition(position + 1)
    }

    const handlePrev = () => {
        setPosition(position - 1)
    }

    // Défilement automatique toutes les 3 secondes
    useEffect(() => {
        const intervalId = setInterval(() => {
            handleNext()
        }, 3000)

        return () => clearInterval(intervalId)
    }, [position])

    return (
        <div className="flex items-center justify-center w-full">
            <button
                className="px-4 py-2 mr-4 font-bold text-white bg-gray-800 rounded-lg"
                onClick={handlePrev}
            >
                Prev
            </button>
            <div className="overflow-x-hidden grid grid-cols-3 w-full gap-10">
                {visibleMovies.map((movie) => (
                    <MovieCard key={movie.id} movie={movie} />
                ))}
                {movies.slice(0, 3 - visibleMovies.length).map((movie) => (
                    <MovieCard key={movie.id} movie={movie} />
                ))}
            </div>
            <button
                className="px-4 py-2 ml-4 font-bold text-white bg-gray-800 rounded-lg"
                onClick={handleNext}
            >
                Next
            </button>
        </div>
    )
}

export default Carousel
