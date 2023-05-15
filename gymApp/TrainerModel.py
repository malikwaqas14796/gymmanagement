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