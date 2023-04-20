import { Analyses, Informations, Cinema, Hero } from '../layouts'
import { ScrollTopButton } from '../components'

const Home = () => {
    return (
        <main>
            <Hero />
            <Cinema />
            <Informations />
            <Analyses />
            <ScrollTopButton />
        </main>
    )
}

export default Home
