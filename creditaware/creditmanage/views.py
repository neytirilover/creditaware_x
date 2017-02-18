# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_page(request):
	return HttpResponse("<p>Under development, thank you.</p>")
