// O(n) time - every element processed once 
// O(n) space - stores all element + recursion overhead
function flatten(arr) {
    let result = []

    // make sure to declare "let i" otherwise it treats as a global
    for (let i = 0; i < arr.length; i++) {
        if (Array.isArray(arr[i])){
            result = result.concat(flatten(arr[i]));
        } else 
        {
            result.push(arr[i])
        }
    }

    return result;
}

console.log(flatten([1, [2, [3, 4], 5], 6]));

function flattenIterative(arr) {
    const result = [];
    // 1. Initialize a stack with the contents of the array
    const stack = [...arr];

    while (stack.length > 0) {
        // 2. Pop the last item from the stack (Efficient O(1) operation)
        const current = stack.pop();

        if (Array.isArray(current)) {
            // 3. If it's an array, spread its contents back onto the stack
            // Example: if current is [2, 3], stack becomes [..., 2, 3]
            stack.push(...current);
        } else {
            // 4. If it's not an array, add it to our result
            result.push(current);
        }
    }

    // 5. Since we popped from the end (Right-to-Left), the result is backwards.
    // Reverse it once at the end to correct the order.
    return result.reverse();
}

// Test Case
const nested = [1, [2, [3, 4], 5], 6];
console.log(flattenIterative(nested)); 
// Output: [1, 2, 3, 4, 5, 6]