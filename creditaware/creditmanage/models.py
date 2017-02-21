from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import date


class creditCard(models.Model):
    SWITCH_CHOICES = ((0,'False'),(1,'True'))
    GRADE_CHOICES = ((0,'Basic'),(1,'beginner'),(2, 'Intermediate'),(3, 'Advanced'))
    CARD_NETWORK_CHOICES = ((0,'Discover'),(1,'VISA'),(2, 'MasterCard'),(3, 'American Express'),(4, 'Other'))
    name = models.CharField(max_length=200)
    comp_name = models.CharField(max_length=200)
    ann_fee = models. IntegerField(default=-1)
    reward_type = models.CharField(max_length=20)
    reward_points = models. IntegerField(default=-1)
    reward_dealine = models. FloatField(default=-1.0)
    reward_spend = models.IntegerField(default=-1)
    comment =  models.CharField(max_length=500)
    isChase524 = models.IntegerField(choices=SWITCH_CHOICES, default=0)
    isChargeCard = models.IntegerField(choices=SWITCH_CHOICES, default=0)
    isFirstYearFree = models.IntegerField(choices=SWITCH_CHOICES, default=0)
    cardGrade = models.IntegerField(choices=GRADE_CHOICES, default=1)
    isKeepable = models.IntegerField(default=0)
    isHotelC = models.IntegerField(choices=SWITCH_CHOICES, default=0)
    isAirlineC = models.IntegerField(choices=SWITCH_CHOICES, default=0)
    hasFTF = models.IntegerField(choices=SWITCH_CHOICES, default=1)
    isDowngradable = models.IntegerField(choices=SWITCH_CHOICES, default=0)
    id_num = models.IntegerField(default=-1)
    min_credit_history = models.IntegerField(default = -1)
    card_network = models. IntegerField(choices=CARD_NETWORK_CHOICES, default=1)
    card_image = models.ImageField(upload_to='card_images/',default='card_images/no-img-placeholder.png')
    
    def __unicode__(self):
        return self.name
		
		
		
		
		
class user_card(models.Model):
    user = models.ForeignKey(User)
    card = models.ForeignKey(creditCard)
    name = models.CharField(max_length = 100, default = 'default')
    activation_date = models.DateField(default = str(date.today().year)+'-'+str(date.today().month)+'-'+str(date.today().day))
    expiry_date = models.DateField(default = str(date.today().year+1)+'-'+str(date.today().month)+'-'+str(date.today().day))
    isActive = models.IntegerField(default = 1)
    creditLine = models.IntegerField(default=1)
	
    def __unicode__(self):
        return self.name