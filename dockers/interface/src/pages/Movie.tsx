import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { useParams } from 'react-router-dom'
import { GenreBadge, StatBadge } from '../components'

const Movie = () => {
    const { id } = useParams()
    const { isLoading, error, data } = useQuery({
        queryKey: ['movie'],
        queryFn: async () =>
            await axios
                .get(`https://localhost:5000/api/v1/movies/${id}`)
                .then((res) => res.data.result),
    })

    const movie = data ? data : {}

    return (
        <main className="bg-background pt-[104px] h-screen min-h-screen">
            <section className="h-full grid grid-flow-col w-full px-[5%]">
                <div className="max-h-[90%] flex justify-center col-span-2">
                    <img
                        className="max-w-full max-h-full rounded-3xl"
                        src={`data:image/png;base64,${movie.encoded_pic}`}
                        alt={movie.title}
                    />
                </div>
                <div className="pl-20 mt-3 col-span-3 h-[90%] flex flex-col justify-between">
                    <div>
                        <h1 className="text-primary text-6xl font-newake neon-title-pink pb-6">
                            {movie.title}
                        </h1>
                        <div className="flex flex-wrap pb-6">
                            {movie.genre_ids?.map((genre: any) => (
                                <GenreBadge genre={genre.title} />
                            ))}
                        </div>
                        <p className="text-white text-justify font-poppins text-xl">
                            {movie.overview}
                        </p>
                    </div>
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
