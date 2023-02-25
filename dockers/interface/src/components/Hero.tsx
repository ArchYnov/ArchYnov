import HeroImage from "../assets/images/hero-image.jpg";
import { TiArrowRightOutline } from "react-icons/ti";


const Hero = () => {
    const handleClickScroll = () => {
        const element = document.getElementById('global-stats');
        if (element) {
          // 👇 Will scroll smoothly to the top of the next section
          element.scrollIntoView({ behavior: 'smooth' });
        }
    };
  return (
    <section className="h-screen">
        <div className="grid grid-cols-2 h-full items-center">
            <div className="ml-20 w-3/4">
                <h1 className="font-['Gugi'] text-8xl col-span-1 mb-5">
                    Archynov
                </h1>
                <p className="text-justify  mb-5">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                <button 
                    onClick={handleClickScroll} 
                    type="button" 
                    className="flex items-center text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">
                        <span className="mr-3">Global statistics</span> <TiArrowRightOutline size={20} />
                </button>
            </div>
            <div>
                <img src={HeroImage} alt="hero vector" className="w-auto col-span-4" />  
            </div>
        </div>
  </section>
  );
};

export default Hero;