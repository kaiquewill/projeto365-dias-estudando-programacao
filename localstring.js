



let myNum = .9;

// myNum = myNum.toLocaleString("en-US"); // US english


// myNum = myNum.toLocaleString("hi-IN"); hindi 

// myNum = myNum.toLocaleString("de-DE");

//myNum = myNum.toLocaleString("en-US", {style:"currency", currency:"USD" })

//myNum = myNum.toLocaleString("hi-IN", {style:"currency", currency:"INR" })

// myNum = myNum.toLocaleString(undefined, {style: "percent"})

myNum = myNum.toLocaleString(undefined,{style:"unit", unit:"celsius"})
console.log(myNum);