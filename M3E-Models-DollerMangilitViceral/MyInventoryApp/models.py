'''
Tashannah H. Doller, 245541
Sebastian Mangilit, ID number
Jared Viceral, ID Number
14 February 2026

We hereby attest to the truth of the following facts:
We have not discussed the Python code in my program with anyone 
other than our instructor or the teaching assistants assigned to this course.
We have not used Python code obtained from another student, 
or any other unauthorized source, whether modified or unmodified.
If any Python code or documentation used in my program was 
obtained from another source, it has been clearly noted with 
citations in the comments of our program.
'''

from django.db import models
from django.utils import timezone

class Supplier(models.Model): # i followed the same format as the sample in the slides
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()
    
    def getName(self):
        return self.name

    def __str__(self):
        return f"{self.name} - {self.city}, {self.country} created at: {self.created_at}"

class WaterBottle(models.Model):
    sku =  models.CharField(max_length=300, unique=True)
    brand = models.CharField(max_length=300)
    cost = models.DecimalField(max_digits=300, decimal_places=2)
    size = models.CharField(max_length=300)
    mouth_size = models.CharField(max_length=300)
    color = models.CharField(max_length=300)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE) # from the slides too
    current_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.sku}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by.name}, {self.cost} : {self.current_quantity}"

'''
Reference(s):
- GeeksforGeeks. (2019, October 9). DecimalField Django Models. GeeksforGeeks. https://www.geeksforgeeks.org/python/decimalfield-django-models/
'''