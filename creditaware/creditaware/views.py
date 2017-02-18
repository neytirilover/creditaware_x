# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.forms import ModelForm
from creditmanage.models import user_card, creditCard
from django.forms import modelform_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm


# class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # class Meta:
        # model = User
        # fields = ("username", "password1", "password2", "email")
        
    # def save(self, commit=True):
        # user = super(UserCreateForm, self).save(commit=False)
        # user.email = self.cleaned_data["email"]
        # if commit:
            # user.save()
        # return user

class user_cardForm(ModelForm):
    class Meta:
        model = user_card
        fields = ['card', 'activation_date', 'expiry_date', 'isActive','creditLine']
		
@csrf_protect
def show_index(request):
    errorid = request.GET.get('eid')
    UNAME_ALERT = ''
    if errorid == '1':
        UNAME_ALERT = 'Username already Exists!'
    elif errorid == '2':
        UNAME_ALERT = 'Please check your password'
    return render(request, "index.html",{'MEDIA_ROOT':settings.MEDIA_ROOT, 'UNAME_ALERT':UNAME_ALERT})  

	
#-----------------------------------------------------------------------------------------
@csrf_protect
def user_login(request):
    '''
    login
    '''
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(username=username, password=password)
        if user is not None and user.is_active:
                login(request, user)
                user_obj_id = user.id
                #ctx.update(csrf(request))
                return redirect(reverse('login_landing')+'?uid='+str(user_obj_id))            
    ctx = {}
    ctx['MEDIA_ROOT']=settings.MEDIA_ROOT
    ctx['STATIC_ROOT']=settings.STATIC_ROOT
    return redirect('/admin')

@csrf_protect
def user_register(request):
    '''
    register
    '''
    if request.POST:
        new_username = request.POST.get('username')
        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')
        new_email = request.POST.get('email')
        new_last_name = request.POST.get('last_name')
        new_fisrt_name = request.POST.get('first_name')
        try:
            NoconflictUser = False
            conflictUser = User.objects.get(username = new_username)
        except:
            NoconflictUser = True
            pass
        if NoconflictUser is not True:
            return redirect(reverse('show_index')+'?eid='+'1')
        elif new_password1 and new_password2 and new_password1==new_password2:
            new_user = User.objects.create_user(new_username, new_email, new_password1)
            new_user.first_name = new_fisrt_name
            new_user.last_name = new_last_name
            new_user.save()
            new_user_id = new_user.id
            login(request, new_user)
            return redirect(reverse('login_landing')+'?uid='+str(new_user_id))
        else:
            return redirect(reverse('show_index')+'?eid='+'2')



@csrf_protect	
def user_add_card(request):
    SWITCH_CHOICES = ((0,'No'),(1,'Yes'))
    YEARS = range(1980,2080)
    userid = request.GET.get('uid')
    user = User.objects.get(id = int(userid))
    cards = user_card.objects.filter(user = user)
    form = modelform_factory(user_card, form=user_cardForm, widgets = {'activation_date':forms.SelectDateWidget(years = YEARS), 'expiry_date':forms.SelectDateWidget(years = YEARS), 'isActive': forms.Select(choices=SWITCH_CHOICES)})
    if request.POST:
        if request.POST.get('card') is not None:
            new_user_card = user_card()
            new_user_card.user = user
            new_user_card.card = creditCard.objects.get(id = request.POST.get('card'))
            new_user_card.name = new_user_card.user.first_name + '\'s ' + new_user_card.card.name
            new_user_card.activation_date = request.POST.get('activation_date_year')+'-'+request.POST.get('activation_date_month')+'-'+request.POST.get('activation_date_day')
            new_user_card.expiry_date = request.POST.get('expiry_date_year')+'-'+request.POST.get('expiry_date_month')+'-'+request.POST.get('expiry_date_day')
            new_user_card.isActive = request.POST.get('isActive')
            new_user_card.creditLine = request.POST.get('creditLine')
            new_user_card.save()
            return redirect(reverse('user_add_card') + '?uid='+userid)
    return render(request, "new_card.html", {'uid':userid,'p_form':form,'object_list':cards})

@csrf_protect    
def delete_card(request):
    userid = request.GET.get('uid')
    cardid = request.GET.get('cid')
    #first get the object from cid:
    card_del = user_card.objects.get(id = int(cardid))
    #then delete_card
    card_del.delete()
    #now return to user_add_card with userid as url query string
    return redirect(reverse('user_add_card') + '?uid='+userid)
	
@csrf_protect	
def login_landing(request):

    userid = request.GET.get('uid')
    user = User.objects.get(id = int(userid))
    p_name = user.first_name
	
    return render(request, "landing.html", {'p_name':p_name, 'p_uid':userid, 'user':user})
    #return HttpResponse("<p>世界好</p>")
	
	
def user_logout(request):
    '''
    logout
    URL: /users/logout
    '''
    logout(request)
    return redirect('/')