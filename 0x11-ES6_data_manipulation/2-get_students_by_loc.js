function getStudentsByLocation(list, city) {
  return list.filter((s) => s.location === city);
}

export default getStudentsByLocation;
