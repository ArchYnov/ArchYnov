import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { useState } from 'react'
import { MovieCard, ScrollTopButton } from '../components'
import { Link } from 'react-router-dom'

const AllMovies = () => {
    const [selectedGenre, setSelectedGenre] = useState('')
    const [sortOrder, setSortOrder] = useState('desc')
    const {
        isLoading: allMoviesLoading,
        error: allMoviesError,
        data: all_movies,
    } = useQuery({
        queryKey: ['allMovies'],
        queryFn: async () =>
            await axios
                .get('https://localhost:5000/api/v1/movies?sort=-release_date')
                .then((res) => res.data.result),
    })

    const sortedMovies = all_movies?.sort((a: any, b: any) => {
        if (sortOrder === 'asc') {
            return a.release_date > b.release_date ? 1 : -1
        } else {
            return a.release_date < b.release_date ? 1 : -1
        }
    })

    const filteredMovies = selectedGenre
        ? sortedMovies?.filter((movie: any) =>
              movie.genre_ids.some(
                  (genre: any) => genre.title === selectedGenre
              )
          )
        : sortedMovies

    return (
        <main className="bg-background pt-[90px] pb-10 px-9 min-h-screen">
            <div className="flex justify-between items-center">
                <h1 className="text-primary font-bold text-3xl">All Movies</h1>
                <div>
                    <select
                        className="px-4 py-2 rounded-lg bg-white border border-gray-300 shadow-sm focus:border-primary focus:ring focus:ring-primary focus:ring-opacity-50"
                        onChange={(e) => setSelectedGenre(e.target.value)}
                        value={selectedGenre}
                    >
                        <option value="">All Genres</option>
                        <option value="Animation">Animation</option>
                        <option value="Adventure">Adventure</option>
                        <option value="Family">Family</option>
                        <option value="Fantasy">Fantasy</option>
                        <option value="Comedy">Comedy</option>
                    </select>
                    <select
                        className="px-4 py-2 rounded-lg bg-white border border-gray-300 shadow-sm focus:border-primary focus:ring focus:ring-primary focus:ring-opacity-50 ml-4"
                        onChange={(e) => setSortOrder(e.target.value)}
                        value={sortOrder}
                    >
                        <option value="desc">
                            Sort by Date (Newest First)
                        </option>
                        <option value="asc">Sort by Date (Oldest First)</option>
                    </select>
                </div>
            </div>
            <div className="grid grid-cols-4">
                {filteredMovies?.map((movie: any) => (
                    <Link to={`/movie/${movie.id}`} className="w-full">
                        <MovieCard key={movie.id} movie={movie} />
                    </Link>
                ))}
            </div>
            <ScrollTopButton />
        </main>
    )
}

export default AllMovies
