from .models import *
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


class ExcelAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Images, ExcelAdmin)
admin.site.register(Introduction, ExcelAdmin)
admin.site.register(Epidemiology, ExcelAdmin)
admin.site.register(FirstDescribed, ExcelAdmin)
admin.site.register(CausativeGene, ExcelAdmin)
admin.site.register(CodifiedProtein, ExcelAdmin)
admin.site.register(PathoPhysiology, ExcelAdmin)
admin.site.register(CharacteristicsTableRows, ExcelAdmin)
admin.site.register(CharacteristicsTable, ExcelAdmin)
admin.site.register(Clinical, ExcelAdmin)
admin.site.register(ListItems, ExcelAdmin)
admin.site.register(List, ExcelAdmin)
admin.site.register(Reference, ExcelAdmin)
admin.site.register(Disease, ExcelAdmin)
admin.site.register(HtmlTutorial, ExcelAdmin)
admin.site.register(CSS_Class, ExcelAdmin)
admin.site.register(Coordinate_Text, ExcelAdmin)
admin.site.register(RefLinks, ExcelAdmin)
admin.site.register(Trials, ExcelAdmin)
admin.site.register(AddedInfoTrials, ExcelAdmin)
