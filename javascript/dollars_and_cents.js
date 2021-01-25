/* The company you work for has just been awarded a contract to build a payment gateway. In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.

39.99 becomes $39.99

The rest of your team will make sure that the argument is sanitized before being passed to your function although you will need to account for adding trailing zeros if they are missing (though you won't have to worry about a dangling period).

Examples:

3 needs to become $3.00

3.1 needs to become $3.10 */

function formatMoney(amount){
    let result = Number(amount).toFixed(2)
    result = `$${result}`
    return result
}

console.log(formatMoney(3), formatMoney(3.5444), formatMoney(12.44))