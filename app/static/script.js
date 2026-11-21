async function sendPrompt(){

let prompt=document.getElementById("prompt").value;

const response=await fetch("/process",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

prompt:prompt

})

});

const data=await response.json();

document.getElementById("category").innerHTML=data.category;

document.getElementById("response").innerHTML=data.response;

}