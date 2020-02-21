// let hrInput = [
//   [1, 1, 1, 0, 0, 0],
//   [0, 1, 0, 0, 0, 0],
//   [1, 1, 1, 0, 0, 0],
//   [0, 0, 2, 4, 4, 0],
//   [0, 0, 0, 2, 0, 0],
//   [0, 0, 1, 2, 4, 0]
// ];

let hrInput = [
  [-1, -1, 0, -9, -2, -2],
  [-2, -1, -6, -8, -2, -5],
  [-1, -1, -1, -2, -3, -4],
  [-1, -9, -2, -4, -4, -5],
  [-7, -3, -3, -2, -9, -9],
  [-1, -3, -1, -2, -4, -5]
];

// let hrInput = [
//   ['a', 'b', 'c', 'd', 'e', 'f'],
//   ['f', 'g', 'h', 'i', 'j', 'k'],
//   ['l', 'm', 'm', 'o', 'p', 'r'],
//   [0, 0, 2, 4, 4, 0],
//   [0, 0, 0, 2, 0, 0],
//   [0, 0, 1, 2, 4, 0]
// ];

// console.log("initial input :");
// console.log(hrInput);
// console.log("--------------");

function hourglassSum(arr) {
  // console.log(arr);
  // console.log(arr[0][0], arr[0][1], arr[0][2]);
  // console.log(arr[1][0], arr[1][1], arr[1][2]);
  // console.log(arr[2][0], arr[2][1], arr[2][2]);
  let biggestSum = -99999;
  for (let x = 0; x < 4; x++) {
    for (let y = 0; y < 4; y++) {
      let topHourGlass = [arr[x][y], arr[x][y + 1], arr[x][y + 2]];
      let middleHourGlass = [
        arr[x + 1][y],
        arr[x + 1][y + 1],
        arr[x + 1][y + 2]
      ];
      let bottomHourGlass = [
        arr[x + 2][y],
        arr[x + 2][y + 1],
        arr[x + 2][y + 2]
      ];
      let sumTopHourGlass = topHourGlass[0] + topHourGlass[1] + topHourGlass[2];
      let sumMiddleHourGlass = middleHourGlass[1];
      let sumBottomHourGlass =
        bottomHourGlass[0] + bottomHourGlass[1] + bottomHourGlass[2];

      let sumTotalHourGlass =
        sumTopHourGlass + sumMiddleHourGlass + sumBottomHourGlass;

      // console.log(topHourGlass);
      // console.log(middleHourGlass);
      // console.log(bottomHourGlass);
      // console.log("-----");
      // console.log(sumTotalHourGlass);
      // console.log("-----");

      if (sumTotalHourGlass >= biggestSum) {
        biggestSum = sumTotalHourGlass;
      }
    }
  }
  return biggestSum;
}

console.log(hourglassSum(hrInput));
