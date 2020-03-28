const string1 = "abcszz"
const string2 = "bszcaz"

if(string1.length !== string2.length){
 console.log(false);
 return;
}

let string1Keys = {}
let string2Keys = {}

for(let character of string1) {
 
 if(!string2.includes(character)) {
  console.log(false);
  return;
 }

 if(string1Keys.hasOwnProperty(character)){
  string1Keys[character] += 1;
 } else {
  string1Keys[character] = 1;
 } 

}

for(let character of string2) {
 
 if(!string1.includes(character)) {
   console.log(false);
   return;
 }

 if(string2Keys.hasOwnProperty(character)){
  string2Keys[character] += 1;
 } else {
  string2Keys[character] = 1;
 } 

}

for (key in string1Keys) {
 if(string1Keys[key] !== string2Keys[key]) {
   console.log(false);
   return;
 }
}
console.log(true);


