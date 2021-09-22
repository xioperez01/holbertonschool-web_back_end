function groceriesList() {
  const array = [
    ['Apples', 10],
    ['Tomatoes', 10],
    ['Pasta', 1],
    ['Rice', 1],
    ['Banana', 5],
  ];
  const arrayMap = new Map();
  for (const item of array) arrayMap.set(item[0], item[1]);
  return arrayMap;
}

export default groceriesList;
