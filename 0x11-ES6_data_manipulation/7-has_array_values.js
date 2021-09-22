function hasValuesFromArray(set, arr) {
  return arr.every((e) => set.has(e));
}

export default hasValuesFromArray;
