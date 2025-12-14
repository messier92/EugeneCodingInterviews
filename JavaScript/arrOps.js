// Array chunking


function chunk(array,size) {
    const res = []
    let index = 0

    while (index < array.length) {
     res.push(array.slice(index,index+size))
     index += size
    }
    return res
}

console.log(chunk([1,2,3,4,5],2))