from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=200)
    cardNumber = models.CharField(max_length=50)
    birthDate = models.DateField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return self.name
    
