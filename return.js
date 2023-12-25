




let area;
let width;
let height;

width = window.prompt("enter width")
height = window.prompt("enter height")


area = getArea(width, height)
console.log(" the area result is:" , area)

function getArea(width,height){
    let result = (width * height)
    return result

}