import React from 'react';
import './Navbar.css'; // Import your CSS file for styling if needed
import {FaBars, FaUser, FaBell} from 'react-icons/fa'

const Navbar = () => {
  return (
    <div className="navbar">
      <div className="logo">
        <img src="src/assets/logo-removebg-preview.png" alt="Logo" />
      </div>
      <ul className="nav-links">
        <div>
          <FaBars className="Bars"/>
          <FaUser className="User"/>
          <FaBell className="Bell"/>
        </div>
        <li className="nav-item">MASINDE MULIRO UNIVERSITY OF SCIENCE AND TECHNOLOGY</li>
        <li className="nav-item">Hi, User</li>
      </ul>
    </div>
  );
};

export default Navbar;
