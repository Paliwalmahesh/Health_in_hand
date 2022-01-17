dropLogo = document.getElementById("drop_logo");
dropLogo.addEventListener("click",dropList)
nav_list = document.getElementById("nav_list");
li = document.getElementsByTagName('li');

function dropList(){
    if(nav_list.style.visibility === "visible")
    {
        nav_list.style.visibility = "hidden";
        nav_list.style.height = "0rem";
        for(var i=0;i<li.length;i++){
        li[i].style.visibility = "hidden"}
        
    }

    else{
        nav_list.style.visibility = "visible";
        nav_list.style.height = "10rem";
        for(var i=0;i<li.length;i++){
        li[i].style.visibility = "visible"}
            
    }
}