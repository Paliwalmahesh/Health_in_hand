var user = document.getElementById('userDOC1');
user.addEventListener('blur',validity11);
function validity11(){
      
  
  var username = document.querySelector("#userDOC1").value;
  const request = new XMLHttpRequest();
      
      

      // If specified, responseType must be empty string or "text"11
    request.responseType = 'json';

      request.onload = function () {
            if (request.readyState === request.DONE) {
                if (request.status === 200) {

                    
                    var us = request.response.usernames;
                    var val = us.includes(username);
                    console.log(val);

                    if(val){
                        document.getElementById('userValid1').innerHTML = "This Username is in the system ";
                        document.getElementById('userDOC1').style.borderColor = "green";
                        document.getElementById('signup_btn').disabled = false;

                    
                    }
                    else{
                        document.getElementById('userValid1').innerHTML = "This Username not in system";
                      document.getElementById('userDOC1').style.borderColor = "red";
                      document.getElementById('signup_btn').disabled = true;
                      
                    }
                }
            }
        }

        request.open('GET', 'validate_username', true);
        
      
      request.send();
      
      };