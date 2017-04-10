# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index( request ):
	return render( request, 'gold/index.html' )

def process( request ):
	post = request.POST
	gold = 0

	if post[ 'where' ] == 'farm':
		gold = random.randint( 10, 20 )
		request.session[ 'gold' ] += gold

	if post[ 'where' ] == 'cave':
		gold = random.randint( 5, 10 )
		request.session[ 'gold' ] += gold

	if post[ 'where' ] == 'house':
		gold = random.randint( 2, 5 )
		request.session[ 'gold' ] += gold

	if post[ 'where' ] == 'casino':
		gold = random.randint( -50, 50 )
		request.session[ 'gold' ] += gold

	location = post[ 'where' ]
	if location == 'casino':
		if gold > 0:
			activities = 'Entered a casino and won {} gold!...Sweet\n'.format( gold ) + request.session[ 'activities' ]

		elif gold < 0:
			activities = 'Entered a casino and lost {} gold!...Ouch\n'.format( gold ) + request.session[ 'activities' ]

		else:
			activities = 'Entered a casino and broke even\n' + request.session[ 'activities' ]

	else:
		activities = 'Earned {} gold from the {}!\n'.format( gold, location ) + request.session[ 'activities' ]

	request.session[ 'activities' ] = activities
	return redirect( '/' )

def start( request ):
	request.session[ 'gold' ] = 0
	request.session[ 'activities' ] = ''
	return redirect( '/' )