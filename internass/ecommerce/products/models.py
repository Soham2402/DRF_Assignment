from django.db import models
import uuid 

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")
    quantity = models.PositiveIntegerField(default=1, null=False)
    #Adding choices for category size and weight (Not reccomended in an ecommerce use case)
    CATEGORY_CHOICE = [
        ('clothing','Clothing'),
        ('food','Food')
    ]
    
    SIZE_CHOICE = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra-Large')
    ]
    
    WEIGHT_CHOICE = [
        ('250g', '250 gram'),
        ('500g', '500 gram'),
        ('1kg', '1 Kilogram'),
        ('1.5kg', '1.5 Kilogram')
    ]
    category = models.CharField(max_length=150,choices=CATEGORY_CHOICE)    
    size = models.CharField(max_length=20, choices=SIZE_CHOICE, blank=True)
    weight = models.CharField(max_length=20, choices=WEIGHT_CHOICE, blank=True)

    #Dynamically choosing size or weight based on the category
    def get_fields(self):
        fields = super.get_fields()
        if self.category == "Clothing":
            fields.pop('weight',None)
        
        #simply add more conditions if more categories are added
        else: 
            fields.pop('size',None)  
        return fields
    
    def __str__(self):
        return self.name