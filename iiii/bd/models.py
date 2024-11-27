from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'



class Course(models.Model):
    title = models.CharField('Title', max_length=100, db_index=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ManyToManyField(Teacher, related_name='courses')

    def __str__(self):
        return f'{self.title}'



class Group(models.Model):
    name = models.CharField('Название группы', max_length=100)
    year = models.IntegerField('Год обучения')
    group_number = models.IntegerField('Номер группы')
    courses = models.ManyToManyField(Course, related_name='groups')

    def __str__(self):
        return f'{self.name} - {self.year} курс, группа {self.group_number}'



class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField("Номер телефона", max_length=15, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students', default=1)

    def __str__(self):
        return f'{self.name}'



class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField('Name of the lecture', max_length=200)
    date = models.DateField('Date of the lecture')

    def __str__(self):
        return f'{self.title}: {self.date}'




class Practice(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='practice')
    title = models.CharField('Name of the practice', max_length=200)
    date = models.DateField('Date of the practice')

    def __str__(self):
        return f'{self.title}: {self.date}'