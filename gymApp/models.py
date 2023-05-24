from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)
    
    # def __int__(self):
    #     return self.id or 0

class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.id or 0


class Trainers(models.Model):
    id = models.AutoField(primary_key=True)
    trainer_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cnic = models.IntegerField()
    phone_no = models.IntegerField()
    email_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)




class Members(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.CharField(max_length=100)
    package_id = models.ForeignKey(Packages, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    cnic = models.IntegerField()
    phone_no = models.IntegerField()
    email_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)


class TrainerPackages(models.Model):
    id = models.AutoField(primary_key=True)
    trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)


class TrainerMembers(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    trainer_id = models.ForeignKey(Trainers, on_delete=models.CASCADE, null=True)
    trainer_package_id = models.ForeignKey(TrainerPackages, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)


class Material(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, default = '')
    weight = models.IntegerField(default = 0)
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)


class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)


class Invoices(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, null=True)
    invoice_category = models.CharField(max_length=200)
    amount = models.IntegerField()
    status = models.CharField(max_length=20)
    datetime = models.DateField(auto_now=True)
    operator = models.CharField(max_length=100)