from django.contrib import admin
from .models import CollegeInfo, PositionsInfo, Roles, Department, Staff, CycleCommittees, StudentGroups, Specialties,\
    Qualifications, ProfModules, QualModules, StudyCycles, Modules, StudyDiscipline, MDK, Courses, Semester

# Register your models here.

admin.site.register(CollegeInfo)
admin.site.register(PositionsInfo)
admin.site.register(Roles)
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(CycleCommittees)
admin.site.register(StudentGroups)
admin.site.register(Specialties)
admin.site.register(Qualifications)
admin.site.register(ProfModules)
admin.site.register(QualModules)
admin.site.register(StudyCycles)
admin.site.register(Modules)
admin.site.register(StudyDiscipline)
admin.site.register(MDK)
admin.site.register(Courses)
admin.site.register(Semester)
