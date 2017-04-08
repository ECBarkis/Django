# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index( request ):
	return render( request, 'vinmyMVC/index.html' )

def show( request ):
	return render( request, 'vinmyMVC/show_users.html' )

def create( request ):
	if request.method == 'POST':
		request.session[ 'name' ] = request.POST[ 'first_name' ]
		return redirect( '/' )
	else:
		return redirect( '/' )