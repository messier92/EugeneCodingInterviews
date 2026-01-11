/**
 * @param {...(any|Object|Array<any|Object|Array>)} args
 * @return {string}
 */
export default function classNames(...args) {
  const classes = [];

  args.forEach((arg) => {
    // 1. Skip "falsy" values (null, undefined, false, etc.)
    if (!arg) return;

    const argType = typeof arg;

    // 2. Handle Strings and Numbers
    if (argType === 'string' || argType === 'number') {
      classes.push(arg);
    } 
    // 3. Handle Arrays (recursively)
    else if (Array.isArray(arg)) {
      const inner = classNames(...arg);
      if (inner) classes.push(inner);
    } 
    // 4. Handle Objects
    else if (argType === 'object') {
      // Loop through keys and add if the value is truthy
      for (const key in arg) {
        if (Object.prototype.hasOwnProperty.call(arg, key) && arg[key]) {
          classes.push(key);
        }
      }
    }
  });

  return classes.join(' ');
}