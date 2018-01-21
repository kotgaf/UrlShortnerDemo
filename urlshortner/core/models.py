from django.db import models

from utils.functions import generate_random_string


# Create your models here.
class Url(models.Model):
    short = models.CharField(max_length=10, db_index=True)
    url = models.CharField(max_length=500, null=False)
    views = models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def generate_unique_short(self):
        short = generate_random_string(length=10)
        i = 0
        while i < 100:
            if not Url.objects.filter(short=short).exists():
                break
            short = generate_random_string(length=10)
            i += 1
        if i >= 100:
            raise Exception('Generation unique ID failed')
        return short

    def save(self, *args, **kwargs):
        self.short = kwargs.get('short', self.generate_unique_short())
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['views', 'created']
