const GenreBadge = ({ genre }: { genre: any }) => {
    return (
        <div className="bg-transparent w-fit h-fit px-4 py-4 rounded-xl flex justify-center items-center my-4 mr-8 text-neon border-4 border-neon btn-shadows">
            <h2 className="text-xl font font-poppins font-medium">{genre}</h2>
        </div>
    )
}

export default GenreBadge
