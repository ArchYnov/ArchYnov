import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { NewsCard, ScrollTopButton } from '../components'

const News = () => {
    const news = [
        {
            id: '1000020455',
            index: 'allocineaffiche',
            source: {
                title: "Star Wars : l'Etoile de la mort à la poubelle ? Le destin invraisemblable de l'arme ultime de Dark Vador",
                text: "Objet iconique d'une saga qui ne l'est pas moins, l'Etoile de la mort faisait son apparition dans le premier volet Star Wars, en 1977. Sa maquette originale a connu un destin assez incroyable, et même émouvant...",
                date: [2023, 4, 14, 17, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'POSITIVE',
                score: 0.8920488357543945,
            },
        },
        {
            id: '1000020216',
            index: 'allocineaffiche',
            source: {
                title: 'Au fait, ça veut dire quoi DC ?',
                text: "A l'instar des films Marvel, les productions super-héroïques DC tiennent aujourd'hui une place majeure dans le paysage cinématographique mondial. Mais au fait, elles veulent dire quoi, les initiales DC ?",
                date: [2023, 4, 14, 16, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'POSITIVE',
                score: 0.7183932065963745,
            },
        },
        {
            id: '1000020521',
            index: 'allocineaffiche',
            source: {
                title: "James Bond jeune ? Voilà pourquoi ce n'est jamais arrivé et pourquoi Daniel Craig a été choisi",
                text: "A l'origine, James Bond devait être joué par un jeune comédien dans \"Casino Royale\". Mais la production a vite changé son fusil d'épaule, ainsi que le révèle aujourd'hui la directrice de casting Debbie McWilliams.",
                date: [2023, 4, 14, 15, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'NEGATIVE',
                score: 0.9136056900024414,
            },
        },
        {
            id: '1000019767',
            index: 'allocineaffiche',
            source: {
                title: 'Super Mario : cette série animée des années 90 que tout le monde a oubliée',
                text: 'Alors que "Super Mario Bros le film" est en salles depuis le 5 avril, (re)découvrez la série animée qui revisitait déjà la célèbre franchise vidéoludique de Nintendo en 1989.',
                date: [2023, 4, 14, 15, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'NEGATIVE',
                score: 0.9430292248725891,
            },
        },
        {
            id: '1000020609',
            index: 'allocineaffiche',
            source: {
                title: 'Spider-Man Far From Home : le méchant du film a failli jouer... le super-héros Marvel !',
                text: 'Disponible sur Disney+, Spider-Man : Far From Home réunit à l’écran Tom Holland et Jake Gyllenhaal. Une première incursion dans l’univers Marvel pour celui qui a pourtant déjà failli se glisser sous le costume du célèbre super-héros…',
                date: [2023, 4, 14, 14, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'NEGATIVE',
                score: 0.89261394739151,
            },
        },
        {
            id: '1000020539',
            index: 'allocineaffiche',
            source: {
                title: "\"Si un remake est fait, c'est parce que l'original est nul. Et le mien ne l'est pas\" : ce réalisateur critique Hollywood pour avoir refait son film",
                text: "Réalisateur du film d'horreur \"Morse\", qui revisitait intelligemment l'increvable mythe du vampire, Tomas Alfredson n'avait pas du tout apprécié l'annonce d'un remake sauce hollywoodienne de son film, et ne s'était pas privé de le faire savoir....",
                date: [2023, 4, 14, 9, 34, 33, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'NEGATIVE',
                score: 0.5223713517189026,
            },
        },
        {
            id: '1000020356',
            index: 'allocineaffiche',
            source: {
                title: 'Donjons & Dragons : découvrez (et commandez) les figurines POP des héros du film !',
                text: 'Votre collection de Funko POP est sur le point de s’agrandir… de six figurines à l’effigie des héros de “Donjons & Dragons : L’Honneur des voleurs” actuellement au cinéma !',
                date: [2023, 4, 14, 9, 30, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'POSITIVE',
                score: 0.953042209148407,
            },
        },
        {
            id: '1000020531',
            index: 'allocineaffiche',
            source: {
                title: 'Bande-annonce Migration : après Super Mario, un Français aux commandes du film Illumination de Noël !',
                text: 'Après Les Minions, Tous en scène et Super Mario Bros, découvrez le nouveau film des studios Illumination : Migration de Benjamin Renner (Le Grand Méchant Renard et autres contes).',
                date: [2023, 4, 14, 9, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'POSITIVE',
                score: 0.9811483025550842,
            },
        },
        {
            id: '1000020529',
            index: 'allocineaffiche',
            source: {
                title: "Horreur : \"L'un des films les plus effrayants que j'ai vus depuis longtemps\"... Cette adaptation de Stephen King fera-t-elle l'événement au cinéma ?",
                text: 'Vu récemment à l\'affiche de "L\'Etrangleur de Boston" sur Disney+, David Dastmalchian ne tarit pas d\'éloges sur "Le Croque-mitaine", adaptation de Stephen King attendue le 31 mai dans nos salles et dans laquelle il joue.',
                date: [2023, 4, 14, 9, 0, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'POSITIVE',
                score: 0.8736169338226318,
            },
        },
        {
            id: '1000020526',
            index: 'allocineaffiche',
            source: {
                title: "Avengers 3 a une scène coupée de 45 minutes et on sait ce qu'il y a dedans !",
                text: "Jim Starlin, créateur du personnage de Thanos, grand méchant d'Avengers 3 et 4, a révélé qu'il existe une séquence de combat de 45 minutes coupée d'\"Avengers: Infinity War\".",
                date: [2023, 4, 14, 8, 40, 0, 4, 104, 0],
            },
            sentiment_analysis: {
                label: 'POSITIVE',
                score: 0.9934040904045105,
            },
        },
        {
            id: '1000020403',
            index: 'allocineaffiche',
            source: {
                title: 'Noté 5/5, le meilleur film des années 80 ressort au cinéma et va vous mettre KO !',
                text: "En 1980, le réalisateur Martin Scorsese nous offre un long-métrage qui va faire l'effet d'une déflagration monumentale dans le monde du cinéma : Raging Bull ! Cette oeuvre majeure ressort le 12 avril en version restaurée 4K.",
                date: [2023, 4, 13, 15, 0, 0, 3, 103, 0],
            },
            sentiment_analysis: {
                label: 'NEGATIVE',
                score: 0.7498689889907837,
            },
        },
    ]

    // const { isLoading, error, data } = useQuery({
    //     queryKey: ['newMovies'],
    //     queryFn: async () =>
    //         await axios
    //             .get('https://localhost:5000/api/v1/news')
    //             .then((res) => res.data.result),
    // })

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
                {news.map((item) => (
                    <NewsCard
                        key={item.id}
                        title={item.source.title}
                        description={item.source.text}
                        date={item.source.date}
                        source={item.index}
                    />
                ))}
            </div>
            <ScrollTopButton />
        </main>
    )
}

export default News
