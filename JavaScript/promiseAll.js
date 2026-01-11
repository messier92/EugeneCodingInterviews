/**
 * @param {Array} iterable
 * @return {Promise<Array>}
 */
export default function promiseAll(iterable) {
return new Promise((resolve, reject) => {
    const results = [];
    let completedCount = 0;

    // Handle the edge case of an empty array immediately
    if (iterable.length === 0) {
      resolve(results);
      return;
    }

    iterable.forEach((item, index) => {
      // We wrap item in Promise.resolve() in case it's a primitive value (like a number)
      Promise.resolve(item)
        .then((value) => {
          // Store result at the specific index to maintain order
          results[index] = value;
          completedCount++;

          // Once all items are processed, resolve the main promise
          if (completedCount === iterable.length) {
            resolve(results);
          }
        })
        .catch((error) => {
          // If any single promise rejects, the whole thing rejects immediately
          reject(error);
        });
    });
  });
}