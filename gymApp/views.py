import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from gymApp import decorators as decorator

from gymApp.AuthModel import AuthModel
from gymApp.AdminModel import AdminModel
from gymApp.TrainerModel import TrainerModel
from gymApp.MemberModel import MemberModel
from gymApp.PackageModel import PackageModel
from gymApp.MaterialModel import MaterialModel
from gymApp.InventoryModel import InventoryModel


@csrf_exempt
def login(request):
    # return HttpResponse('12121')
    return render(request, "login.html")


@csrf_exempt
# @decorator.check_login
def register_user(request):
    return render(request, "register_user.html")


@csrf_exempt
def perform_login_ajax(request):
    
    empId = request.POST.get('userName')
    password = request.POST.get('password')

    if empId == 'waqas.rafique' and password == '123456':
        authModelObj = AuthModel()
        # return HttpResponse(authModelObj)
        #response = authModelObj.fetch_employee(empId) 
        make_session(request, empId)
        return HttpResponse('success')
    
    else:
        return HttpResponse('error')


@csrf_exempt
def perform_logout_ajax(request):
    
    destroy_session(request)
    return HttpResponse('true')


@csrf_exempt
def make_session(request, userName):

    request.session['USERNAME'] = userName

    
@csrf_exempt
def destroy_session(request):
   
    del request.session['USERNAME']

@decorator.check_login
@csrf_exempt
def dashboard(request):
    return render(request, "admin_templates/dashboard.html")




################################## ADMIN SECTION STARTS HERE #################################
@decorator.check_login
@csrf_exempt
def createadmin(request):
    return render(request, "admin_templates/createadmin.html")


