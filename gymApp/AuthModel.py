from gymApp.models import *

class AuthModel():
        
    def create_employee_ajax(self, data, operator):
        
        check_employee_entry = EMPLOYEE.objects.filter(empid = data['empid']).values()

        # return(len(check_department_entry))
        if len(check_employee_entry) > 0:
            return '0'
        
        department_id = DEPARTMENTDESIGNATION.objects.get(id = data['dept_desig_id'])

        result = EMPLOYEE(first_name = data['first_name'], last_name = data['last_name'], empid = data['empid'], office_city = data['office_city'], dept_desig_id = department_id, status = "active", operator = operator)
        result.save()
        return result
    
    def get_employee():
        
        # EMPLOYEE.objects.filter(empid='mwaqas96').delete()
        # return 12121
        # employees = EMPLOYEE.objects.values()
        employees = EMPLOYEE.objects.filter(status = 'active').select_related('dept_desig_id')

        return employees
    
    def create_department_ajax(self, data, operator):

        check_department_entry = DEPARTMENTDESIGNATION.objects.filter(department_name = data['department_name'], sub_department_name = data['sub_department_name'], designation_name = data['designation_name']).values()

        # return(len(check_department_entry))
        if len(check_department_entry) > 0:
            return '0'
        else:
            result = DEPARTMENTDESIGNATION(department_name = data['department_name'], sub_department_name = data['sub_department_name'], designation_name = data['designation_name'], status = "active", operator = operator)

            result.save()
            return result

    def get_departments_details():
        
        departments = DEPARTMENTDESIGNATION.objects.filter(status='active').values()
        # departments = DEPARTMENTDESIGNATION.objects.raw("SELECT * FROM profilemanagement_DEPARTMENTDESIGNATION WHERE STATUS = 'active'")

        return departments
    
    def get_departments():
        
        departments = DEPARTMENTDESIGNATION.objects.filter(status='active').values('department_name').distinct()

        return departments
    
    def get_sub_departments(data):
        
        sub_departments = DEPARTMENTDESIGNATION.objects.filter(status='active', department_name = data['department_name']).values('sub_department_name').distinct()

        return sub_departments
    
    def get_designations(data):
        
        designations = DEPARTMENTDESIGNATION.objects.filter(status='active', department_name = data['department_name'], sub_department_name = data['sub_department_name']).values('id','designation_name').distinct()

        return designations

    def delete_department(self, data, operator):

        result = DEPARTMENTDESIGNATION.objects.filter(id=data['dept_desig_id']).update(status='del', operator = operator)

        return result