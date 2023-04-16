import { useState } from 'react'
import { FaChevronUp } from 'react-icons/fa'

const ScollTopButton = () => {
    const [showScroll, setShowScroll] = useState(false)

    const checkScrollTop = () => {
        if (!showScroll && window.pageYOffset > 400) {
            setShowScroll(true)
        } else if (showScroll && window.pageYOffset <= 400) {
            setShowScroll(false)
        }
    }

    const scrollTop = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' })
    }

    window.addEventListener('scroll', checkScrollTop)

    return (
        <button
            className={
                'scrollTop bg-primary text-white rounded-full text-center fixed bottom-4 right-4 h-12 w-12 flex justify-center items-center cursor-pointer shadow-md transition-opacity duration-300' +
                (showScroll ? ' opacity-100' : ' opacity-0')
            }
            onClick={scrollTop}
            style={{ display: showScroll ? 'flex' : 'none' }}
        >
            <FaChevronUp size={20} className="mt-[-2px]" />
        </button>
    )
}

export default ScollTopButton
