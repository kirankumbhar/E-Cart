from django.db import models

# Create your models here.
class Products(models.Model):
	ProductID = models.IntegerField(primary_key=True)
	ProductSKU = models.CharField(max_length=50)
	ProductName = models.CharField(max_length=100)
	ProductPrice = models.FloatField()
	ProductWeight = models.FloatField()
	ProductCartDesc = models.CharField(max_length=250)
	ProductShortDesc = models.CharField(max_length=1000)
	ProductLongDesc = models.TextField()
	ProductThumb = models.CharField(max_length=100)
	ProductImage = models.CharField(max_length=100)
	ProductCategoryID = models.IntegerField()
	ProductUpdateDate = models.DateTimeField()
	ProductStock = models.FloatField()
	ProductLive = models.IntegerField()
	ProductUnlimited = models.IntegerField()
	ProductLocation = models.CharField(max_length=250)

	def __str__(self):
		self.name=ProductName



		