from __future__ import unicode_literals
from django.db import models
from ..first_app.models import User

# Create your models here.
class DestinationManager(models.Manager):
    def tripVal(self, postData):
        results = {'status': True, 'errors': []}
        destination = []

        if not postData['location'] or len(postData['location']) < 2:
            results['status'] = False
            results['errors'].append('Please add a destination.')

        if not postData['description'] or len(postData['description']) < 2:
            results['status'] = False
            results['errors'].append('Please add a description.')

        # if not postData['travel_date_from'] or len(postData['travel_date_from' == '%m/%d/%y']):
        #     results['status'] = False
        #     results['errors'].append('Please add a travel date from.')
        #
        # if not postData['travel_date_to'] or len(postData['travel_date_from' == '%m/%d/%y']):
        #     results['status'] = False
        #     results['errors'].append('Please add a travel date to.')

        if results['status'] == True:
            destination = Destination.objects.filter(location = postData['location'])

        if len(destination) != 0:
            results['status'] = False
            results['errors'].append('Destination/Plan has already been added.')

        print results['status']
        print results['errors']
        return results

    def createDestination(self, postData):
        destination = Destination.objects.create(location = postData['location'], description = postData['description'], travel_date_from = postData['travel_date_from'], travel_date_to = postData['travel_date_to'])
        return destination

class Destination(models.Model):
    location = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    travel_date_from = models.DateField(default = ['%m/%d/%Y'])
    travel_date_to = models.DateField(default = ['%m/%d/%Y'])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = DestinationManager()

class Traveler(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
