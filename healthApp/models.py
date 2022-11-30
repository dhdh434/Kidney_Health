from django.db import models

 

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

 

class TargetSerumLevel (models.Model) :

    tsl_K = models.FloatField(default=0)

    tsl_phos = models.FloatField(default=0)

    tsl_Na = models.IntegerField(default=0)

    tsl_creatinine_male = models.FloatField(default=0)

    tsl_creatinine_female = models.FloatField(default=0)

    tsl_albumin = models.FloatField(default=0)

    tsl_blood_sugar = models.IntegerField(default=0)

 

    class Meta:

        db_table = 'Target_Serum_Level'

 

    def __str__(self) :

        return (self.tsl_blood_sugar)

 

class TargetDailyValue (models.Model) :

    tdv_sodium = models.IntegerField(default=0)

    tdv_protein = models.FloatField(default=0)

    tdv_water_male = models.FloatField(default=0)

    tdv_water_female = models.FloatField(default=0)

    tdv_K = models.FloatField(default=0)

    tdv_phos = models.FloatField(default=0)

 

    class Meta:

        db_table = 'Target_Daily_Value'

 

    def __str__(self) :

        return (self.tdv_sodium)

 

class Comorbidity (models.Model) :

    morb_type = models.CharField(max_length=25)

    date_diagnosed = models.DateField(blank=True)

    notes = models.CharField(max_length= 250)

    stage = models.CharField(max_length=10)

    target_serum_level = models.ForeignKey(TargetSerumLevel, null = True, blank=True, on_delete=models.SET_NULL)

    target_daily_value = models.ForeignKey(TargetDailyValue, null=True, blank=True, on_delete=models.SET_NULL)

 

    class Meta:

        db_table = 'Comorbidity'

 

    def __str__(self) :

        return (self.morb_type)

 

class Client (Person) :

    username = models.CharField(max_length= 25)

    password = models.CharField(max_length=25)

    age = models.IntegerField()

    weight = models.IntegerField()

    height_inches = models.IntegerField()

    birth_date = models.DateField()

    gender = models.CharField(max_length=10)

    comorbidity = models.ForeignKey(Comorbidity, null=True, blank=True, on_delete=models.SET_NULL)

 

    class Meta:

        db_table = 'Client'

 

    def __str__(self) :

        return (self.username)

 

class ActualSerumLevel (models.Model) :

    asl_serum_level_date = models.DateField(blank=True)

    asl_K = models.FloatField(default=0)

    asl_phos = models.FloatField(default=0)

    asl_Na = models.IntegerField(default=0)

    asl_creatinine = models.FloatField(default=0)

    asl_albumin = models.FloatField(default=0)

    asl_blood_sugar = models.IntegerField(default=0)

    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)

 

    class Meta:

        db_table = 'Actual_Serum_Level'

 

    def __str__(self) :

        return (self.asl_serum_level_date)

 

class FoodDiaryEntry (models.Model) :

    fde_entry_date = models.DateField(blank=True)

    fde_food_name = models.CharField(max_length=25)

    fde_sodium = models.IntegerField(default=0)

    fde_protein = models.FloatField(default=0)

    fde_water = models.FloatField(default=0)

    fde_K = models.FloatField(default=0)

    fde_phos = models.FloatField(default=0)

    client = models.ForeignKey(Client, null=True, blank=True, on_delete=models.SET_NULL)

 

    class Meta:

        db_table = 'Food_Diary_Entry'

 

    def __str__(self) :

        return (self.fde_food_name)

 

class ActualDailyValue (models.Model) :

    adv_value_date = models.DateField(blank=True)

    adv_sodium = models.IntegerField(default=0)

    adv_protein = models.FloatField(default=0)

    adv_water = models.FloatField(default=0)

    adv_K = models.FloatField(default=0)

    adv_phos = models.FloatField(default=0)

    food_diary_entry = models.ManyToManyField(FoodDiaryEntry, blank = True)

 

    class Meta:

        db_table = 'Actual_Daily_Value'

 

    def __str__(self) :

        return (self.adv_value_date)