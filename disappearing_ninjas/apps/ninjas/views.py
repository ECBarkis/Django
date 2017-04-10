# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index( request ):
	return HttpResponse( 'No Ninjas Here' )

def ninja( request, ninja ):
	context = { 'ninjas': ninja }
	return render( request, 'ninjas/index.html', context )