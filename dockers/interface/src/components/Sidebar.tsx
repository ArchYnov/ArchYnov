// import { useState } from 'react'
// import React from 'react'
// import { HiMenuAlt3 } from 'react-icons/hi'
// import { MdOutlineDashboard } from 'react-icons/md'
// import { RiSettings4Line } from 'react-icons/ri'
// import { TbReportAnalytics } from 'react-icons/tb'
// import { AiOutlineUser, AiOutlineHeart } from 'react-icons/ai'
// import { FiMessageSquare, FiFolder, FiShoppingCart } from 'react-icons/fi'
// import { Link } from 'react-router-dom'

// const Sidebar = () => {
//     const menus = [
//         { name: 'Dashboard', link: '/', icon: MdOutlineDashboard },
//         { name: 'User', link: '/', icon: AiOutlineUser },
//         { name: 'Messages', link: '/', icon: FiMessageSquare },

//         { name: 'Analytics', link: '/', icon: TbReportAnalytics, margin: true },
//         { name: 'File Manager', link: '/', icon: FiFolder },
//         { name: 'Cart', link: '/', icon: FiShoppingCart },

//         { name: 'Saved', link: '/', icon: AiOutlineHeart, margin: true },
//         { name: 'Setting', link: '/', icon: RiSettings4Line },
//     ]
//     const [open, setOpen] = useState(true)
//     return (
//         <div
//             className={`bg-[#0e0e0e] min-h-screen drop-shadow-[-5px 0 5px -5px #333] fixed ${
//                 open ? 'w-[16rem]' : 'w-[4rem]'
//             } duration-500 text-gray-100 px-4`}
//         >
//             <div className="py-3 flex justify-end">
//                 <HiMenuAlt3
//                     size={26}
//                     // className="cursor-pointer"
//                     style={{
//                         transitionDelay: `100ms`,
//                     }}
//                     className={`cursor-pointer rotate-0 ${
//                         !open && 'rotate-180'
//                     }`}
//                     onClick={() => setOpen(!open)}
//                 />
//             </div>
//             <div className="mt-4 flex flex-col gap-4 relative">
//                 {menus?.map((menu, i) => (
//                     <Link
//                         to={menu?.link}
//                         key={i}
//                         className={` ${
//                             menu?.margin && 'mt-5'
//                         } group flex items-center text-sm  gap-3.5 font-medium p-2 hover:bg-gray-800 rounded-md`}
//                     >
//                         <div>
//                             {React.createElement(menu?.icon, { size: '20' })}
//                         </div>
//                         <h2
//                             style={{
//                                 transitionDelay: `${i + 1}00ms`,
//                             }}
//                             className={`whitespace-pre duration-500 ${
//                                 !open &&
//                                 'opacity-0 translate-x-28 overflow-hidden'
//                             }`}
//                         >
//                             {menu?.name}
//                         </h2>
//                         <h2
//                             className={`${
//                                 open && 'hidden'
//                             } absolute left-48 bg-white font-semibold whitespace-pre text-gray-900 rounded-md drop-shadow-lg px-0 py-0 w-0 overflow-hidden group-hover:px-2 group-hover:py-1 group-hover:left-14 group-hover:duration-300 group-hover:w-fit  `}
//                         >
//                             {menu?.name}
//                         </h2>
//                     </Link>
//                 ))}
//             </div>
//         </div>
//     )
// }

export default {}
