from django.db import models

class Usuarios(models.Model):

    nombres=models.CharField(max_length=30)
    documento=models.CharField(max_length=30)

    class Meta:
        managed=False
        db_table= 'usuarios'

    def __str__(self) :
        return self.nombres
    
class Empleados(models.Model):
        
    id = models.IntegerField
    nombres=models.CharField(max_length=30)
    documento=models.CharField(max_length=30)

    class Meta:
        managed=False
        db_table= 'empleados'
        
    def __str__(self) :
        return self.nombres
    
