export default function createReportObject(employeesList) {
  return ({
    allEmployees: employeesList,
    getNumberOfDepartments: (dpt) => Object.keys(dpt).length,
  });
}
