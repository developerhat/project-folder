//Linked to WebPageProject

function initialPrompt() {
var userAge = prompt("How old are you?");
var text;

if(userAge >= 21){
  alert("Congrats!! You're over 21!")
} else {
  alert("Aw darn! Shucks you're not 21.")
}

var favDrink = prompt("What's your favorite car?");
switch(favDrink) {
  case "GTI":
  text = "Great choice! The father of hot hatches";
  break;
  case "BRZ":
  text = "Ahh!! Solid choice with the BRZ!";
  break;
  case "M3":
  text = "Solid option! Will give you a run for your money";
  break;
  default:
  text = "That's not in our database. Sorry!";
  break;
}
alert(text);
}

//in this function, phrase & another are just parameter 1 & parameter 2
//This doesn't make sense completely to me rn but I know it will
function getPhrase(params){

  if(params.phrase){
  l = params.phrase.length;

}

  if (typeof params.another !== "undefined"){
    l += params.another.length;
  }


  return l;

}
//returning the function doesn't do anything. It returns the value
//the reason we see it printed is cos we console.log the thisLength variable


var p1 = "This is a long sentence";
var p2 = "This is a longerrrrr sentece";

var thisLength = getPhrase({phrase: p1, another:p2});
// the above variable is PASSING IN p1 & p2 to the getPhrase function!


console.log(thisLength);


//this function is able to locate the missing number within an array or list
//I don't really understand the whole function. Keep workin
function missingNumber(missingNo){
  var missing = -1;

  for(var i = 0; i <= missingNo.length; i++){
    if(missingNo.indexOf(i) === -1){
      missing = i;
    }
  }
  return missing;
}

var missingNo = [3, 8, 7, 9, 6, 0, 1, 12, 5, 14, 2, 19, 16, 18, 11, 10, 15, 13, 17, 20];

console.log(missingNumber(missingNo));


class Animal {

  constructor(name, height, weight){
    console.log("Created animal: " + name + " is " + weight + "lbs");
    this.name = name;
    this.height = height;
    this.weight = weight;

  }

  nameLength(){
    return this.name.length;
  }

}

Animal.planet = "Earth";


var dog = new Animal("Ace", 25, 90);
var fish = new Animal("Fishy", 2, .3);

console.log("The length of our fish's name is: " + fish.nameLength());
console.log("The length of our dog's name is: " + dog.nameLength());

console.log(dog.constructor.planet);
