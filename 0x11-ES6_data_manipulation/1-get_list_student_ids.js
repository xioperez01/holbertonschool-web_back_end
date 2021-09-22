function getListStudentIds(arr) {
  if (!Array.isArray(arr)) return [];
  return arr.map((e) => e.id);
}

export default getListStudentIds;
