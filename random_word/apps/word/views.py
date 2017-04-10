# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
import string

def random_generator( size = 14, chars = string.ascii_uppercase + string.digits ):
	return ''.join( random.choice( chars ) for x in range( size ) )

# Create your views here.
def index( request ):
	return render( request, 'word/index.html' )

def create( request ):
	request.session[ 'word' ] = random_generator()
	request.session[ 'count' ] += 1
	return redirect( '/' )

def reset( request ):
	request.session[ 'count' ] = 0
	request.session[ 'word' ] = ''
	return redirect( '/' )