/**
 * @callback func
 * @param {number} wait
 * @return {Function}
 */
export default function throttle(func, wait) {
  let isLocked = false;

  return function (...args) {
    // If the "lock" is active, exit early
    if (isLocked) return;

    // 1. Invoke the callback immediately
    func.apply(this, args);

    // 2. Activate the lock
    isLocked = true;

    // 3. Set a timer to deactivate the lock after X milliseconds
    setTimeout(() => {
      isLocked = false;
    }, wait);
  };  
}
