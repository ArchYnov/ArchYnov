import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { useParams } from 'react-router-dom'
import { GenreBadge, StatBadge } from '../components'
import { FaThumbsUp, FaRegThumbsDown } from 'react-icons/fa'

const Movie = () => {
    // const movie = {
    //     _id: '643005e67667e97657e2a1f5',
    //     id: 502356,
    //     adult: false,
    //     backdrop_path: '/9n2tJBplPbgR2ca05hS5CKXwP2c.jpg',
    //     genre_ids: [
    //         {
    //             id: 16,
    //             title: 'Animation',
    //         },
    //         {
    //             id: 10751,
    //             title: 'Family',
    //         },
    //         {
    //             id: 14,
    //             title: 'Fantasy',
    //         },
    //         {
    //             id: 12,
    //             title: 'Adventure',
    //         },
    //         {
    //             id: 35,
    //             title: 'Comedy',
    //         },
    //     ],
    //     original_language: 'en',
    //     original_title: 'The Super Mario Bros. Movie',
    //     overview:
    //         'While working underground to fix a water main, Brooklyn plumbers—and brothers—Mario and Luigi are transported down a mysterious pipe and wander into a magical new world. But when the brothers are separated, Mario embarks on an epic quest to find Luigi.',
    //     popularity: 3665.784,
    //     poster_path: '/qNBAXBIQlnOThrVvA6mA2B5ggV6.jpg',
    //     release_date: '2023-04-05',
    //     title: 'The Super Mario Bros. Movie',
    //     video: false,
    //     vote_average: 5,
    //     vote_count: 157,
    // }
    const { id } = useParams()
    const { isLoading, error, data } = useQuery({
        queryKey: ['movie'],
        queryFn: async () =>
            await axios
                .get(`http://localhost:5000/api/v1/movies/${id}`)
                .then((res) => res.data.result),
    })

    const movie = data ? data : {}

    console.log(typeof movie.vote_average)
    let icon
    if (movie.vote_average > 5) {
        icon = <FaThumbsUp />
    } else {
        icon = <FaRegThumbsDown />
    }

    return (
        <main className="bg-background pt-[104px] h-screen min-h-screen">
            <section className="h-full grid grid-flow-col w-full px-[5%]">
                <div className="max-h-[90%] flex justify-center col-span-2">
                    {/* <div className="absolute inset-0 bg-gradient-to-r from-gray-900 to-transparent rounded-3xl"></div> */}
                    <img
                        // src={movie.poster_path}
                        className="max-w-full max-h-full rounded-3xl"
                        src="https://image.tmdb.org/t/p/w500/6LuXaihVIoJ5FeSiFb7CZMtU7du.jpg"
                        alt={movie.title}
                    />
                </div>
                <div className="pl-20 mt-3 col-span-3 h-[90%] flex flex-col justify-between">
                    <h1 className="text-primary text-6xl font-newake neon-title-pink">
                        {movie.title}
                    </h1>
                    <div className="flex flex-wrap">
                        {movie.genre_ids?.map((genre: any) => (
                            <GenreBadge genre={genre.title} />
                        ))}
                    </div>
                    <p className="text-white text-justify font-poppins text-xl">
                        {movie.overview}
                    </p>
                    <div className="grid grid-cols-3 gap-10">
                        <StatBadge
                            note={movie.vote_average}
                            source="Note TMDB"
                            review_nbr={movie.vote_count}
                            on={10}
                        />
                        <StatBadge
                            note={(parseInt(movie.popularity) / 1000).toFixed(
                                1
                            )}
                            source="Popularity TMDB"
                            review_nbr={movie.vote_count}
                            on={10}
                        />
                        <StatBadge
                            note={movie.vote_average}
                            source="Sentiment Analysis Twitter"
                            review_nbr={movie.vote_count}
                            on={10}
                        />
                    </div>
                </div>
            </section>
        </main>
    )
}

export default Movie
