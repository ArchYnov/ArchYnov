import diamond from '../assets/backgrounds/diamond.svg'
import analysis_section from '../assets/backgrounds/analysis.png'
import { Link } from 'react-router-dom'

const Analyses = () => {
    return (
        <section
            className="h-screen bg-background grid grid-cols-2 pt-[104px] mr-1/2"
            id="analyses"
        >
            <div className="flex align-center justify-center pr-[5%] relative">
                <img src={diamond} alt="bg" className="w-3/4" />
                <img
                    src={analysis_section}
                    alt="Analysisimage"
                    className="absolute top-[49%] left-[48%] transform -translate-x-1/2 -translate-y-1/2 w-[40%]"
                />
            </div>
            <div className="flex flex-col justify-center pl-[10%] pr-[10%]">
                <h1
                    className="text-white
                    font-newake text-8xl pb-1"
                >
                    ANALYSIS
                </h1>
                {/* 
                <p className="text-xl text-white font-josefin text-justify">
                    Nous vous proposons{' '}
                    <span className="text-primary font-bold">
                        d'explorer les données
                    </span>{' '}
                    de{' '}
                    <span className="text-primary font-bold">
                        l'industrie cinématographique
                    </span>{' '}
                    en utilisant des{' '}
                    <span className="text-primary font-bold">
                        techniques de deep learning
                    </span>
                    . Vous pourrez parcourir les{' '}
                    <span className="text-primary font-bold">
                        analyses de sentiment
                    </span>{' '}
                    qui permettent de déterminer les{' '}
                    <span className="text-primary font-bold">réactions</span> et
                    les{' '}
                    <span className="text-primary font-bold">
                        émotions du public
                    </span>{' '}
                    envers les films. Grâce à l'utilisation de{' '}
                    <span className="text-primary font-bold">
                        modèles de machine learning sophistiqués
                    </span>
                    , les analyses de cette section permettent d'extraire des{' '}
                    <span className="text-primary font-bold">
                        informations précieuses
                    </span>{' '}
                    à partir de{' '}
                    <span className="text-primary font-bold">
                        grandes quantités de données
                    </span>
                    , telles que des{' '}
                    <span className="text-primary font-bold">
                        avis de films
                    </span>
                    , des{' '}
                    <span className="text-primary font-bold">
                        commentaires de réseaux sociaux
                    </span>{' '}
                    et des
                    <span className="text-primary font-bold">
                        critiques de cinéma
                    </span>
                    . Ces informations sont ensuite utilisées pour déterminer{' '}
                    <span className="text-primary font-bold">
                        l'opinion générale
                    </span>{' '}
                    du public sur les films,
                    <span className="text-primary font-bold">
                        identifier les tendances émergentes
                    </span>
                    , et{' '}
                    <span className="text-primary font-bold">
                        prédire le succès ou l'échec
                    </span>{' '}
                    d'un film avant même sa sortie.
                </p> */}
                <p className="text-xl text-white font-josefin text-justify">
                    We offer you to{' '}
                    <span className="text-primary font-bold">explore data</span>{' '}
                    from the{' '}
                    <span className="text-primary font-bold">
                        movie industry
                    </span>{' '}
                    using{' '}
                    <span className="text-primary font-bold">
                        deep learning techniques
                    </span>{' '}
                    . You will be able to browse{' '}
                    <span className="text-primary font-bold">
                        sentiment analysis
                    </span>{' '}
                    that determine{' '}
                    <span className="text-primary font-bold">
                        audience reactions
                    </span>{' '}
                    and <span className="text-primary font-bold">emotions</span>{' '}
                    towards movies. Using{' '}
                    <span className="text-primary font-bold">
                        sophisticated deep learning models
                    </span>
                    , the analytics in this section{' '}
                    <span className="text-primary font-bold">
                        extract valuable informations
                    </span>{' '}
                    from{' '}
                    <span className="text-primary font-bold">
                        large amounts of data
                    </span>
                    , such as{' '}
                    <span className="text-primary font-bold">
                        movie reviews
                    </span>{' '}
                    and{' '}
                    <span className="text-primary font-bold">
                        social media comments
                    </span>
                    . This information is then used to determine the{' '}
                    <span className="text-primary font-bold">
                        general public's opinion of movies
                    </span>
                    ,{' '}
                    <span className="text-primary font-bold">
                        identify emerging trends
                    </span>
                    , and{' '}
                    <span className="text-primary font-bold">
                        predict the success or failure
                    </span>{' '}
                    of a movie before it is even released.
                </p>
                <div className="pt-9 flex justify-end">
                    <Link to="/movies">
                        <button className="text-4xl cursor-pointer decoration-none text-neon border-4 border-neon py-4 px-3 font-josefin rounded-lg btn-shadows neon-btn">
                            Check out our movies
                        </button>
                    </Link>
                </div>
            </div>
        </section>
    )
}

export default Analyses
