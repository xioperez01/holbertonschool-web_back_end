function getStudentIdsSum(list) {
  return list.map((i) => i.id).reduce((a, b) => a + b, 0);
}

export default getStudentIdsSum;
