import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar: React.FC = () => {
    return (
        <nav className="navbar">
            <ul className='navList'>
                <li className='navItem'>
                    <NavLink to="/" className='navLink'>Home</NavLink>
                </li>
                <li className='navItem'>
                    <NavLink to="/about" className='navLink'>About</NavLink>
                </li>
            </ul>

        </nav>
    );
};

export default Navbar;