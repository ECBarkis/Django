# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index( request ):
	return render( request, 'form/index.html' )

def create( request ):
	request.session[ 'count' ] += 1
	request.session[ 'name' ] = request.POST[ 'name' ]
	request.session[ 'location' ] = request.POST[ 'location' ]
	request.session[ 'language' ] = request.POST[ 'language' ]
	request.session[ 'comment' ] = request.POST[ 'comment' ]
	return redirect( '/result' )

def result( request ):
	return render( request, 'form/results.html' )

def back( request ):
	print 'in back'
	return redirect( '/' )