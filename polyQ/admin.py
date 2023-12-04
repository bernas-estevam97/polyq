from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from translations.admin import TranslatableAdmin, TranslationInline
# from translations.models import Translation


class ModelAdmin(ImportExportModelAdmin):
    # inlines = [TranslationInline, ]
    pass


admin.site.register(Images, ModelAdmin)
admin.site.register(Introduction, ModelAdmin)
admin.site.register(Epidemiology, ModelAdmin)
admin.site.register(FirstDescribed, ModelAdmin)
admin.site.register(CausativeGene, ModelAdmin)
admin.site.register(CodifiedProtein, ModelAdmin) 
admin.site.register(PathoPhysiology, ModelAdmin)
admin.site.register(CharacteristicsTableRows, ModelAdmin)
admin.site.register(CharacteristicsTable, ModelAdmin)
admin.site.register(Clinical, ModelAdmin)
admin.site.register(ListItems, ModelAdmin)
admin.site.register(List, ModelAdmin)
admin.site.register(Reference, ModelAdmin)
admin.site.register(Disease, ModelAdmin)
admin.site.register(HtmlTutorial, ModelAdmin)
admin.site.register(CSS_Class, ModelAdmin)
admin.site.register(Coordinate_Text, ModelAdmin)
admin.site.register(RefLinks, ModelAdmin)
admin.site.register(Trials. ExcelAdmin)
admin.site.register(AddedInfoTrials, ModelAdmin)
# admin.site.register(Translation)
