from django.db import models
from datetime import datetime as date

class Livro(models.Model):

    opcoes_categoria = [
         ("MOTIVACIONAL","Motivacional")
        ,("LIFESTYLE","Lifestyle")
        ,("ESTRATÉGIA","Estratégia")
        ,("FINANÇAS","Finanças")
    ]

    titulo  = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=opcoes_categoria,default='')
    descricao = models.TextField(null=False,blank=False)
    foto =  models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=False)
    data_adicao_livro = models.DateTimeField(default=date.now, blank=False)

    def __str__(self):
        return self.titulo