import React, { useState } from 'react'
import { Swiper, SwiperSlide } from 'swiper/react'
import { Autoplay, Pagination, Navigation } from 'swiper'
import 'swiper/css'
import 'swiper/css/navigation'
import 'swiper/css/pagination'
import { BsChevronLeft, BsChevronRight } from 'react-icons/bs'
import MovieCard from './MovieCard'
import { Link } from 'react-router-dom'

const Carousel = ({ movies }: { movies: any[] }) => {
    const [currentSlide, setCurrentSlide] = useState(0)
    const itemsPerPage = 4

    return (
        <div className="relative">
            <Swiper
                slidesPerView={itemsPerPage}
                slidesPerGroup={itemsPerPage}
                onSlideChange={(swiper) => setCurrentSlide(swiper.activeIndex)}
                pagination={{
                    clickable: true,
                }}
                spaceBetween={-10}
                navigation={{
                    prevEl: '.swiper-button-prev',
                    nextEl: '.swiper-button-next',
                }}
                modules={[Autoplay, Pagination, Navigation]}
            >
                <div className="swiper-button-prev text-primary">
                    <BsChevronLeft size="1.5em" />
                </div>
                <div className="swiper-button-next">
                    <BsChevronRight size="1.5em" />
                </div>
                {movies?.map((movie, id) => (
                    <SwiperSlide key={id}>
                        <Link
                            to={`/movie/${movie.id}`}
                            className="w-full h-full"
                        >
                            <MovieCard key={movie.id} movie={movie} />
                        </Link>
                    </SwiperSlide>
                ))}
            </Swiper>
        </div>
    )
}

export default Carousel
