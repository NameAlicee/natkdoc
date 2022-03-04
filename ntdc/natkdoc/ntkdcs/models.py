from django.db import models
from datetime import date

# Create your models here.
# Сведения о колледже.


class CollegeInfo(models.Model):

    FullName = models.TextField("Полное оффициальное название")
    ShortName = models.CharField("Сокращенное название", max_length=20)

    def __str__(self):
        return self.ShortName

    class Meta:
        verbose_name = "Сведения о колледже"
        verbose_name_plural = "Сведения о колледже"


class PositionsInfo(models.Model):

    name = models.TextField("Должность", max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Roles(models.Model):

    name = models.TextField("Роли")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Department(models.Model):

    name = models.TextField("Наименование отделения")
    manager = models.ForeignKey(Roles, verbose_name="Заведующий", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отделение"
        verbose_name_plural = "Отделения"


class Staff(models.Model):

    name = models.TextField("Имя")
    surname = models.TextField("Фамилия")
    patronymic = models.TextField("Общество")
    position = models.ForeignKey(PositionsInfo, verbose_name="Должность", on_delete=models.SET_NULL, null=True)
    base_roles = models.ForeignKey(Roles, verbose_name="Роль в БД", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Люди"
        verbose_name_plural = "Люди"


class CycleCommittees(models.Model):

    name = models.TextField("Наименование цикловой комисии")
    department = models.ForeignKey(Department, verbose_name="Отделение", on_delete=models.SET_NULL, null=True)
    chairman = models.ManyToManyField(Staff, verbose_name="Председатели ЦК", related_name="committees_chairmans")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цикловая комиссия"
        verbose_name_plural = "Цикловые комиссии"


class StudentGroups(models.Model):

    group_code = models.CharField("Код группы", max_length=30)
    department = models.ForeignKey(Department, verbose_name="отделение", on_delete=models.SET_NULL, null=True)
    year_of_enrollment = models.DateField("Год набора", default=date.today)
    base_nine_eleven = models.PositiveIntegerField("База 9/11 классов", default=9)

    def __str__(self):
        return self.group_code

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"


class Specialties(models.Model):

    specialities_code = models.CharField("Код специальности", max_length=30)
    name = models.TextField("Наименование специальности")
    department = models.ForeignKey(Department, verbose_name="отделение", on_delete=models.SET_NULL, null=True)
    cycle_committee = models.ForeignKey(CycleCommittees, verbose_name="цикловая комиссия",
                                        on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.specialities_code

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Qualifications(models.Model):

    name = models.TextField("Наименование квалификации")
    Spec = models.ForeignKey(Specialties, verbose_name="специальности", on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, verbose_name="отделение", on_delete=models.SET_NULL, null=True)
    cycle_committee = models.ForeignKey(CycleCommittees, verbose_name="цикловая комиссия",
                                        on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Квалификация"
        verbose_name_plural = "Квалификации"


class ProfModules(models.Model):

    name_main = models.TextField("Наименование основных видов деятельности")
    name_prof = models.TextField("Наименование профессиональных модулей")

    def __str__(self):
        return self.name_main

    class Meta:
        verbose_name = "Профессиональный модуль"
        verbose_name_plural = "Профессиональные модули"


class QualModules(models.Model):

    qual = models.ManyToManyField(Qualifications, verbose_name="Квалификации")
    modules = models.ManyToManyField(ProfModules, verbose_name="Модуль")

    def __str__(self):
        return self.qual

    class Meta:
        verbose_name = "Квалификации модули"
        verbose_name_plural = "Квалификации модули"


class StudyCycles(models.Model):

    index = models.CharField("Индекс", max_length=40)
    name = models.TextField("Наименование")
    Hours = models.PositiveIntegerField("Количество часов", default=0)

    def __str__(self):
        return self.index

    class Meta:
        verbose_name = "Учебный цикл"
        verbose_name_plural = "Учебные циклы"


class Modules(models.Model):

    index = models.CharField("Индекс", max_length=40)
    name = models.TextField("Наименование")
    Cycle = models.ForeignKey(StudyCycles, verbose_name="Учебный Модуль", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.index

    class Meta:
        verbose_name = "Учебный модуль"
        verbose_name_plural = "Учебные модули"


class StudyDiscipline(models.Model):
    index = models.CharField("Индекс", max_length=40)
    name = models.TextField("Наименование")
    Cycle = models.ForeignKey(StudyCycles, verbose_name="Учебный Модуль", on_delete=models.SET_NULL, null=True)
    TotalHours = models.PositiveIntegerField("Всего часов", default=0)
    AuditoreHours = models.PositiveIntegerField("Часов аудиторных всего", default=0)
    PracticeHours = models.PositiveIntegerField("В том числе практических", default=0)
    CourseProjectHours = models.PositiveIntegerField("Курсовой проект", default=0)
    ProductionPracticeHours = models.PositiveIntegerField("Практики", default=0)
    IndependentHours = models.PositiveIntegerField("Самостоятельные", default=0)
    Variety = models.BooleanField("Вариативный", default=True)

    def __str__(self):
        return self.index

    class Meta:
        verbose_name = "Учебная дисциплина"
        verbose_name_plural = "Учебные дисциплины"


class MDK(models.Model):

    index = models.CharField("Индекс", max_length=40)
    name = models.TextField("Наименование")
    modules = models.ForeignKey(Modules, verbose_name="Модули", on_delete=models.SET_NULL, null=True)
    TotalHours = models.PositiveIntegerField("Всего часов", default=0)
    AuditoreHours = models.PositiveIntegerField("Часов аудиторных всего", default=0)
    PracticeHours = models.PositiveIntegerField("В том числе практических", default=0)
    CourseProjectHours = models.PositiveIntegerField("Курсовой проект", default=0)
    ProductionPracticeHours = models.PositiveIntegerField("Практики", default=0)
    IndependentHours = models.PositiveIntegerField("Самостоятельные", default=0)
    Variety = models.BooleanField("Вариативный", default=True)

    def __str__(self):
        return self.index

    class Meta:
        verbose_name = "МДК"
        verbose_name_plural = "МДК"


class Courses(models.Model):
    number = models.PositiveIntegerField("Номер", default=1)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Semester(models.Model):
    number = models.PositiveIntegerField("Номер", default=1)
    weeks = models.PositiveIntegerField("Номер", default=16)
    courses = models.ForeignKey(Courses, verbose_name="Учебный Курс", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Семестр"
        verbose_name_plural = "Семестры"
