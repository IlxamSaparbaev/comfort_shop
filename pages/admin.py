from django.contrib import admin
from .models import Product
from .models import Transport
from .models import Furniture
from .models import Cloth
from .models import Sport

admin.site.register(Product)
admin.site.register(Transport)
admin.site.register(Furniture)
admin.site.register(Cloth)
admin.site.register(Sport)