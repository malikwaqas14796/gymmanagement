from gymApp.models import *

class MemberModel():
        
    def create_member(self, data, operator):
        
        check_member_entry = Members.objects.filter(member_id = data['id'], status = 'active').values()

        # return(len(check_department_entry))
        if len(check_member_entry) > 0:
            return '0'

        package_instance = Packages.objects.get(id = data['package'], status = 'active')

        result = Members(name = data['name'],  member_id = data['id'], city = data['city'], phone_no = data['phone_no'], email_address = data['email_address'], cnic = data['cnic'], password = data['password'], package_id = package_instance, status = "active", operator = operator)
        result.save()
        return result
    
    def get_members():
        
        # EMPLOYEE.objects.filter(empid='mwaqas96').delete()
        # return 12121
        # employees = EMPLOYEE.objects.values()
        # members = Members.objects.filter(status = 'active')

        members = Members.objects.filter(status = 'active').select_related('package_id')

        return members
    
    

    def edit_member(self, data, operator):

        result = Members.objects.filter(member_id = data['id']).update(name = data['name'],  member_id = data['id'], city = data['city'], phone_no = data['phone_no'], email_address = data['email_address'], cnic = data['cnic'], password = data['password'], package_id = data['package'], operator = operator)

        return result
    
    
    def delete_member(self, data, operator):

        result = Members.objects.filter(member_id = data['id']).update(status = 'del', operator = operator)
        
        if result:
            return '1'
        else:
            return '0'