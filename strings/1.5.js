const string1 = "pal"
const string2 = "pale"

if(string1 === string2){
 console.log(true);
 return;
}

if(Math.abs(string1.length - string2.length)>1){
 console.log(false);
 return;
}

console.log('Implementation missing, exercise is incomplete');


