/*
Given: an array of different type of values (number, string, boolean). You should return an object with a separate properties for each of types presented in input. Each property should contain an array of corresponding values.

keep order of values like in input array
if type is not presented in input, no corresponding property are expected
So, for this input:

['a', 1, 2, false, 'b']
expected output is:

{
  number: [1, 2],
  string: ['a', 'b'],
  boolean: [false]
}
*/

function separateTypes(input) {
    types = ['number', 'string', 'boolean']
    obj = {number:[], string:[], boolean:[]}
    input.forEach(el => {
        switch(typeof el){
            case 'number':
                obj.number.push(el)
                break
            case 'string':
                obj.string.push(el)
                break
            case 'boolean':
                obj.boolean.push(el)
                break
        }
    })

    types.forEach( (type) => {
        if (obj[type].length === 0) {
            delete obj[type]
        }
    })

    return obj
}


console.log(separateTypes(['a', 1, 2, false, 'b']))
console.log(separateTypes(['a', 1, 2 ]))
