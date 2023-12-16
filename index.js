let username;
document.getElementById("mybutton").onclick=function(){
    username = document.getElementById("mytext").value;
    console.log(username);
    document.getElementById("mylabel").innerHTML = "hello " + username;
}