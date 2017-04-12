# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index( request ):
	context = {
		'courses': Course.objects.all()
	}
	return render( request, 'course/index.html', context )

def create( request ):
	post = request.POST
	Course.objects.create( name = post[ 'name' ], description = post[ 'description'])
	return redirect( '/' )

def destroy( request, id ):
	Course.objects.filter( id = id ).delete()
	return redirect( '/' )

def delete( request, id ):
	context = {
		'course': Course.objects.get( id = id )
	}
	return render( request, 'course/delete.html', context )

def home( request):
	return redirect( '/' )