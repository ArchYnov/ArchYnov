import ReactDOM from 'react-dom/client'
import './assets/style/index.scss'
import Root from './views/Root'
import reportWebVitals from './reportWebVitals'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { Home, Movies } from './pages'

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement)
const router = createBrowserRouter([
    {
        path: '/',
        element: <Root />,
        children: [
            {
                index: true,
                element: <Home />,
            },
            {
                path: 'movies',
                element: <Movies />,
            },
        ],
    },
])
root.render(<RouterProvider router={router} />)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
