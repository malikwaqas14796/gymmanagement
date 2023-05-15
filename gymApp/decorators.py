from django.views.decorators.csrf import csrf_exempt, csrf_protect
from gymApp import views

#decorator to check if the user is logged in
@csrf_exempt
def check_login(given_function):

    def check_session(request):

        if 'USERNAME' not in request.session:
            return views.login(request)
        
        else:
            return given_function(request)
    
    return check_session