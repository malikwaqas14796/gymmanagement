from django.contrib import admin
from django.urls import path 
from gymApp import views

urlpatterns = [
    #Authentication Views
    path('login', views.login, name = 'login'),
    path('registeruser', views.register_user, name = 'register_user'),
    
    
    #Admin views
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('createadmin', views.createadmin, name = 'createadmin'),

    #Trainer Views
    path('createtrainer', views.createtrainer, name = 'createtrainer'),


    #Member Views
    path('createmember', views.createmember, name = 'createmember'),



    #Package Views
    path('createpackage', views.createpackage, name = 'createpackage'),
    path('assignpackage', views.assignpackage, name = 'assignpackage'),


    #Material Views
    path('creatematerial', views.creatematerial, name = 'creatematerial'),
    path('inventory', views.inventory, name = 'inventory'),


    #Authentication ajax calls
    path('perform_login_ajax', views.perform_login_ajax, name = 'perform_login_ajax'),
    path('perform_logout_ajax', views.perform_logout_ajax, name = 'perform_logout_ajax'),



    #admin ajax calls
    path('create_admin_ajax', views.create_admin_ajax, name = 'create_admin_ajax'),
    path('get_admin_ajax', views.get_admin_ajax, name = 'get_admin_ajax'),
    path('edit_admin_ajax', views.edit_admin_ajax, name = 'edit_admin_ajax'),
    path('delete_admin_ajax', views.delete_admin_ajax, name = 'delete_admin_ajax'),







    #trainer ajax calls
    path('create_trainer_ajax', views.create_trainer_ajax, name = 'create_trainer_ajax'),
    path('get_trainer_ajax', views.get_trainer_ajax, name = 'get_trainer_ajax'),
    path('edit_trainer_ajax', views.edit_trainer_ajax, name = 'edit_trainer_ajax'),
    path('delete_trainer_ajax', views.delete_trainer_ajax, name = 'delete_trainer_ajax'),




    #member ajax calls
    path('create_member_ajax', views.create_member_ajax, name = 'create_member_ajax'),
    path('get_member_ajax', views.get_member_ajax, name = 'get_member_ajax'),
    path('edit_member_ajax', views.edit_member_ajax, name = 'edit_member_ajax'),
    path('delete_member_ajax', views.delete_member_ajax, name = 'delete_member_ajax'),
    path('get_members_values_ajax', views.get_members_values_ajax, name = 'get_members_values_ajax'),



    #package ajax calls
    path('create_package_ajax', views.create_package_ajax, name = 'create_package_ajax'),
    path('get_package_ajax', views.get_package_ajax, name = 'get_package_ajax'),
    path('edit_package_ajax', views.edit_package_ajax, name = 'edit_package_ajax'),
    path('delete_package_ajax', views.delete_package_ajax, name = 'delete_package_ajax'),
    path('get_package_values_ajax', views.get_package_values_ajax, name = 'get_package_values_ajax'),
    path('assign_package_ajax', views.assign_package_ajax, name = 'assign_package_ajax'),




    #material ajax calls
    path('create_material_ajax', views.create_material_ajax, name = 'create_material_ajax'),
    path('get_material_ajax', views.get_material_ajax, name = 'get_material_ajax'),
    path('edit_material_ajax', views.edit_material_ajax, name = 'edit_material_ajax'),
    path('delete_material_ajax', views.delete_material_ajax, name = 'delete_material_ajax'),
    path('get_material_values_ajax', views.get_material_values_ajax, name = 'get_material_values_ajax'),
    path('assign_material_ajax', views.assign_material_ajax, name = 'assign_material_ajax'),
    # path('get_designations_ajax', views.get_designations_ajax, name = 'get_designations_ajax'),



    #inventory ajax calls
    path('add_inventory_ajax', views.add_inventory_ajax, name = 'add_inventory_ajax'),
    path('get_inventory_ajax', views.get_inventory_ajax, name = 'get_inventory_ajax'),
    path('edit_inventory_ajax', views.edit_inventory_ajax, name = 'edit_inventory_ajax'),
    path('delete_inventory_ajax', views.delete_inventory_ajax, name = 'delete_inventory_ajax'),
]