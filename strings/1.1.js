const string = "this";

let keys = {};

for(let character of string) {
 if(keys.hasOwnProperty(character)){
  keys[character] += 1;
 } else {
  keys[character] = 1;
 }
}

for(let key in keys) {
  if(keys[key] > 1){
   console.log(false);
   return;
  }
}
console.log(true);
