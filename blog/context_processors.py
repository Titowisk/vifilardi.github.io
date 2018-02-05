# Loads the model of choice throrought the whole application
from blog.models import Category

def categories(request):
    return {'categories': Category.objects.all()}