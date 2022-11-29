from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class Person (models.Model) :
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    class Meta:
        db_table = 'Person'

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self) :
        return (self.full_name)

class TargetDailyValue (models.Model) :
    tdv_sodium = models.IntegerField(default=0)
    tdv_protein = models.DecimalField(max_digits=8, decimal_places=2)
    tdv_water_male = models.DecimalField(max_digits=8, decimal_places=2)
    tdv_water_female = models.DecimalField(max_digits=8, decimal_places=2)
    tdv_K = models.DecimalField(max_digits=8, decimal_places=2)
    tdv_phos = models.DecimalField(max_digits=8, decimal_places=2)
    class Meta:
        db_table = 'Target_Daily_Value'

    def __str__(self) :
        return (self.tdv_sodium)

class TargetSerumLevel (models.Model) :
    tsl_K = models.DecimalField(max_digits=8, decimal_places=2)
    tsl_phos = models.DecimalField(max_digits=8, decimal_places=2)
    tsl_sodium = models.IntegerField(default=0)
    tsl_creatinine_male = models.DecimalField(max_digits=8, decimal_places=2)
    tsl_creatinine_female = models.DecimalField(max_digits=8, decimal_places=2)
    tsl_albumin = models.DecimalField(max_digits=8, decimal_places=2)
    tsl_blood_sugar = models.IntegerField(default=0)

    class Meta:
        db_table = 'Target_Serum_Level'

    def __str__(self) :
        return (self.tsl_blood_sugar)

class Comorbidity (models.Model) :
    morb_type = models.CharField(max_length=25)
    date_diagnosed = models.DateField(default=datetime.today)
    notes = models.CharField(max_length= 250)
    stage = models.CharField(max_length=10)
    targetSerumLevel = models.ForeignKey(TargetSerumLevel, on_delete=models.SET_NULL)
    targetDailyValue = models.ForeignKey(TargetDailyValue, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Comorbidity'

    def __str__(self) :
        return (self.morb_type)

class Client (Person) :
    username = models.CharField(max_length= 25)
    password = models.CharField(max_length=25)
    age = models.IntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    height_inches = models.IntegerField()
    birth_date = models.DateField(default=datetime.today)
    gender = models.CharField()
    comorbidity = models.ForeignKey(Comorbidity, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Client'

    def __str__(self) :
        return (self.username)


class ActualSerumLevel (models.Model) :
    asl_date = models.DateField(default=datetime.today)
    asl_K = models.DecimalField(max_digits=8, decimal_places=2)
    asl_phos = models.DecimalField(max_digits=8, decimal_places=2)
    asl_sodium = models.IntegerField(default=0)
    asl_creatinine = models.DecimalField(max_digits=8, decimal_places=2)
    asl_albumin = models.DecimalField(max_digits=8, decimal_places=2)
    asl_blood_sugar = models.IntegerField(default=0)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Actual_Serum_Level'

    def __str__(self) :
        return (self.asl_date)
 
class ActualDailyValue (models.Model) :
    adv_value_date = models.DateField(default=datetime.today)
    adv_sodium = models.IntegerField(default=0)
    adv_protein = models.DecimalField(max_digits=8, decimal_places=2)
    adv_water = models.DecimalField(max_digits=8, decimal_places=2)
    adv_K = models.DecimalField(max_digits=8, decimal_places=2)
    adv_phos = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        db_table = 'Actual_Daily_Value'

    def __str__(self) :
        return (self.adv_value_date)

class FoodDiaryEntry (models.Model) :
    fde_entry_date = models.DateField(default=datetime.today)
    fde_entry_time = models.TimeField(auto_now=True)
    fde_food_name = models.CharField(max_length=25)
    fde_sodium = models.IntegerField(default=0)
    fde_protein = models.DecimalField(max_digits=8, decimal_places=2)
    fde_water = models.DecimalField(max_digits=8, decimal_places=2)
    fde_K = models.DecimalField(max_digits=8, decimal_places=2)
    fde_phos = models.DecimalField(max_digits=8, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL)
    actualDailyValue = models.ForeignKey(ActualDailyValue, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'Food_Diary_Entry'

    def __str__(self) :
        return (self.fde_food_name)



