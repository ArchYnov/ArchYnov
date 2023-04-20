import React from 'react'
interface StatFrameProps {
    stat: string
    stat_name: string
}
const StatFrame = (props: StatFrameProps) => {
    return (
        // <div className=" my-[5%] p-7 border-4 border-primary shadow-[0_0_15px_5px] shadow-primary">
        //     <h2 className="text-white text-4xl font-bold text-center">
        //         {props.stat}
        //     </h2>
        //     <h3 className="text-white text-xl text-center font-thin">
        //         {props.stat_name}
        //     </h3>
        // </div>

        <div className="bg-transparent h-fit px-4 py-4 rounded-xl text-center justify-center items-center my-4 mr-8  text-neon border-4 border-neon badge-border-shadow w-full">
            <h2 className="text-8xl pb-2 font-newake badge-text-shadow flex items-end justify-center">
                {props.stat}
            </h2>
            <h3 className="text-md font-poppins font-medium">
                {props.stat_name}
            </h3>
        </div>
    )
}

export default StatFrame
