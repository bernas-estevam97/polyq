from django.db import models


class HtmlTutorial(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class Images(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image_caption = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Introduction(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class Epidemiology(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)

    def __str__(self):
        return f'{self.text}'


class FirstDescribed(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class CausativeGene(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)

    def __str__(self):
        return f'{self.text}'


class CodifiedProtein(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)

    def __str__(self):
        return f'{self.text}'


class PathoPhysiology(models.Model):
    text = models.TextField()
    image = models.ManyToManyField(Images)

    def __str__(self):
        return f'{self.text}'


class CharacteristicsTableRows(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.text}'


class CharacteristicsTable(models.Model):
    rows_col = models.ManyToManyField(
        CharacteristicsTableRows, related_name='col1')

    # rows_col2 = models.ManyToManyField(CharacteristicsTableRows, related_name='col2')
    # rows_col3 = models.ManyToManyField(CharacteristicsTableRows, related_name='col3')
    def __str__(self):
        return f'{self.rows_col}'


class Clinical(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class ListItems(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'


class List(models.Model):
    text = models.CharField(max_length=200)
    item = models.ManyToManyField(ListItems)

    def __str__(self):
        return f'{self.text}'


class Reference(models.Model):
    author = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    journal_link = models.CharField(max_length=500)
    journal_link_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.journal_link_name}'


class Disease(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    first_described = models.ForeignKey(FirstDescribed, on_delete=models.CASCADE)
    epidemiology = models.ForeignKey(Epidemiology, on_delete=models.CASCADE)
    codified_protein = models.ForeignKey(CodifiedProtein, on_delete=models.CASCADE)
    patho_physiology = models.ForeignKey(PathoPhysiology, on_delete=models.CASCADE)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    list = models.ManyToManyField(List)
    references = models.ManyToManyField(Reference)
    characteristic_table = models.ForeignKey(CharacteristicsTable, on_delete=models.CASCADE)
    image = models.ManyToManyField(Images, blank=True)

    def __str__(self):
        return f'{self.name}'
