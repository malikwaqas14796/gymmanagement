from gymApp.models import *

class TrainerModel():
        
    def create_trainer(self, data, operator):
        
        check_trainer_entry = Trainers.objects.filter(trainer_id = data['id'], status = 'active').values()

        # return(len(check_department_entry))
        if len(check_trainer_entry) > 0:
            return '0'


        result = Trainers(name = data['name'],  trainer_id = data['id'], city = data['city'], phone_no = data['phone_no'], email_address = data['email_address'], cnic = data['cnic'], password = data['password'], status = "active", operator = operator)
        result.save()
        return result
    
    def get_trainers():
        
        # EMPLOYEE.objects.filter(empid='mwaqas96').delete()
        # return 12121
        # employees = EMPLOYEE.objects.values()
        trainers = Trainers.objects.filter(status = 'active')

        return trainers
    
    

    def edit_trainer(self, data, operator):

        result = Trainers.objects.filter(trainer_id = data['id']).update(name = data['name'],  trainer_id = data['id'], city = data['city'], phone_no = data['phone_no'], email_address = data['email_address'], cnic = data['cnic'], password = data['password'], operator = operator)

        return result
    
    
    def delete_trainer(self, data, operator):

        result = Trainers.objects.filter(trainer_id = data['id']).update(status = 'del', operator = operator)
        
        if result:
            return '1'
        else:
            return '0'
    

    def get_trainer_packages():
        trainer_packages = TrainerPackages.objects.filter(status = 'active')

        return trainer_packages

    def create_trainer_member(self, data, operator):
        
        check_entry = TrainerMembers.objects.filter(member_id = data['member_id'], trainer_id = data['trainer_id'], status = 'active').values()
        if len(check_entry) > 0:
            return '0'

        member_instance = Members.objects.get(id = data['member_id'], status = 'active')
        trainer_instance = Trainers.objects.get(id = data['trainer_id'], status = 'active')
        trainer_package_instance = TrainerPackages.objects.get(id = data['package_id'], status = 'active')

        result = TrainerMembers(trainer_id = trainer_instance,  member_id = member_instance, trainer_package_id = trainer_package_instance, status = "active", operator = operator)
        result.save()
        return result

    
    def get_trainer_members():
        trainer_members = TrainerMembers.objects.filter(status = 'active').select_related('member_id', 'trainer_id', 'trainer_package_id')
        return trainer_members

    
    def edit_trainer_member(self, data, operator):
        
        result = TrainerMembers.objects.filter(id = data['id']).update(trainer_id = data['trainer_id'],  member_id = data['member_id'], trainer_package_id = data['package_id'], operator = operator)

        return result

    
    def delete_trainer_member(self, data, operator):

        result = TrainerMembers.objects.filter(id = data['id']).update(status = 'del', operator = operator)
        
        if result:
            return '1'
        else:
            return '0'