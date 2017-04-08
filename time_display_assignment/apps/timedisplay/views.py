# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index( request ):
  context = {
  	"somekey": datetime.datetime.now()
  }
  return render( request, 'timedisplay/page.html', context )