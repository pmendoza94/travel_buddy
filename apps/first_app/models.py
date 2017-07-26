from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []

        if not postData['name'] or len(postData['name']) < 3:
            results['status'] = False
            results['errors'].append('Name needs to be longer than 2 characters.')

        if not postData['username'] or len(postData['username']) < 3:
            results['status'] = False
            results['errors'].append('Username name needs to be longer than 2 characters.')

        if not postData['password'] or len(postData['password']) < 8:
            results['status'] = False
            results['errors'].append('Password needs to be at least 8 characters long.')

        if results['status'] == True:
            user = User.objects.filter(username = postData['username'])

        if len(user) != 0:
            results['status'] = False
            results['errors'].append('User already exists. Please try another email.')

        print results['status']
        print results['errors']
        return results


    def loginVal(self, postData):
        results = {'status':True, 'errors': [], 'user': None}

        if len(postData['username']) < 3:
            results['status'] = False
            results['errors'].append('Something went wrong. Double check everything.')

        else:
            user = User.objects.filter(username = postData['username'])

            if len(user) <= 0:
                results['status'] = False
                results['errors'].append('Something went wrong. Double check everything.')

            elif len(postData['password']) < 8 or postData['password'] != user[0].password:
                results['status'] = False
                results['errors'].append('Something went wrong. Double chekc everything.')

            else:
                results['user'] = user[0]

        print results['status']
        print results['errors']
        return results

    def createUser(self, postData):
        p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = User.objects. create(name = postData['name'], username = postData['username'], password = postData['password'])
        return user

class User(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
