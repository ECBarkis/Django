# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
import bcrypt


# Create your views here.
def index( request ):
	context = {
		'users': User.objects.all()
	}
	return render( request, 'login/index.html', context )

def create( request ):
	post = {
		'first': request.POST[ 'first_name' ],
		'last': request.POST[ 'last_name' ],
		'email': request.POST[ 'email' ],
		'password': request.POST[ 'password' ],
		'confirm': request.POST[ 'confirmation' ]
	}
	user = User.userManager.registration( post )
	if user == True:
		context = {
			'user': User.objects.get( email = request.POST[ 'email' ] ),
			'phrase': 'registered!'
		}
		return render( request, 'login/success.html', context )
	else:
		return redirect( '/' )

def login( request ):
	post = {
		'email': request.POST[ 'email' ],
		'password': request.POST[ 'password']
	}
	user = User.userManager.login( post )
	if user == True:
		context = {
			'user': User.objects.get( email = request.POST[ 'email' ] ),
			'phrase': 'logged in!'
		}
		return render( request, 'login/success.html', context )
	else:
		return redirect( '/')


