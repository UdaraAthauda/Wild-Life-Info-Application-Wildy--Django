from django.db import models

# regional info model

class Region(models.Model):
    name = models.CharField(max_length=100)
    region = models.TextField(blank=True)

    def __str__(self):
        return self.name


# venom type info model

class VenomType(models.Model):
    VENOM_TYPE = [
        ('non-venomous', 'Non-Venomous'),
        ('mildly-venomous', 'Mildly-Venomous'),
        ('moderately-venomous', 'Moderately-Venomous'),
        ('deadly-venomous', 'Deadly-Venomous'),
    ]

    name = models.CharField(max_length=50, choices=VENOM_TYPE)
    effect_description = models.TextField()
    description_translation = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def venom_type_translation(self):
        venom_type = ''
        if self.name == "non-venomous":
            venom_type = "විෂ නොවන"
        elif self.name == "mildly-venomous":
            venom_type = "මද-විෂ සහිත"
        elif self.name == "moderately-venomous":
            venom_type = "මධ්‍යස්ථ-විෂ සහිත"
        else:
            venom_type = "මාරාන්තික-විෂ සහිත"
        
        return venom_type


# snake info model

class Snake(models.Model):
    COMMON_DANGER_LEVELS = [
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    ]

    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    description_translation = models.TextField(blank=True, null=True)
    danger_level = models.CharField(max_length=10, choices=COMMON_DANGER_LEVELS, default='low')
    image = models.ImageField(upload_to='snakes/', blank=True, null=True)
    is_venomous = models.ForeignKey(VenomType, on_delete=models.SET_NULL, null=True, blank=True)
    found_in = models.ManyToManyField(Region, related_name='snakes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

