/* Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times. */

function findOdd(A) {
    let elementsCount = []
    for (let i=0; i < A.length; i++) {
        let count = 0
        for (num of A) {
            if (num === A[i]) {
                count++
            }
        }
        elementsCount.push(count)
    }
    for (el of elementsCount) {
        if (el % 2 === 1) {
            return A[(elementsCount.indexOf(el))]
        }
    }
}

console.log(findOdd([ 20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5 ])) 
