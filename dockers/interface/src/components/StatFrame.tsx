import React from 'react'
interface StatFrameProps {
    stat: string
    stat_name: string
}
const StatFrame = (props: StatFrameProps) => {
    return (
        <div className=" my-[5%] p-7 border-4 border-primary shadow-[0_0_15px_5px] shadow-primary">
            <h2 className="text-white text-4xl font-bold text-center">
                {props.stat}
            </h2>
            <h3 className="text-white text-xl text-center font-thin">
                {props.stat_name}
            </h3>
        </div>
    )
}

export default StatFrame
