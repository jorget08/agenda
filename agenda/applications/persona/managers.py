from django.db import models
from django.db.models import Count

class ReunionManager(models.Manager):

    # agrupa a las personas por trabajo y cuenta cuantas veces encontro cada trabajo
    def cantidad_reuniones_job(self):  
                    #values agrupa por el trabajo de las personas
        return self.values('persona__job').annotate(cantidad=Count('id'))