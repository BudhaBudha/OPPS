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

document.querySelector(".form").addEventListener('submit', function (e) {
    e.preventDefault();
    const data = {
        username: document.getElementById('userName').value,
        email: document.getElementById('email').value,
        password: document.getElementById('pass1').value,
        cpassword: document.getElementById('pass2').value,
    };

    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        if (result.success) {
            // Redirect to the user profile page or show a success message.
        } else {
            // Display an error message.
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});