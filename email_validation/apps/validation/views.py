# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Email
import re
from django.core.urlresolvers import reverse

EMAIL_REGEX = re.compile( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$' )

# Create your views here.
def index( request ):
	return render( request, 'validation/index.html' )

def create( request ):
	if request.method == 'GET':
		context = {
			'emails': Email.objects.all(),
			'email': Email.objects.last()
		}
		return render( request, 'validation/success.html', context )
	post = request.POST
	email = post[ 'email' ]
	if not EMAIL_REGEX.match( email ):
		request.session[ 'error' ] = 'Invalid Email Address'
		return redirect( '/' )
	else:
		email = Email.objects.create( email = email )
		context = {
			'emails': Email.objects.all(),
			'email': email
		}
		request.session[ 'error' ] = ''
		return render( request, 'validation/success.html', context )

def destroy( request, id ):
	Email.objects.filter( id = id ).delete()
	return redirect( '/create' )