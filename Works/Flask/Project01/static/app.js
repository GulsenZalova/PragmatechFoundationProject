catagories=["All","Media", "Illustration" , "Video", "Website"]
let nav=document.getElementsByClassName("Navbar")

for (catagory of catagories){
    nav.innerHTML += `<li>${catagory}</li>`
}
