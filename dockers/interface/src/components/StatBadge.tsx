const StatBadge = ({
    note,
    source,
    review_nbr,
    on,
}: {
    note: string
    source: string
    review_nbr: number
    on: number
}) => {
    return (
        <div className="bg-transparent h-fit px-4 py-4 rounded-xl text-center justify-center items-center my-4 mr-8  text-neon border-4 border-neon badge-border-shadow w-full">
            <h2 className="text-8xl pb-2 font-newake badge-text-shadow flex items-end justify-center">
                {note} <span className="text-xl">/{on}</span>
            </h2>
            <h3 className="text-md font-poppins font-medium">{source}</h3>
            <h4 className="text-xs font-poppins">{review_nbr} reviews</h4>
        </div>
    )
}

export default StatBadge
