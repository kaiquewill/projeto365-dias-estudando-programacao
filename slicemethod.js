let fullName = "Bro code"
let fistName; 
let lastName;

//fistname= fullName.slice(0,6)
//lastname= fullName.slice(7);

fistName = fullName.slice(0, fullName.indexOf(" "));
lastName = fullName.slice(fullName.indexOf(" ") + 1);

console.log(fistName);
console.log(lastName);



