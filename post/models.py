from django.db import models

class FilterRegion(models.Model):
    region_choices = [
        ('Алатауский', 'Алатауский'),
        ('Алмалинский', 'Алмалинский район'),
        ('Ауэзовский', 'Ауэзовский район'),
        ('Бостандыкский район', 'Бостандыкский район'),
        ('Медеуский район', 'Медеуский район'),
        ('Наурызбайский', 'Наурызбайский район'),
        ('Турксибский', 'Турксибский район'),
        ('Жетысуский', 'Жетысуский район'),
    ]

    region = models.CharField(max_length=50, choices=region_choices, unique=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.region

class Advertisement(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    regions = models.ManyToManyField(FilterRegion, related_name='advertisements', blank=True)

    def __str__(self):
        return self.title
    

