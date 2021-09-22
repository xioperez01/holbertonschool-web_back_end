function hasValuesFromArray(set, arr) {
  return arr.forEach((e) => set.has(e));
}

export default hasValuesFromArray;
