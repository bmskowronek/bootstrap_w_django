from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=70, unique=True)
    image_file = models.ImageField(upload_to ='uploads/') #needs Pillow
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "species"

class Chromosome(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    ''' NEEDS WORK
    def __str__(self):
        return self.   something
    '''
class SNP(models.Model):
    chromosome = models.ForeignKey(Chromosome, on_delete=models.CASCADE)
    position = models.IntegerField()
    allele_type = models.TextChoices("allele_type", "A T C G")
    ref_allele = models.CharField(blank=True, choices=allele_type, max_length=2)
    alt_allele = models.CharField(blank=True, choices=allele_type, max_length=2)
    maf = models.FloatField()
    annotations = models.CharField(max_length=10, blank=True) #opis kto co anotował na przyklad

    def __str__(self):
        return f"SNP at {self.chromosome}:{self.position} ({self.ref_allele}>{self.alt_allele})"

# Example usage:
# snp = SNP(chromosome=some_chromosome_instance, position=123456, ref_allele='A', alt_allele='G', maf=0.01, annotations='example')
# print(str(snp))  # Output: SNP at Chromosome_instance:123456 (A>G)
