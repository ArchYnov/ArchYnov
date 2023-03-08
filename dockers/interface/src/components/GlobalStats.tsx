import GlobalStatsImage from "../assets/images/global-stats.jpg";
import { LineChart, Line } from 'recharts';
const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400},{name: 'Page B', uv: 400, pv: 2400, amt: 2400}];


const GlobalStats = () => {
  return (
    <section className="h-screen" id="global-stats">
        <div className="grid grid-cols-2 h-full items-center bg-[#f7f7f7]">
            <div >
                <img src={GlobalStatsImage} alt="hero vector" className="w-auto" />  
            </div>
            <div className="ml-20 w-3/4">
                <h1 className="font-['Gugi'] text-4xl mb-4">
                    Global Statistics
                </h1>
                <div>
                    <LineChart width={400} height={400} data={data}>
                        <Line type="monotone" dataKey="uv" stroke="#8884d8" />
                    </LineChart>
                    <p className="text-justify">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                </div>
            </div>
        </div>
  </section>
  );
};

export default GlobalStats;