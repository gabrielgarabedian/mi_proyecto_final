from django.db import models
from traitlets import default

class Configuracion(models.Model):
   nombre_blog = models.CharField(max_length=14)
   construido_por = models.CharField(max_length=30)
   titulo_principal= models.CharField(max_length=30, default='')
   subtitulo_principal= models.CharField(max_length=60, default='')
   
class Post(models.Model):
   title = models.CharField(max_length=100)
   short_content = models.CharField(max_length=255)
   content = models.TextField(max_length=3000)
   date_published = models.DateTimeField(auto_now_add=True)

def __str__(self):
   return f"id:{self.id}, title:{self.title}"