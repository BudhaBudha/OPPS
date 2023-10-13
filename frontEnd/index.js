const NavBar = document.querySelector(".toggle");
const Sidebar = document.querySelector(".sidepanel");
const Main = document.querySelector(".mainscreen");

NavBar.addEventListener("click",()=>{
    Sidebar.classList.toggle("active");
    Main.classList.toggle("active");
});

let profilePic = document.getElementById("profilePic");
let inputFile = document.getElementById("input-file");

inputFile.onchange= function(){
    profilePic.src =URL.createObjectURL(inputFile.files[0]);           
}