from django.db import models
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator

class Species(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, unique=True)
    image_file = models.ImageField(upload_to ='snp_site/uploads/') #needs Pillow

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image_file.path)

        # Resize image to 400x400
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image_file.path)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "species"


class Chromosome(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    def __str__(self):
        return f'chromosome {self.name} of {self.species}'


class SNP(models.Model):
    chromosome = models.ForeignKey(Chromosome, on_delete=models.CASCADE)
    position = models.IntegerField()
    allele_type = models.TextChoices("allele_type", "A T C G")
    ref_allele = models.CharField(blank=True, choices=allele_type, max_length=2)
    alt_allele = models.CharField(blank=True, choices=allele_type, max_length=2)
    maf = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(0.49)]
    )
    annotations = models.TextField() #opis kto co anotował na przyklad

    def __str__(self):
        return f"SNP at {self.chromosome}:{self.position} ({self.ref_allele}>{self.alt_allele})"


