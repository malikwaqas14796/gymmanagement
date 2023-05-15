from gymApp.models import *

class AdminModel():
        
    def create_admin_ajax(self, data, operator):
        
        check_admin_entry = Admin.objects.filter(admin_id = data['admin_id'], status = 'active').values()

        # return(len(check_department_entry))
        if len(check_admin_entry) > 0:
            return '0'


        result = Admin(name = data['admin_name'],  admin_id = data['admin_id'], city = data['city'], password = data['password'], status = "active", operator = operator)
        result.save()
        return result
    
    def get_admins():
        
        # EMPLOYEE.objects.filter(empid='mwaqas96').delete()
        # return 12121
        # employees = EMPLOYEE.objects.values()
        admins = Admin.objects.filter(status = 'active')

        return admins
    
    

    def edit_admin_ajax(self, data, operator):

        result = Admin.objects.filter(admin_id=data['admin_id']).update(name = data['admin_name'],  admin_id = data['admin_id'], city = data['city'], password = data['password'], operator = operator)

        return result
    

    def delete_admin(self, data, operator):

        result = Admin.objects.filter(admin_id = data['id']).update(status = 'del', operator = operator)
        
        if result:
            return '1'
        else:
            return '0'