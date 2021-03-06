from django.db import models

# Create your models here.
class Blog(models.Model) : #{   ## REMEBER TO WRITE models.Model
    title    = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    body     = models.TextField()

    def __str__(self) : #{
        return self.title    
    #}

    def preview(self) : #{
        return self.body[:100]    
    #}
#}
