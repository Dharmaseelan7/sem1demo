from django.contrib import admin
from .models.models1 import Sem_1_Marks_MECH, Sem_1_Marks_AIDS, Sem_1_Marks_AUTO, Sem_1_Marks_CIVIL, Sem_1_Marks_CSE, Sem_1_Marks_ECE, Sem_1_Marks_EEE, Sem_1_Marks_EIE, Sem_1_Marks_IT, Sem_1_Results_AIDS, Sem_1_Results_AUTO, Sem_1_Results_CIVIL, Sem_1_Results_CSE, Sem_1_Results_ECE, Sem_1_Results_EEE, Sem_1_Results_EIE, Sem_1_Results_IT, Sem_1_Results_MECH
from import_export.admin import ImportExportModelAdmin

# ------------ 1ST YEAR -----------


# ------------- SEMESTER 1 -----------


# ------------- EXPORT RESULTS ---------

@admin.register(Sem_1_Results_IT)
class ExportIT(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_CSE)
class ExportCSE(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_ECE)
class ExportECE(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_EEE)
class ExportEEE(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_AIDS)
class ExportAIDS(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_MECH)
class ExportMECH(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_CIVIL)
class ExportCIVIL(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_EIE)
class ExportEIE(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


@admin.register(Sem_1_Results_AUTO)
class ExportAUTO(ImportExportModelAdmin):
    list_display = ['Register_No']
    search_fields = ['Register_No', 'GPA']
    list_per_page = 30
    date_hierarchy = 'Added_On'


# ------------ END OF EXPORT ---------


# ------------- IMPORT MARKS ---------

@admin.register(Sem_1_Marks_IT)
class ImportIT(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_CSE)
class ImportCSE(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_ECE)
class ImportECE(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_EEE)
class ImportEEE(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_AIDS)
class ImportAIDs(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_MECH)
class ImportMECH(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_CIVIL)
class ImportCIVIL(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_EIE)
class ImportEIE(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


@admin.register(Sem_1_Marks_AUTO)
class ImportAUTO(ImportExportModelAdmin):
    list_display = ['Name']
    search_fields = ['Register_No']
    list_per_page = 30


# ------------ END OF IMPORT ---------

# ------------END OF SEMESTER 1---------
