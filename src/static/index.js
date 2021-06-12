console.log("Hi there!")

email = document.getElementById(email);

function check_Email(email){
    var regex = /^(([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5}){1,25})+([;.](([a-zA-Z0-9_\-\.]+)@{[a-zA-Z0-9_\-\.]+0\.([a-zA-Z]{2,5}){1,25})+)*$/;
    if(regex.test(email.value)){
      return true;
      alert("Congrats! This is a valid Email email");
    }
    else{
      alert("This is not a valid email address");
      return false;
    }
  }