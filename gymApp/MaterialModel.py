from gymApp.models import *

class MaterialModel():
        
    def create_material(self, data, operator):
        
        check_material_entry = Material.objects.filter(name = data['name'], weight = data['weight'], status = 'active').values()

        # return(len(check_department_entry))
        if len(check_material_entry) > 0:
            return '0'


        result = Material(name = data['name'],  category = data['category'], weight = data['weight'], status = "active", operator = operator)
        result.save()
        return result
    
    def get_materials():
        
        # EMPLOYEE.objects.filter(empid='mwaqas96').delete()
        # return 12121
        # employees = EMPLOYEE.objects.values()
        materials = Material.objects.filter(status = 'active')

        return materials
    
    

    def edit_material(self, data, operator):

        result = Material.objects.filter(id = data['id']).update(name = data['name'],  category = data['category'], weight = data['weight'], operator = operator)

        return result
    
    
    def delete_material(self, data, operator):

        result = Material.objects.filter(id = data['id']).update(status = 'del', operator = operator)
    
        if result:
            return '1'
        else:
            return '0'