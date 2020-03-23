from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CompanyProfile(models.Model):
    '''
    Country
    State
    '''
    COUNTRY_CHOICES =(
        ('Nigeria', 'Nigeria'),
        ('Kenya', 'Kenya'),
        ('Ghana', 'Ghana'),
        ('South Africa', 'South Africa')
    )
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            related_name="profile_admin"
        )
    fullname =  models.CharField(max_length=100)
    profile_pic= models.ImageField(upload_to=user_directory_path)
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    company_name= models.CharField(max_length=100, blank=True, null=True)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    company_telephone_no = models.CharField(max_length=14, help_text="Start With 234", blank=True, null=True)
    # state = models.CharField(max_length=100 choices=COUNTRY_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated  = models.DateTimeField(auto_now=True)



