var animated = document.getElementById("animated");
var quote = document.getElementById("quote");
animated.addEventListener('animationiteration',anim_end);


var str1 = "If your health is not right the rest of your day will go wrong";
var str2 = "The one who has health has hope, and who has hope has everything.";

quote.innerText = str1;

var count = 0;
function anim_end()
{
    count = count+1
    if (count%2 == 0)
    {
        if (quote.innerText == str1 )
        {
            quote.innerText = str2;
        }
        else{
            quote.innerText = str1;
        }
    }
}

toggle_button = document.getElementById("toggle_button");
service = document.getElementById("services")
toggle_button.addEventListener("click",function(){
    service.style.transform="translatY(25%)";
})



