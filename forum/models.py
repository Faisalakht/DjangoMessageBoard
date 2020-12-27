from django.db import models
from authentication import models as authmodels

# Create your models here.
class Topic(models.Model):
    topictitle = models.CharField(max_length=120,verbose_name='Title')
    createdby = models.ForeignKey(authmodels.CustomUser,on_delete=models.CASCADE)
    createdtime = models.DateTimeField(auto_now_add=True, blank=True,db_index=True,verbose_name='Created Time')
    modifiedtime = models.DateTimeField(auto_now_add=True, blank=True,db_index=True,verbose_name='Modified Time')
    data = models.TextField()
    
    
    def __str__(self):
        return self.topictitle

class Post(models.Model):
    createdby = models.ForeignKey(authmodels.CustomUser,on_delete=models.CASCADE)
    createdtime = models.DateTimeField(auto_now_add=True, blank=True,verbose_name='Created Time')
    data = models.TextField()
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.createdby