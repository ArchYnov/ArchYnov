import React from 'react'
import classnames from 'classnames'

const MovieCard = ({ movie }: { movie: any }) => {
    const movieClasses = classnames({
        'bg-red-500': movie.vote_average <= 2.5,
        'bg-yellow-500': movie.vote_average > 2.5 && movie.vote_average <= 7.5,
        'bg-green-500': movie.vote_average >= 7.5,
    })
    return (
        <div className="w-65 m-8 hover:scale-[1.12] transition ease-in-out relative hover:shadow-inner cursor-pointer card-shadow movie-card">
            <div>
                <img
                    src={`data:image/png;base64,${movie.encoded_pic}`}
                    alt={movie.title}
                />
            </div>
            <div className="absolute bottom-0 left-0 opacity-0 movie-card-content w-full bg-black bg-opacity-80 h-full"></div>
            <div className="absolute bottom-0 left-0 opacity-0 movie-card-content w-full p-4 h-fit">
                <h2 className="text-white text-lg font-poppins font-medium">
                    {movie.title}
                </h2>
                <div className="text-white font-thin movie-card-genres flex flex-wrap overflow-hidden">
                    {movie.genre_ids.map((genre: any) => (
                        <span className="flex items-center">
                            {genre.title}{' '}
                        </span>
                    ))}
                </div>
            </div>
            <div className="absolute top-0 left-100 opacity-0 movie-card-content w-full p-4 flex justify-end">
                <div
                    className={`text-sm ${movieClasses} flex justify-center items-center px-3 pt-1 rounded-xl`}
                >
                    <span className="text-white font-newake text-lg h-fit">
                        {movie.vote_average}
                    </span>{' '}
                </div>
            </div>
        </div>
    )
}

export default MovieCard
