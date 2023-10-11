const NavBar = document.querySelector(".toggle");
const Sidebar = document.querySelector(".sidepanel");
const Main = document.querySelector(".mainscreen");

NavBar.addEventListener("click",()=>{
    Sidebar.classList.toggle("active");
    Main.classList.toggle("active");
});