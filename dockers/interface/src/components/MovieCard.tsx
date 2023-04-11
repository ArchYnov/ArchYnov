import React from 'react'

const MovieCard = ({ movie }: { movie: any }) => {
    return (
        <div className="max-w-md mx-auto bg-[#1b1929] rounded-xl shadow-md overflow-hidden md:max-w-2xl  w-full">
            <div className="md:flex">
                <div className="md:flex-shrink-0">
                    <img
                        className="h-48 w-full object-cover md:h-full md:w-48"
                        // src={movie.poster_path}
                        src="https://image.tmdb.org/t/p/w500/6LuXaihVIoJ5FeSiFb7CZMtU7du.jpg"
                        alt={movie.title}
                    />
                </div>
                <div className="p-8">
                    <div className="uppercase tracking-wide text-sm text-primary font-semibold">
                        {movie.genre_ids}
                    </div>
                    <h2 className="block mt-1 text-lg leading-tight font-medium text-primary hover:underline neon-title-pink">
                        {movie.title}
                    </h2>
                    <p className="mt-2 text-white">{movie.overview}</p>
                    <div className="mt-4">
                        <a
                            href="/#"
                            className="text-primary hover:text-primary font-semibold text-sm"
                        >
                            Consulter les statistiques
                        </a>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default MovieCard
