from gymApp.models import *

class InventoryModel():
        
    def add_inventory(self, data, operator):
        
        check_inventory_entry = Inventory.objects.filter(material_id = data['material_id'], status = 'active').values()

        # return(len(check_department_entry))
        if len(check_inventory_entry) > 0:
            return '0'

        material_instance = Material.objects.get(id = data['material_id'], status = 'active')

        result = Inventory(material_id = material_instance,  quantity = data['quantity'], status = "active", operator = operator)
        result.save()
        return result
    
    def get_inventory():

        inventory = Inventory.objects.filter(status = 'active').select_related('material_id')

        return inventory
    
    

    def edit_inventory(self, data, operator):

        result = Inventory.objects.filter(id = data['id']).update(quantity = data['quantity'], operator = operator)

        return result
    
    
    def delete_inventory(self, data, operator):

        result = Inventory.objects.filter(id = data['id']).update(status = 'del', operator = operator)
    
        if result:
            return '1'
        else:
            return '0'