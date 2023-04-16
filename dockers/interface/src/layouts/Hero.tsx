import HeroImage from '../assets/images/hero-image.jpg'
import { TiArrowRightOutline } from 'react-icons/ti'
import blob from '../assets/backgrounds/blob.svg'
import hero_img from '../assets/backgrounds/hero_img.svg'

const Hero = () => {
    const handleClickScrollToCinema = () => {
        const element = document.getElementById('cinema')
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' })
        }
    }
    const handleClickScrollToInformations = () => {
        const element = document.getElementById('informations')
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' })
        }
    }
    const handleClickScrollToAnalyses = () => {
        const element = document.getElementById('analyses')
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' })
        }
    }
    return (
        <section className="h-screen bg-background grid grid-cols-2 pt-[104px]">
            <div className="flex flex-col justify-center pl-[10%]">
                <h1
                    data-text="CINEMA"
                    className="text-white
                    font-newake relative text-8xl mb-20 cursor-pointer w-fit neon-title"
                    onClick={handleClickScrollToCinema}
                >
                    CINÉMA
                </h1>
                <h1
                    className="text-white font-newake text-8xl mb-20 cursor-pointer w-fit neon-title"
                    onClick={handleClickScrollToInformations}
                >
                    INFORMATIONS
                </h1>
                <h1
                    className="font-newake text-white text-8xl cursor-pointer w-fit neon-title"
                    onClick={handleClickScrollToAnalyses}
                >
                    ANALYSIS
                </h1>
            </div>
            <div className="flex align-center justify-center pr-[5%] relative">
                <img src={blob} alt="bg" className="w-3/4" />
                <img
                    src={hero_img}
                    alt="hero-img"
                    className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-[45%]"
                />
            </div>
        </section>
    )
}

export default Hero
