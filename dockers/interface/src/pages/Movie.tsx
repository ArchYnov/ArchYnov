import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { useParams } from 'react-router-dom'
import { GenreBadge, StatBadge } from '../components'
import { SyncLoader } from 'react-spinners'

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

    const { data: tweets } = useQuery({
        queryKey: ['tweets'],
        queryFn: async () =>
            await axios
                .get(
                    `https://localhost:5000/api/v1/tweets?limit=0&fields=sentiment_analysis,id,tmdb_id&filters=tmdb_id=${movie._id};sentiment_analysis!=n/a`
                )
                .then((res) => res.data),
    })

    let positiveCount = 0
    let negativeCount = 0
    let sentiment_analysis = 0
    if (tweets && tweets.count) {
        // Ajout de la vérification
        const tweets_count = tweets.count
        const tweets_data = tweets.result

        for (let i = 0; i < tweets_count; i++) {
            if (tweets_data[i].sentiment_analysis.label === 'POSITIVE') {
                positiveCount++
            } else if (tweets_data[i].sentiment_analysis.label === 'NEGATIVE') {
                negativeCount++
            }
        }

        console.log('Nombre de valeurs positives : ' + positiveCount)
        console.log('Nombre de valeurs négatives : ' + negativeCount)
        sentiment_analysis = (positiveCount * 10) / tweets.count
    } else {
        console.log('Aucun tweet trouvé.')
    }

    function formatDate(date: any) {
        const d = new Date(date)
        const day = d.getDate().toString().padStart(2, '0')
        const month = (d.getMonth() + 1).toString().padStart(2, '0')
        const year = d.getFullYear().toString()
        return `${day}/${month}/${year}`
    }
    return (
        <main className="bg-background pt-[104px] h-screen min-h-screen">
            {isLoading ? (
                <SyncLoader
                    color="#BB004B"
                    className="text-center my-10"
                    size="30"
                    speedMultiplier={0.5}
                />
            ) : (
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
                            <p className="text-white text-justify font-poppins text-xl pb-6">
                                {movie.overview}
                            </p>
                            <p className="font-poppins text-white text-justify font-thin">
                                Release date : {formatDate(movie.release_date)}
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
                                note={(
                                    parseInt(movie.popularity) / 1000
                                ).toFixed(1)}
                                source="Popularity TMDB"
                                review_nbr={movie.vote_count}
                                on={10}
                            />
                            <StatBadge
                                note={sentiment_analysis.toFixed(1)}
                                source="Sentiment Analysis Twitter"
                                review_nbr={tweets ? tweets.count : 0}
                                on={10}
                            />
                        </div>
                    </div>
                </section>
            )}
        </main>
    )
}

export default Movie
