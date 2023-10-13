import React from 'react';
import Sidebar from './components/sidebar';
import Navbar from './components/navbar';

import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

// export default App1;

const App = () => {
  return (
    <div className="app-container">
        <Navbar />
      <div className="content-container">
        <Sidebar />
        {/* Rest of your content */}
      </div>
    </div>
    );
  };
  
  export default App;