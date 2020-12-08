const fs = require('fs')
const file = fs.readFileSync('inputs/01.txt').toString().split('\n')

let a, b, c = 0

console.log('Part 1')
for (let i = 0; i < file.length; i++){
    for (let j = 0; j < file.length; j++){
        if (parseInt(file[i]) + parseInt(file[j]) == 2020 && i != j) {
            a = parseInt(file[i])
            b = parseInt(file[j])
            break
        }
    }
}
console.log(a * b)

console.log('Part 2')
for (let i = 0; i < file.length; i++){
    for (let j = 0; j < file.length; j++){
        for (let k = 0; k < file.length; k++){
            if (parseInt(file[i]) + parseInt(file[j]) + parseInt(file[k]) == 2020 && i != j != k) {
                a = parseInt(file[i])
                b = parseInt(file[j])
                c = parseInt(file[k])
                break
            }
        }
    }
}
console.log(a * b * c)
