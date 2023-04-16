const NewsCard = ({
    title,
    description,
    date,
    source,
}: {
    title: string
    description: string
    date: any
    source: string
}) => {
    return (
        <div className="bg-transparent h-fit px-4 py-4 rounded-xl mb-20 text-neon border-4 border-neon badge-border-shadow w-full break-inside-avoid">
            <h2 className="text-3xl pb-2 font-newake badge-text-shadow flex items-end justify-center text-center">
                {title}
            </h2>
            <hr className="border-neon mt-3 mb-8 mx-12" />
            <p className="font-poppins text-xl font-medium mx-12 text-justify">
                {description}
            </p>
            <div className="flex justify-between mx-12 mt-6">
                <p>{date}</p>
                <p>Source : {source}</p>
            </div>
        </div>
    )
}

export default NewsCard
