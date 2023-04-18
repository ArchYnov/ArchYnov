import HeroImage from '../assets/images/hero-image.jpg'
import diamond from '../assets/backgrounds/diamond.svg'
import informations_section from '../assets/backgrounds/informations.png'

const Cinema = () => {
    const handleClickScroll = () => {
        const element = document.getElementById('global-stats')
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' })
        }
    }
    return (
        <section
            className="h-screen bg-background grid grid-cols-2 pt-[104px] mr-1/2"
            id="informations"
        >
            <div className="flex flex-col justify-center pl-[10%] pr-[10%]">
                <h1
                    className="text-white
                    font-newake text-8xl pb-1"
                >
                    INFORMATION
                </h1>

                {/* <p className="text-xl text-white font-josefin text-justify">
                    Plongez dans l'univers fascinant de vos films et séries
                    préférés. Découvrez des{' '}
                    <span className="text-primary font-bold">
                        résumés détaillés des intrigues
                    </span>
                    , des informations sur les acteurs et les réalisateurs. Que
                    vous soyez un{' '}
                    <span className="text-primary font-bold">
                        cinéphile passionné
                    </span>{' '}
                    ou un{' '}
                    <span className="text-primary font-bold">
                        simple amateur de divertissement
                    </span>
                    , vous trouverez des{' '}
                    <span className="text-primary font-bold">
                        informations passionnantes
                    </span>{' '}
                    sur vos films et séries préférés. Explorez notre{' '}
                    <span className="text-primary font-bold">
                        vaste collection de titres populaires
                    </span>
                    , des{' '}
                    <span className="text-primary font-bold">
                        classiques intemporels
                    </span>{' '}
                    aux{' '}
                    <span className="text-primary font-bold">
                        dernières sorties
                    </span>{' '}
                    en passant par les{' '}
                    <span className="text-primary font-bold">
                        séries les plus appréciées
                    </span>
                    . Notre service est{' '}
                    <span className="text-primary font-bold">
                        la destination incontournable
                    </span>{' '}
                    pour les{' '}
                    <span className="text-primary font-bold">
                        fans de cinéma et de télévision
                    </span>{' '}
                    en quête d'informations approfondies sur les films et séries
                    qu'ils adorent.
                </p> */}
                <p className="text-xl text-white font-josefin text-justify">
                    Immerse yourself in the fascinating world of your favorite
                    movies and TV shows. Discover{' '}
                    <span className="text-primary font-bold">
                        detailed plot summaries
                    </span>
                    , cast and director information. Whether you're an{' '}
                    <span className="text-primary font-bold">
                        avid moviegoer
                    </span>{' '}
                    or{' '}
                    <span className="text-primary font-bold">
                        just an entertainment enthusiast
                    </span>
                    , you'll find{' '}
                    <span className="text-primary font-bold">
                        exciting informations
                    </span>{' '}
                    about your favorite movies and series. Explore our{' '}
                    <span className="text-primary font-bold">
                        vast collection of popular titles
                    </span>
                    , from{' '}
                    <span className="text-primary font-bold">
                        timeless classics
                    </span>{' '}
                    to the{' '}
                    <span className="text-primary font-bold">
                        latest releases
                    </span>{' '}
                    and{' '}
                    <span className="text-primary font-bold">
                        most popular series
                    </span>
                    . Our service is the{' '}
                    <span className="text-primary font-bold">
                        go-to destination
                    </span>{' '}
                    for{' '}
                    <span className="text-primary font-bold">
                        movie and TV fans
                    </span>{' '}
                    looking for{' '}
                    <span className="text-primary font-bold">
                        in-depth information
                    </span>{' '}
                    about the movies and TV shows they love.
                </p>
            </div>
            <div className="flex align-center justify-center pr-[5%] relative">
                <img src={diamond} alt="bg" className="w-3/4" />
                <img
                    src={informations_section}
                    alt="hero-img"
                    className="absolute top-1/2 left-[48%] transform -translate-x-1/2 -translate-y-1/2 w-[40%]"
                />
            </div>
        </section>
    )
}

export default Cinema
