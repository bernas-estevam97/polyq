from django.db import models


class Images(models.Model):
    image = models.ImageField()


class Introduction(models.Model):
    text = models.TextField()


class Epidemology(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)


class FirstDescribed(models.Model):
    text = models.TextField()


class CausativeGene(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)


class CodifiedProtein(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)


class PathoPhysiology(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images)


class CharacteristicsTableRows(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=100, blank=True, null=True)


class CharacteristicsTable(models.Model):
    rows_col = models.ManyToManyField(CharacteristicsTableRows, related_name='col1')
    # rows_col2 = models.ManyToManyField(CharacteristicsTableRows, related_name='col2')
    # rows_col3 = models.ManyToManyField(CharacteristicsTableRows, related_name='col3')


class Clinical(models.Model):
    text = models.TextField()


class ListItems(models.Model):
    text = models.CharField(max_length=200)


class List(models.Model):
    text = models.CharField(max_length=200)
    item = models.ManyToManyField(ListItems)


class Reference(models.Model):
    text = models.TextField()


class Disease(models.Model):
    name = models.CharField(max_length=200)
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    epidemology = models.ForeignKey(Epidemology, on_delete=models.CASCADE)
    first_described = models.ForeignKey(FirstDescribed, on_delete=models.CASCADE)
    codified_protein = models.ForeignKey(CodifiedProtein, on_delete=models.CASCADE)
    patho_physiology = models.ForeignKey(PathoPhysiology, on_delete=models.CASCADE)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    list = models.ManyToManyField(List)
    references = models.ManyToManyField(Reference)
    characteristic_table = models.ForeignKey(CharacteristicsTable, on_delete=models.CASCADE)
