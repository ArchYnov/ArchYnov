import React, { FunctionComponent, useState } from 'react'
import Home from '../pages/Home'
import Navbar from '../components/Navbar'
import { Outlet } from 'react-router-dom'
// import Sidebar from '../components/Sidebar'

const Root: FunctionComponent = () => {
    return (
        <div>
            <Navbar />
            <Outlet />
        </div>
    )
}

export default Root
