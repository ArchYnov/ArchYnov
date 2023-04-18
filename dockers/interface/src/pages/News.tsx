import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { NewsCard, ScrollTopButton } from '../components'
import { SyncLoader } from 'react-spinners'

const News = () => {
    const {
        isLoading,
        error,
        data: news,
    } = useQuery({
        queryKey: ['news'],
        queryFn: async () =>
            await axios
                .get('https://localhost:5000/api/v1/news')
                .then((res) => res.data.result),
    })

    return (
        <main className="bg-background pt-[104px] pb-10 px-9 min-h-screen">
            <h2
                className="text-white
                    font-newake text-6xl pb-1 text-center mb-20"
            >
                NEWS
            </h2>

            {isLoading ? (
                <SyncLoader
                    color="#BB004B"
                    className="text-center my-10"
                    size="30"
                    speedMultiplier={0.5}
                />
            ) : (
                <div className="gap-20 max-w-[90%] m-auto columns-2">
                    {news.map((item: any, index: any) => (
                        <NewsCard
                            key={index}
                            title={item.source.title}
                            description={item.source.text}
                            date={item.source.date}
                            source={item.index}
                            sentiment_analysis={item.sentiment_analysis.label}
                        />
                    ))}
                </div>
            )}

            {/* <div className="gap-20 max-w-[90%] m-auto columns-2">
                {news ? (
                    news.map((item: any, index: any) => (
                        <NewsCard
                            key={index}
                            title={item.source.title}
                            description={item.source.text}
                            date={item.source.date}
                            source={item.index}
                            sentiment_analysis={item.sentiment_analysis.label}
                        />
                    ))
                ) : (
                    <p>Loading...</p>
                )}
            </div> */}
            <ScrollTopButton />
        </main>
    )
}

export default News
