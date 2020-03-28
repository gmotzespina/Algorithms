const stringToCompress = "aaaBBbcciissAnnnnnnnnn"
console.log(stringToCompress);

let compressedString = ""

let lastCharacter = stringToCompress[0];
let characterCount = 0;
for (character of stringToCompress) {
 if(character === lastCharacter) {
  characterCount += 1;
 } else {
  compressedString += `${lastCharacter}${characterCount}`;
  lastCharacter = character;
  characterCount = 1;
 }
}
compressedString += `${lastCharacter}${characterCount}`
console.log(compressedString);

