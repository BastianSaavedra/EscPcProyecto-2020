from django.contrib import admin

# Register your models here.

from . models import PlacasMadre, Procesadore, Gpu, Ram, Almacenamiento, FuentesPoder, Gabinete, Monitore, Contacto

admin.site.register(PlacasMadre)
admin.site.register(Procesadore)
admin.site.register(Gpu)
admin.site.register(Ram)
admin.site.register(Almacenamiento)
admin.site.register(FuentesPoder)
admin.site.register(Gabinete)
admin.site.register(Monitore)
admin.site.register(Contacto)
