from django.contrib import admin
from main.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Challange)
admin.site.register(Participant)
admin.site.register(Category)