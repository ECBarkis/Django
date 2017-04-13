# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$' )

# Create your models here.
class UserManager( models.Model ):
	def registration( self, postData ):
		counter = 0
		first = postData[ 'first' ]
		last = postData[ 'last' ]
		email = postData[ 'email' ]
		password = postData[ 'password' ].encode( 'utf-8' )
		confirm = postData[ 'confirm' ]
		hashed = bcrypt.hashpw( password , bcrypt.gensalt() )
		if len( first ) < 2:
			counter += 1
			print 'First name must be at least 2 characters'
		if len( last ) < 2:
			counter += 1
			print 'Last name must be at least 2 characters'
		if not EMAIL_REGEX.match( email ):
			counter += 1
			print 'Invalid email'
		if len( password ) < 8:
			counter += 1
			print 'Password must be at least 8 characters'
		if password != confirm:
			counter += 1
			print 'Password does not match password confirmation'
		if counter == 0:
			user = User.objects.create( first_name = first, last_name = last, email = email, password = hashed )
			print 'I am going to create the user'
			return True
		else:
			return False

	def login( self, postData ):
		user = User.objects.filter( email = postData[ 'email' ] )
		if user:
			user = user[ 0 ].password.encode( 'utf-8' )
		else:
			return False
		if postData[ 'password' ]:
			password = postData[ 'password' ].encode( 'utf-8' )
		else:
			return False
		if bcrypt.hashpw( password, user ) == user:
			return True
		else:
			return False

class User( models.Model ):
	first_name = models.CharField( max_length = 45 )
	last_name = models.CharField( max_length = 45 )
	email = models.CharField( max_length = 45 )
	password = models.CharField( max_length = 225 )
	created_at = models.DateTimeField( auto_now_add = True )
	updated_at = models.DateTimeField( auto_now = True )
	userManager = UserManager()