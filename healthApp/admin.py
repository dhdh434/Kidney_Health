from django.contrib import admin
from .models import Person, Client, ActualSerumLevel, Comorbidity, FoodDiaryEntry, ActualDailyValue, TargetSerumLevel, TargetDailyValue

admin.site.register(Person)
admin.site.register(Client)
admin.site.register(ActualSerumLevel)
admin.site.register(Comorbidity)
admin.site.register(FoodDiaryEntry)
admin.site.register(ActualDailyValue)
admin.site.register(TargetSerumLevel)
admin.site.register(TargetDailyValue)