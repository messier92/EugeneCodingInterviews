const myPromise = new Promise((resolve, reject) => {
    const success = true;

    if (success) {
        resolve("Promise resolved successfully!");
    } else {
        reject("Promise rejected.");
    }
})

myPromise.then((value) => {
    console.log(value);
}).catch((error) => {
    console.error(error);
}).finally(() => {
    console.log("Promise has been settled (either resolved or rejected).");
});