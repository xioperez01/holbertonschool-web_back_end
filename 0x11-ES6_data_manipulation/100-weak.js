export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const queriesCount = weakMap.get(endpoint);
    if (queriesCount >= 4) throw Error('Endpoint load is high');
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
}
