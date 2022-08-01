from django.db import models


class HtmlTutorial(models.Model):
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class Coordinate_Text(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    device = models.CharField(max_length=500)
    disease_coords = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} {self.device} {self.disease_coords}'


class Images(models.Model):
    name = models.CharField(max_length=100, blank=True)
    image_caption = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name


class Introduction(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'{self.identifier}'


class Epidemiology(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)

    def __str__(self):
        return f'{self.identifier}'


class FirstDescribed(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'{self.identifier}'


class CausativeGene(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ManyToManyField(Images, blank=True)
    gene_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.identifier}'


class CodifiedProtein(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()
    protein_functions = models.TextField()
    protein_location = models.TextField()
    image = models.ManyToManyField(Images, blank=True)
    protein_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.identifier}'


class PathoPhysiology(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ManyToManyField(Images)

    def __str__(self):
        return f'{self.identifier}'


class CharacteristicsTableRows(models.Model):
    text = models.CharField(max_length=100, blank=True, null=True)
    text2 = models.CharField(max_length=100, blank=True, null=True)
    text3 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.text}'


class CharacteristicsTable(models.Model):
    table_identifier = models.CharField(max_length=100)
    table_title = models.CharField(max_length=200)
    table_caption = models.CharField(max_length=500)
    rows_col = models.ManyToManyField(
        CharacteristicsTableRows, related_name='col1')

    # rows_col2 = models.ManyToManyField(CharacteristicsTableRows, related_name='col2')
    # rows_col3 = models.ManyToManyField(CharacteristicsTableRows, related_name='col3')
    def __str__(self):
        return f'{self.table_identifier}'


class Clinical(models.Model):
    identifier = models.CharField(max_length=100)
    text = models.TextField()
    signs_symptoms = models.TextField()
    text_under_list = models.TextField(blank=True)

    def __str__(self):
        return f'{self.identifier}'


class ListItems(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'


class List(models.Model):
    text = models.CharField(max_length=200)
    item = models.ManyToManyField(ListItems)

    def __str__(self):
        return f'{self.text}'


class RefLinks(models.Model):
    link_identifier = models.CharField(max_length=100)
    ref_link = models.CharField(max_length=500)
    clickable_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.link_identifier}'


class Reference(models.Model):
    ref_name_disease = models.CharField(max_length=200)
    author_and_title = models.CharField(max_length=300)
    journal_info = models.CharField(max_length=200)
    links = models.ManyToManyField(RefLinks)

    def __str__(self):
        return f'{self.ref_name_disease}'


class CSS_Class(models.Model):
    # field_name = models.CharField(max_length=100)
    css_class = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.css_class}'


class Disease(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)
    first_described = models.ForeignKey(
        FirstDescribed, on_delete=models.CASCADE)
    epidemiology = models.ForeignKey(Epidemiology, on_delete=models.CASCADE)
    causative_gene = models.ForeignKey(CausativeGene, on_delete=models.CASCADE)
    codified_protein = models.ForeignKey(
        CodifiedProtein, on_delete=models.CASCADE)
    patho_physiology = models.ForeignKey(
        PathoPhysiology, on_delete=models.CASCADE)
    clinical = models.ForeignKey(Clinical, on_delete=models.CASCADE)
    list = models.ManyToManyField(List)
    references = models.ManyToManyField(Reference)
    characteristic_table = models.ForeignKey(
        CharacteristicsTable, on_delete=models.CASCADE)
    css_class = models.ForeignKey(
        CSS_Class, on_delete=models.CASCADE, blank=True, null=True)
    coordinates = models.ManyToManyField(Coordinate_Text, blank=True)

    # image = models.ManyToManyField(Images, blank=True)

    def __str__(self):
        return f'{self.name}'
