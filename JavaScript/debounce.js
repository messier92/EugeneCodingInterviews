export default function debounce(func, wait) {
  let timeoutId;

  return function (...args) {
    clearTimeout(timeoutId);

    timeoutId = setTimeout(() => {
      // Use .apply(this) to ensure the context remains correct
      // args is the arguments passed to the debounced function (e.g. input)
      func.apply(this, args);
      // wait is the delay in millisecondsc
    }, wait); 
  };
}