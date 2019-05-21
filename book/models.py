from django.db import models

class Save(models.Model) :
    saving1 = models.CharField(max_length = 200)
    saving2 = models.CharField(max_length = 200)
    saving3 = models.DateField('date published')

    def __str__ (self) :
        return self.saving1
    
    def summary(self) :
        return self.saving2[:100]


