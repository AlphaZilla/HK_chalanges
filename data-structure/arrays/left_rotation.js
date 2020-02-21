let firstInput = 5;
let secondInput = 4;
let lastInput = [1, 2, 3, 4, 5];

function rotateLeft(arrayLength, nSteps, theList) {
  for (let x = 0; x < nSteps; x++) {
    theList.push(theList.shift());
  }

  return theList.join(" ");
}

console.log(rotateLeft(firstInput, secondInput, lastInput));
