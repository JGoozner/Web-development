from django.contrib import admin

# Register your models here.


from .models import Todo

admin.site.register(Todo)






#********
#after models.py then admin.py
#for cmd
#run -> python manage.py migrate
#run -> python manage.py makemigrations appname
#run -> python manage.py migrate
# (then create superuser)
#run -> python manage.py createsuperuser
#********
