import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav>
            <div>
                <NavLink to="/continents">Continents</NavLink>
            </div>
            <div>
                <NavLink to="/cities">Destination</NavLink>
                <NavLink to="/foods">Food & Travel</NavLink>
                <NavLink to="/blogs">Blog</NavLink>
                <NavLink to="/login">Login</NavLink>
            </div>
        </nav>
    )
}

export default NavBar;