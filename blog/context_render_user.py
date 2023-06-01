from .models import Post



def render_user(request):
    return {
        'user': request.user
    }   
