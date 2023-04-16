import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { NewsCard, ScrollTopButton } from '../components'

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

    // const movies = data ? data : []

    return (
        <main className="bg-background pt-[104px] pb-10 px-9 min-h-screen">
            <h2
                className="text-white
                    font-newake text-6xl pb-1 text-center mb-20"
            >
                NEWS
            </h2>

            <div className="gap-20 max-w-[90%] m-auto columns-2">
                {news ? (
                    news.map((item: any, index: any) => (
                        <NewsCard
                            key={index}
                            title={item.source.title}
                            description={item.source.text}
                            date={item.source.date}
                            source={item.index}
                        />
                    ))
                ) : (
                    <p>Loading...</p>
                )}
            </div>
            <ScrollTopButton />
        </main>
    )
}

export default News