@decorator.check_login
@csrf_exempt
def create_admin_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        admin_class_obj = AdminModel();
        result = admin_class_obj.create_admin_ajax(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')

@decorator.check_login
@csrf_exempt
def edit_admin_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        admin_class_obj = AdminModel();
        result = admin_class_obj.edit_admin_ajax(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
        

@decorator.check_login
@csrf_exempt
def get_admin_ajax(request):

    dataArray = []
    admins = AdminModel.get_admins()

    for i in range(0, len(admins)):
        admin_id = admins[i].admin_id
        # dataArray.append([employees[i]['first_name'],employees[i]['last_name'],employees[i]['empid'],employees[i]['office_city'],employees[i]['dept_desig_id'],1,1,employees[i]['status'],employees[i]['datetime'],employees[i]['operator'],
        # '<a onclick = "showOrderModal('+str(employee_id)+')"; class="btn btn-app bg-success"><span class="badge bg-teal"></span><i class="fas fa-inbox"></i>Order</a>'
        # ])

        dataArray.append([admins[i].name, admins[i].admin_id,admins[i].city,admins[i].password,admins[i].datetime,admins[i].operator,
        "<div><a onclick = 'edit_admin(\""+str(admin_id)+"\",\""+str(admins[i].name)+"\",\""+str(admins[i].city)+"\",\""+str(admins[i].password)+"\")'; class='btn btn-sm btn-primary'><span class='badge bg-teal'></span><i class='fas fa-edit'></i></a>&nbsp;<a onclick = 'delete_admin_ajax(\""+str(admin_id)+"\")' class='btn btn-sm btn-danger'><span class='badge bg-teal'></span><i class='fas fa-trash'></i></a></div>"
        ])

    return JsonResponse({'data': dataArray})



@decorator.check_login
@csrf_exempt
def delete_admin_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        admin_class_obj = AdminModel();
        result = admin_class_obj.delete_admin(data, operator)
        
        if result == '0':
            return HttpResponse('Error.')
        else:
            return HttpResponse('true')

################################## ADMIN SECTION ENDS HERE #################################






################################## TRAINER SECTION STARTS HERE #################################


@decorator.check_login
@csrf_exempt
def createtrainer(request):
    return render(request, "trainer_templates/createtrainer.html")

@csrf_exempt
def create_trainer_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        trainer_class_obj = TrainerModel();
        result = trainer_class_obj.create_trainer(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')


@decorator.check_login
@csrf_exempt
def edit_trainer_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        trainer_class_obj = TrainerModel();
        result = trainer_class_obj.edit_trainer(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
        


@decorator.check_login
@csrf_exempt
def get_trainer_ajax(request):

    dataArray = []
    trainers = TrainerModel.get_trainers()

    for i in range(0, len(trainers)):
        trainer_id = trainers[i].trainer_id

        dataArray.append([trainers[i].name, trainers[i].trainer_id,trainers[i].city,trainers[i].phone_no,trainers[i].email_address,trainers[i].cnic,trainers[i].password,trainers[i].datetime,trainers[i].operator,
        "<div><a onclick = 'edit_trainer(\""+str(trainer_id)+"\",\""+str(trainers[i].name)+"\",\""+str(trainers[i].city)+"\",\""+str(trainers[i].phone_no)+"\",\""+str(trainers[i].email_address)+"\",\""+str(trainers[i].cnic)+"\",\""+str(trainers[i].password)+"\")'; class='btn btn-sm btn-primary'><span class='badge bg-teal'></span><i class='fas fa-edit'></i></a>&nbsp;<a onclick = 'delete_trainer_ajax(\""+str(trainer_id)+"\")' class='btn btn-sm btn-danger'><span class='badge bg-teal'></span><i class='fas fa-trash'></i></a></div>"
        ])

    return JsonResponse({'data': dataArray})




@decorator.check_login
@csrf_exempt
def delete_trainer_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        trainer_class_obj = TrainerModel();
        result = trainer_class_obj.delete_trainer(data, operator)
        
        if result == '0':
            return HttpResponse('Error.')
        else:
            return HttpResponse('true')


################################## TRAINER SECTION ENDS HERE #################################







################################## MEMBER SECTION STARTS HERE #################################


@decorator.check_login
@csrf_exempt
def createmember(request):
    return render(request, "member_templates/createmember.html")

@csrf_exempt
def create_member_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        member_class_obj = MemberModel();
        result = member_class_obj.create_member(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')


@decorator.check_login
@csrf_exempt
def edit_member_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        member_class_obj = MemberModel();
        result = member_class_obj.edit_member(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
        

@decorator.check_login
@csrf_exempt
def get_member_ajax(request):

    dataArray = []
    members = MemberModel.get_members()

    for i in range(0, len(members)):
        member_id = members[i].member_id

        dataArray.append([members[i].name, members[i].member_id,members[i].city,members[i].phone_no,members[i].email_address,members[i].cnic,members[i].password,members[i].datetime,members[i].operator,
        "<div><a onclick = 'edit_member(\""+str(member_id)+"\",\""+str(members[i].name)+"\",\""+str(members[i].city)+"\",\""+str(members[i].phone_no)+"\",\""+str(members[i].email_address)+"\",\""+str(members[i].cnic)+"\",\""+str(members[i].password)+"\")'; class='btn btn-sm btn-primary'><span class='badge bg-teal'></span><i class='fas fa-edit'></i></a>&nbsp;<a onclick = 'delete_member_ajax(\""+str(member_id)+"\")' class='btn btn-sm btn-danger'><span class='badge bg-teal'></span><i class='fas fa-trash'></i></a></div>"
        ])

    return JsonResponse({'data': dataArray})




@decorator.check_login
@csrf_exempt
def delete_member_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        member_class_obj = MemberModel();
        result = member_class_obj.delete_member(data, operator)
        
        if result == '0':
            return HttpResponse('Error.')
        else:
            return HttpResponse('true')



@decorator.check_login
@csrf_exempt
def get_members_values_ajax(request):

    members = MemberModel.get_members()

    dataArray = []
    for i in range(0, len(members)):
        dataArray.append([members[i].member_id])
    return JsonResponse({"data":dataArray})

################################## MEMBER SECTION ENDS HERE #################################






################################## PACKAGE SECTION STARTS HERE #################################


@decorator.check_login
@csrf_exempt
def createpackage(request):
    return render(request, "package_templates/createpackage.html")



@decorator.check_login
@csrf_exempt
def assignpackage(request):
    return render(request, "package_templates/assignpackage.html")


@decorator.check_login
@csrf_exempt
def create_package_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        package_class_obj = PackageModel();
        result = package_class_obj.create_package(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')


@decorator.check_login
@csrf_exempt
def edit_package_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        package_class_obj = PackageModel();
        result = package_class_obj.edit_package(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
        

@decorator.check_login
@csrf_exempt
def get_package_ajax(request):

    dataArray = []
    packages = PackageModel.get_packages()

    for i in range(0, len(packages)):
        package_id = packages[i].id

        dataArray.append([packages[i].name, packages[i].amount,packages[i].datetime,packages[i].operator,
        "<div><a onclick = 'edit_package(\""+str(package_id)+"\",\""+str(packages[i].name)+"\",\""+str(packages[i].amount)+"\")'; class='btn btn-sm btn-primary'><span class='badge bg-teal'></span><i class='fas fa-edit'></i></a>&nbsp;<a onclick = 'delete_package_ajax(\""+str(package_id)+"\")' class='btn btn-sm btn-danger'><span class='badge bg-teal'></span><i class='fas fa-trash'></i></a></div>"
        ])

    return JsonResponse({'data': dataArray})




@decorator.check_login
@csrf_exempt
def delete_package_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        package_class_obj = PackageModel();
        result = package_class_obj.delete_package(data, operator)
        
        if result == '0':
            return HttpResponse('Error.')
        else:
            return HttpResponse('true')



@decorator.check_login
@csrf_exempt
def get_package_values_ajax(request):

    packages = PackageModel.get_packages()

    dataArray = []
    for i in range(0, len(packages)):
        dataArray.append([packages[i].id, packages[i].name])
    return JsonResponse({"data":dataArray})



@decorator.check_login
@csrf_exempt
def assign_package_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        package_class_obj = PackageModel();
        result = package_class_obj.create_package(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
################################## PACKAGE SECTION ENDS HERE #################################




################################## MATERIAL SECTION STARTS HERE #################################


@decorator.check_login
@csrf_exempt
def creatematerial(request):
    return render(request, "material_templates/creatematerial.html")



@decorator.check_login
@csrf_exempt
def assignmaterial(request):
    return render(request, "material_templates/assignmaterial.html")



@decorator.check_login
@csrf_exempt
def create_material_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        material_class_obj = MaterialModel();
        result = material_class_obj.create_material(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')


@decorator.check_login
@csrf_exempt
def edit_material_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        material_class_obj = MaterialModel();
        result = material_class_obj.edit_material(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
        


@decorator.check_login
@csrf_exempt
def get_material_ajax(request):

    dataArray = []
    materials = MaterialModel.get_materials()

    for i in range(0, len(materials)):
        material_id = materials[i].id

        dataArray.append([materials[i].name, materials[i].category,materials[i].weight,materials[i].datetime,materials[i].operator,
        "<div><a onclick = 'edit_material(\""+str(material_id)+"\",\""+str(materials[i].name)+"\",\""+str(materials[i].category)+"\",\""+str(materials[i].weight)+"\")'; class='btn btn-sm btn-primary'><span class='badge bg-teal'></span><i class='fas fa-edit'></i></a>&nbsp;<a onclick = 'delete_material_ajax(\""+str(material_id)+"\")' class='btn btn-sm btn-danger'><span class='badge bg-teal'></span><i class='fas fa-trash'></i></a></div>"
        ])

    return JsonResponse({'data': dataArray})




@decorator.check_login
@csrf_exempt
def delete_material_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        material_class_obj = MaterialModel();
        result = material_class_obj.delete_material(data, operator)
        
        if result == '0':
            return HttpResponse('Error.')
        else:
            return HttpResponse('true')


@decorator.check_login
@csrf_exempt
def get_material_values_ajax(request):

    materials = MaterialModel.get_materials()

    dataArray = []
    for i in range(0, len(materials)):
        dataArray.append([materials[i].id, materials[i].name])
    return JsonResponse({"data":dataArray})



@decorator.check_login
@csrf_exempt
def assign_material_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        material_class_obj = MaterialModel();
        result = material_class_obj.create_material(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
################################## MATERIAL SECTION ENDS HERE #################################




################################## INVENTORY SECTION STARTS HERE #################################


@decorator.check_login
@csrf_exempt
def inventory(request):
    return render(request, "inventory_templates/inventory.html")



@decorator.check_login
@csrf_exempt
def add_inventory_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        inventory_class_obj = InventoryModel();
        result = inventory_class_obj.add_inventory(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')



@decorator.check_login
@csrf_exempt
def edit_inventory_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        inventory_class_obj = InventoryModel();
        result = inventory_class_obj.edit_inventory(data, operator)

        if result == '0':
            return HttpResponse('Already Exists.')
        else:
            return HttpResponse('true')
        



@decorator.check_login
@csrf_exempt
def get_inventory_ajax(request):

    dataArray = []
    inventory = InventoryModel.get_inventory()

    for i in range(0, len(inventory)):
        inventory_id = inventory[i].id

        dataArray.append([inventory[i].material_id.name, inventory[i].material_id.weight, inventory[i].material_id.category, inventory[i].quantity,inventory[i].datetime,inventory[i].operator,
        "<div><a onclick = 'edit_inventory(\""+str(inventory_id)+"\",\""+str(inventory[i].material_id.id)+"\",\""+str(inventory[i].quantity)+"\")'; class='btn btn-sm btn-primary'><span class='badge bg-teal'></span><i class='fas fa-edit'></i></a>&nbsp;<a onclick = 'delete_inventory_ajax(\""+str(inventory_id)+"\")' class='btn btn-sm btn-danger'><span class='badge bg-teal'></span><i class='fas fa-trash'></i></a></div>"
        ])

    return JsonResponse({'data': dataArray})




@decorator.check_login
@csrf_exempt
def delete_inventory_ajax(request):
    if request.method == 'POST':
        data= json.loads(request.POST.get('payload'))
        operator = request.session['USERNAME']

        inventory_class_obj = InventoryModel();
        result = inventory_class_obj.delete_inventory(data, operator)
        
        if result == '0':
            return HttpResponse('Error.')
        else:
            return HttpResponse('true')


################################## INVENTORY SECTION ENDS HERE #################################