/**
 * @param {*} valueA
 * @param {*} valueB
 * @return {boolean}
 */
export default function deepEqual(valueA, valueB) {
  // 1. Handle primitives and identical references
  if (valueA === valueB) return true;

  // 2. Handle nulls and non-object types
  // (null is an 'object' in JS, so we check it explicitly)
  if (
    valueA === null ||
    valueB === null ||
    typeof valueA !== "object" ||
    typeof valueB !== "object"
  ) {
    return false;
  }

  // 3. Handle Array vs Object mismatch
  if (Array.isArray(valueA) !== Array.isArray(valueB)) {
    return false;
  }

  // 4. Check keys length to save time
  const keys1 = Object.keys(valueA);
  const keys2 = Object.keys(valueB);

  if (keys1.length !== keys2.length) {
    return false;
  }

  // 5. Recursive check for every key
  for (let key of keys1) {
    // Check if the key exists in both and then recurse
    if (!keys2.includes(key) || !deepEqual(valueA[key], valueB[key])) {
      return false;
    }
  }

  return true;
}
