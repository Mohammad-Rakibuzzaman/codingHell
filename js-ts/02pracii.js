// b) Create variables to store the prices of three items. 
// Calculate and store the total cost in a new variable. 
// Apply a discount percentage stored in another variable.

let bananaPrice = 10
let watermelonPrice = 20
let peanutPrice = 5

let totalPrice = bananaPrice + watermelonPrice + peanutPrice

let discountPrice = 30

let totalDiscount = (totalPrice * discountPrice) / 100
let finalTotal = totalPrice - totalDiscount

console.log("The total price of the fruite is: " + totalPrice + "$, Also there is a " + discountPrice +"% of discount if he could use voucher. So after discount total cost is: " + finalTotal.toFixed(2) + "$.")