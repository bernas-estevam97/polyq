from modeltranslation.translator import translator, TranslationOptions
from .models import *

class IntroductionTranslationOptions(TranslationOptions):
    fields = ('text',)


class DiseaseTranslationOptions(TranslationOptions):
    fields = ('slug',)

class CoordinatesTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)

class ImagesTranslationOptions(TranslationOptions):
    fields = ('name', 'image_caption',)

class EpidemiologyTranslationOptions(TranslationOptions):
    fields = ('text',)

class FirstDescribedTranslationOptions(TranslationOptions):
    fields = ('text',)

class CausativeGeneTranslationOptions(TranslationOptions):
    fields = ('text', 'gene_name')

class CodifiedProteinTranslationOptions(TranslationOptions):
    fields = ('text', 'protein_functions', 'protein_location', 'protein_name',)

class PathoPhysiologyTranslationOptions(TranslationOptions):
    fields = ('text',)

class ClinicalTranslationOptions(TranslationOptions):
    fields = ('text', 'signs_symptoms', 'text_under_list',)

class CharacteristicsTableRowsTranslationOptions(TranslationOptions):
    fields = ('text',)

class CharacteristicsTableTranslationOptions(TranslationOptions):
    fields = ('table_title', 'table_caption',)

class ListTranslationOptions(TranslationOptions):
    fields = ('text',)

class ListItemsTranslationOptions(TranslationOptions):
    fields = ('text',)

class TrialsTranslationOptions(TranslationOptions):
    fields = ('text',)

class AddedInfoTrialsTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(Introduction, IntroductionTranslationOptions)
translator.register(Disease, DiseaseTranslationOptions)
translator.register(Coordinate_Text, CoordinatesTranslationOptions)
translator.register(Images, ImagesTranslationOptions)
translator.register(Epidemiology, EpidemiologyTranslationOptions)
translator.register(FirstDescribed,FirstDescribedTranslationOptions)
translator.register(CausativeGene, CausativeGeneTranslationOptions)
translator.register(CodifiedProtein, CodifiedProteinTranslationOptions)
translator.register(PathoPhysiology, PathoPhysiologyTranslationOptions)
translator.register(Clinical ,ClinicalTranslationOptions)
translator.register(CharacteristicsTableRows, CharacteristicsTableRowsTranslationOptions)
translator.register(CharacteristicsTable, CharacteristicsTableTranslationOptions)
translator.register(List ,ListTranslationOptions)
translator.register(ListItems ,ListItemsTranslationOptions)
translator.register(Trials, TrialsTranslationOptions)
translator.register(AddedInfoTrials, AddedInfoTrialsTranslationOptions)




# python manage.py update_translation_fields -----------> update values with previously existing ones 
#                                                         after adding language columns to database
