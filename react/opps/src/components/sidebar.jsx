import React from 'react';
import './Sidebar.css'; // Import your CSS file for styling if needed

const Sidebar = () => {
  const topItems = ['Home', 'About', 'Services'];
  const bottomItems = ['Contact'];

  return (
    <div className="sidebar">
      <ul className="sidebar-list">
        {topItems.map((item, index) => (
          <li key={index} className="sidebar-item">
            {item}
          </li>
        ))}
      </ul>
      {/* <hr className="sidebar-divider" />  */}
      <ul className="sidebar-listB">
        {bottomItems.map((item, index) => (
          <li key={index} className="sidebar-item">
            {item}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Sidebar;
