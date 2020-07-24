from django.contrib import admin
#Do banco models importe Post que foi o objeto que eu
#criei no arquivo models.py
from .models import Post

#Registra-se o modelo dessa maneira para que ele
#fique visível na pag de administração
admin.site.register(Post)
# Register your models here.
