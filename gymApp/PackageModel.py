from gymApp.models import *

class PackageModel():
        
    def create_package(self, data, operator):
        
        check_package_entry = Packages.objects.filter(name = data['name'], status = 'active').values()

        # return(len(check_department_entry))
        if len(check_package_entry) > 0:
            return '0'


        result = Packages(name = data['name'],  amount = data['amount'],  status = "active", operator = operator)
        result.save()
        return result
    
    def get_packages():
        
        # EMPLOYEE.objects.filter(empid='mwaqas96').delete()
        # return 12121
        # employees = EMPLOYEE.objects.values()
        packages = Packages.objects.filter(status = 'active')

        return packages
    
    

    def edit_package(self, data, operator):

        result = Packages.objects.filter(id = data['id']).update(name = data['name'],  amount = data['amount'], operator = operator)

        return result
    
    
    def delete_package(self, data, operator):

        result = Packages.objects.filter(id = data['id']).update(status = 'del', operator = operator)
        
        if result:
            return '1'
        else:
            return '0'