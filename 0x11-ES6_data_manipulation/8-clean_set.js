function cleanSet(set, startString) {
  let finalString = '';
  if (!startString || startString.length === 0) return finalString;
  set.forEach((el) => {
    if (el && el.startsWith(startString)) finalString += `${el.slice(startString.length)}-`;
  });
  return finalString.slice(0, finalString.length - 1);
}

export default cleanSet;
