import { useState } from 'react'

import { close, menu } from '../assets'
import { navLinks } from '../constants'
import { RiMovie2Line } from 'react-icons/ri'

import { useScrollPosition } from '../hooks'

const Navbar = () => {
    const [active, setActive] = useState('Home')
    const [toggle, setToggle] = useState(false)

    function classNames(...classes: string[]) {
        return classes.filter(Boolean).join(' ')
    }

    const scrollPosition = useScrollPosition()
    console.log(scrollPosition)

    return (
        <nav
            className={classNames(
                scrollPosition > 0
                    ? 'shadow-md shadow-primary bg-background'
                    : 'shadow-none bg-background',
                'transition-shadow w-full flex py-6 justify-between items-center navbar fixed top-0 z-10'
            )}
        >
            <div className="ml-5 flex items-center">
                <RiMovie2Line className="text-primary text-4xl mr-4 " />{' '}
                <span className="text-white text-3xl font-newake">Cinews</span>
            </div>

            <ul className="list-none sm:flex hidden justify-end items-center flex-1">
                {navLinks.map((nav, index) => (
                    <li
                        key={nav.id}
                        className={`font-poppins font-normal cursor-pointer text-[16px] mr-10 ${
                            active === nav.title ? 'text-primary' : 'text-white'
                        } `}
                        onClick={() => setActive(nav.title)}
                    >
                        <a href={`#${nav.id}`}>{nav.title}</a>
                    </li>
                ))}
            </ul>
            <div className="sm:hidden flex flex-1 justify-end items-center ">
                <img
                    src={toggle ? close : menu}
                    alt="menu"
                    className="w-[28px] h-[28px] object-contain mr-5"
                    onClick={() => setToggle(!toggle)}
                />

                <div
                    className={`${
                        !toggle ? 'hidden' : 'flex'
                    } p-6 bg-black bg-black-gradient absolute top-20 right-0 mx-4 my-2 min-w-[140px] rounded-xl sidebar`}
                >
                    <ul className="list-none flex justify-end items-start flex-1 flex-col">
                        {navLinks.map((nav, index) => (
                            <li
                                key={nav.id}
                                className={`font-poppins font-medium cursor-pointer text-[16px] ${
                                    active === nav.title
                                        ? 'text-primary'
                                        : 'text-white'
                                } ${
                                    index === navLinks.length - 1
                                        ? 'mb-0'
                                        : 'mb-4'
                                }`}
                                onClick={() => setActive(nav.title)}
                            >
                                <a href={`#${nav.id}`}>{nav.title}</a>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </nav>
    )
}

export default Navbar
