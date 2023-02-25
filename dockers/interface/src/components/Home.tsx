import { useState } from "react";
import HeroImage from "../assets/images/hero-image.jpg";
import GlobalStats from "./GlobalStats";
import Hero from "./Hero";
import { FaChevronUp } from "react-icons/fa";

const Home = () => {
  const [showScroll, setShowScroll] = useState(false);

  const checkScrollTop = () => {
    if (!showScroll && window.pageYOffset > 400){
      setShowScroll(true);
    } else if (showScroll && window.pageYOffset <= 400){
      setShowScroll(false);
    }
  };

  const scrollTop = () =>{
    window.scrollTo({top: 0, behavior: 'smooth'});
  };

  window.addEventListener('scroll', checkScrollTop);

  return (
    <section className="home ml-[16rem]">
        <Hero/>
        <GlobalStats/>
        <button className={"scrollTop bg-blue-500 text-white rounded-full text-center fixed bottom-4 right-4 h-12 w-12 flex justify-center items-center cursor-pointer shadow-md transition-opacity duration-300" + (showScroll ? ' opacity-100' : ' opacity-0')} onClick={scrollTop} style={{display: showScroll ? 'flex' : 'none'}}><FaChevronUp size={20} /></button>
    </section>
  );
};

export default Home;