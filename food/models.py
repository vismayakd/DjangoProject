from django.db import models

# Create your models here.
class Items(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=200, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6w-cm1vGXpLrYd-1fo0WViPNtk2DuhR-xBnfDl7l-ADoW6AWx1rX_Cw-mPw&s')
