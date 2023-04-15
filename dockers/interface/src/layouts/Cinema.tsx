import diamond from '../assets/backgrounds/diamond.svg'
import cinema_section from '../assets/backgrounds/cinema.png'
import StatFrame from '../components/StatFrame'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'

const Cinema = () => {
    // const { data, status } = useQuery('myData', () =>
    //     axios.get('/my-api-endpoint').then((res) => res.data)
    // )

    const { isLoading, error, data } = useQuery(['moviesNumber'], () =>
        axios
            .get('http://localhost:5000/api/v1/movies/number')
            .then((res) => res.data.result)
    )

    return (
        <section
            className="h-screen bg-background grid grid-cols-2 pt-[104px] mr-1/2"
            id="cinema"
        >
            <div className="flex align-center justify-center pr-[5%] relative">
                <img src={diamond} alt="bg" className="w-3/4" />
                <img
                    src={cinema_section}
                    alt="hero-img"
                    className="absolute top-1/2 left-[45%] transform -translate-x-1/2 -translate-y-1/2 w-[40%]"
                />
            </div>
            <div className="flex flex-col justify-center pl-[10%] pr-[10%]">
                <h1
                    className="text-white
                    font-newake text-8xl pb-1"
                >
                    CINÉMA
                </h1>

                <p className="text-xl text-white font-josefin text-justify">
                    Retrouvez un large choix de{' '}
                    <span className="text-primary font-bold">films</span> et{' '}
                    <span className="text-primary font-bold">séries</span> afin
                    de parfaire votre{' '}
                    <span className="text-primary font-bold">
                        culture cinématographique
                    </span>
                    . Notre catalogue est{' '}
                    <span className="text-primary font-bold">
                        constamment mis à jour
                    </span>{' '}
                    pour vous offrir les{' '}
                    <span className="text-primary font-bold">
                        dernières nouveautés
                    </span>
                    , ainsi que les titres les{' '}
                    <span className="text-primary font-bold">
                        plus populaires
                    </span>{' '}
                    et les{' '}
                    <span className="text-primary font-bold">
                        plus appréciés
                    </span>{' '}
                    du public. Vous pouvez parcourir notre collection de films
                    et de séries en utilisant nos filtres pratiques, qui vous
                    permettent de trier par genre, année, réalisateur ou acteur.{' '}
                </p>
                <div className="grid grid-cols-2 gap-10 pt-5">
                    <StatFrame stat_name="Films / Séries" stat={data} />
                    <StatFrame stat_name="Genres" stat="15" />
                </div>
            </div>
        </section>
    )
}

export default Cinema
