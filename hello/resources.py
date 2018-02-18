from import_export import resources
from .models import Destinations

class DestinationsResource(resources.ModelResource):
    class Meta:
        model = Destinations
        fields = ('title', 'price', 'photoURL', 'description', 'city_id')

