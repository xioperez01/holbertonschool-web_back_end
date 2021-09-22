function getStudentsByLocation(list, city, newGrade) {
  return list
    .filter((item) => item.location === city)
    .map((student) => {
      const gradeItem = newGrade
        .filter((item) => item.studentId === student.id)
        .map((x) => x.grade)[0];
      const grade = gradeItem || 'N/A';
      return { ...student, grade };
    });
}

export default getStudentsByLocation;
