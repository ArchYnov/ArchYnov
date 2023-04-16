import { MdThumbsUpDown } from 'react-icons/md'
import { FaThumbsDown, FaThumbsUp } from 'react-icons/fa'
const NewsCard = ({
    title,
    description,
    date,
    source,
    sentiment_analysis,
}: {
    title: string
    description: string
    date: any
    source: string
    sentiment_analysis: string
}) => {
    function formatDate(date: any) {
        const d = new Date(date)
        const day = d.getDate().toString().padStart(2, '0')
        const month = (d.getMonth() + 1).toString().padStart(2, '0')
        const year = d.getFullYear().toString()
        return `${day}/${month}/${year}`
    }
    return (
        <div className="bg-transparent h-fit px-4 py-4 rounded-xl mb-20 text-neon border-4 border-neon badge-border-shadow w-full break-inside-avoid">
            <h2 className="text-3xl pb-2 font-newake badge-text-shadow flex items-end justify-center text-center">
                {title}
            </h2>
            <hr className="border-neon mt-3 mb-8 mx-12" />
            <p className="font-poppins text-xl font-medium mx-12 text-justify">
                {description}
            </p>
            <div className="flex justify-between items-center mx-12 mt-6">
                <p>{formatDate(date)}</p>
                {sentiment_analysis === 'POSITIVE' ? (
                    <div className=" border-4 border-neon p-4 rounded-full">
                        <FaThumbsUp className="text-neon text-xl" />
                    </div>
                ) : sentiment_analysis === 'NEGATIVE' ? (
                    <div className=" border-4 border-neon p-4 rounded-full">
                        <FaThumbsDown className="text-neon text-xl" />
                    </div>
                ) : (
                    <div className=" border-4 border-neon p-4 rounded-full">
                        <MdThumbsUpDown className="text-neon text-xl" />
                    </div>
                )}
                <p>Source : {source}</p>
            </div>
        </div>
    )
}

export default NewsCard
