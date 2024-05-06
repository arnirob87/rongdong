from .models import Category

def cat_menu(request):
    cat_menu = Category.objects.all()
    return {'cat_menu': cat_menu}