import { initializeApp } from 'firebase/app';
import { getDatabase } from "firebase/database";

let nameInput, rollInput, emailInput, contactInput, skillsInput, reasonInput, radio;
const firebaseConfig = {
    //still to add
  };

  const app = initializeApp(firebaseConfig);
  const database = getDatabase();

function submitlocal(){
    console.log("onsubmitloacl")

    nameInput = document.getElementById("name");
    rollInput = document.getElementById("rollno");
    emailInput = document.getElementById("email");
    skillsInput = document.getElementById("skills");
    contactInput = document.getElementById("contact");
    reasonInput = document.getElementById("reason");
    radio = document.getElementById("radio");

    if(isFormComplete()){
        if(radio.checked){
            app.document()


        }else{
            alert("Please Accept the conditions!")
        }
    }else{
        alert("Please complete the Form!")
    }
    
    
}

function isFormComplete(){
    form = document.getElementsByClassName("form");
    let boolean=true;
    for (let i = 0; i < form.length; i++) {
        if(form[i].value=="" ){
            boolean = false;
            console.log("iteration"+i)
            break;
        }
        if(i==form.length){
            boolean = true;
        }
        
      }
      return boolean;
}
