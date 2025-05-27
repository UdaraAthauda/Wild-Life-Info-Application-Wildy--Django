from .models import VenomType

def categories_processor(request):
    categories = VenomType.objects.all()
    return {'categories': categories}
