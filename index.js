// let arr = [, , ,];
// // leght of the Array is 3 because it has 3 empty slots
// console.log(arr.length); // Output: 3
// let arr2 = ["i am bilal"];
// let reverceArr = arr2[0].split(" ").reverse().join(" ");
// // Split the string into characters, reverse them, and join back to a string
// console.log(reverceArr); // Output: 'labil ma i

// let reverceArrFun = str => {
//   return str.split(" ").reverse().join(" ");
// };
// console.log(reverceArrFun("i am bilal")); // Output: 'labil ma i
// let arr3 = ["i", "am", "bilal"];
// let reverceArrFun2 = arr => {
//   return arr.join(" ");
// };
// console.log(reverceArrFun2(arr3)); // Output: 'bilal am i'
// function returnArr(arr) {
//   return arr.join(" ");
// }
// console.log(returnArr(arr3)); // Output: 'bilal am i'
// let arr4 = "i am bilal";
// let reverceArrFun3 = str => {
//   return str.split(" ").reverse().join(" ");
// };
// console.log(reverceArrFun3(arr4)); // Output: 'labil ma i'
// let errFun = (a, b) => {
//   return a + b;
// };
// console.log(errFun(2, 3)); // Output: 5
// // check the string is palindrome or not
// // function isPalindrome(str) {
// //   let reversedStr = str.split("").reverse().join("");
// //   return str === reversedStr;
// // }
// // console.log(isPalindrome("madam")); // Output: true
// // console.log(isPalindrome("hello")); // Output: false
// // Check if a number is even or odd
// // function isEvenOrOdd(num) {
// //   return num % 2 === 0 ? "Even" : "Odd";
// // }
// // console.log(isEvenOrOdd(4)); // Output: Even
// // console.log(isEvenOrOdd(5)); // Output: Odd

// let isPalindrome = str => {
//   // Check if the string is a palindrome
//   let reversedStr = str.split("").reverse().join("");
//   return str === reversedStr;
// };
// console.log(isPalindrome("racecar")); // Output: true
// console.log(isPalindrome("hello")); // Output: false
// let isEvenOrOdd = num => {
//   // Check if a number is even or odd
//   return num % 2 === 0 ? "Even" : "Odd";
// };
// console.log(isEvenOrOdd(10)); // Output: Even
// console.log(isEvenOrOdd(11)); // Output: Odd

// // how to covert a string to an array
// let str = "Hello, World!";
// let arrFromStr = str.split(""); // Convert string to array of characters
// console.log(arrFromStr); // Output: ['H', 'e', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']
// // how to convert an array to a string
// let arrToStr = arrFromStr.join(""); // Convert array back to string
// console.log(arrToStr); // Output: 'Hello, World!'
// let srr2 = "Hello, World!";
// let arrFromStr2 = srr2.split("").reverse().join(""); // Convert string to array of characters, reverse, and join
// console.log(arrFromStr2); // Output: '!dlroW ,olleH'
// console.log(arrFromStr2.split(" ").reverse().join(" ")); // Output: '!dlroW ,olleH' (reversing the words in the string)
// // primitive data vs non primitive in js with example
// let primitiveDataTypes = {
//   string: "Hello",
//   number: 42,
//   boolean: true,
//   null: null,
//   undefined: undefined,
//   symbol: Symbol("unique"),
// };
// let nonPrimitiveDataTypes = {
//   object: {key: "value"},
//   array: [1, 2, 3],
//   function: function () {
//     return "I am a function";
//   },
// };
// // Primitive data types are immutable and stored by value, while non-primitive data types are mutable and stored by reference.
// console.log(primitiveDataTypes);
// console.log(nonPrimitiveDataTypes);
// // Example of primitive data type
// let strPrimitive = "Hello"; // String primitive
// let numPrimitive = 42; // Number primitive
// let boolPrimitive = true; // Boolean primitive
// // Example of non-primitive data type
// let objNonPrimitive = {name: "John", age: 30}; // Object non-primitive
// let arrNonPrimitive = [1, 2, 3]; // Array non-primitive
// let funcNonPrimitive = function () {
//   return "I am a function"; // Function non-primitive
// };
// console.log(strPrimitive); // Output: 'Hello'
// console.log(numPrimitive); // Output: 42
// console.log(boolPrimitive); // Output: true
// console.log(objNonPrimitive); // Output: {name: 'John', age: 30
// console.log(arrNonPrimitive); // Output: [1, 2, 3]
// console.log(funcNonPrimitive()); // Output: 'I am a function'

// reduce mathod
// let arrry = [1, 2, 3, 4, 5];

// const sumEle = arrry.reduce((sum, arr) => sum <= arr);

// console.log(sumEle);

// Array mothods in js
let fruits = ["apple", "banana", "cherry"];
// 1. push() - Adds an element to the end of the array
fruits.push("date");
console.log(fruits); // Output: ['apple', 'banana', 'cherry', 'date']
// 2. pop() - Removes the last element from the array
let lastFruit = fruits.pop();
console.log(lastFruit); // Output: 'date'
console.log(fruits); // Output: ['apple', 'banana', 'cherry']
// 3. unshift() - Adds an element to the beginning of the array
fruits.unshift("avocado");
console.log(fruits); // Output: ['avocado', 'apple', 'banana', 'cherry']
// 4. shift() - Removes the first element from the array
let firstFruit = fruits.shift();
console.log(firstFruit); // Output: 'avocado'
console.log(fruits); // Output: ['apple', 'banana', 'cherry']
// 5. indexOf() - Returns the index of the first occurrence of an element
let index = fruits.indexOf("banana");
console.log(index); // Output: 1
// 6. slice() - Returns a shallow copy of a portion of the array
let citrus = fruits.slice(1, 3);
console.log(citrus); // Output: ['banana', 'cherry']
// 7. splice() - Adds or removes elements from the array
fruits.splice(0, 1, "blueberry");
console.log(fruits); // Output: ['blueberry', 'banana', 'cherry']
// 8. forEach() - Executes a provided function once for each array element
fruits.forEach(fruit => console.log(fruit)); // Output: 'blueberry' 'banana' 'cherry'
// 9. map() - Creates a new array with the results of calling a provided function on every element
let upperFruits = fruits.map(fruit => fruit.toUpperCase());
console.log(upperFruits); // Output: ['BLUEBERRY', 'BANANA', 'CHERRY']
// 10. filter() - Creates a new array with all elements that pass the test implemented by the provided function
let bFruits = fruits.filter(fruit => fruit.startsWith("b"));
console.log(bFruits); // Output: ['blueberry', 'banana']
// 11. reduce() - Executes a reducer function on each element of the array, resulting in a single output value
let totalLength = fruits.reduce((total, fruit) => total + fruit.length, 0);
console.log(totalLength); // Output: 19
