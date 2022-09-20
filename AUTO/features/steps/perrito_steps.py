from behave import *
import os
import requests
import signal
import time
import json

# service expose according to  http://192.168.49.2:32248/perrito

@given('a valid user is logged in for perrito')
def step_impl(context):
    pass

@when('the user sends a get request for perrito')
def step_impl(context):
    print("checking API /perrito")
    context.url = 'http://192.168.49.2:32248/perrito'
    context.headers = {'content-type': 'application/json'}
    context.response = requests.get(context.url)  
    print(context.response) # This is the response status code 
    print(context.response.content.decode('utf8')) # This is the body response code 
    print()
    assert True is not False
    # might check if there is a valid response assert context.response.status_code is not null 

@Then('the user obtains a 200 OK for perrito')
def step_impl(context):
    print("checking response status code")
    # if the response code is not 200 we are failing the step
    assert context.response.status_code == 200, "Response code is different: %s" % context.response.status_code + " Error: " + str(context.response.content)

@Then('the user obtains guau')
def step_impl(context):
    print('checking response body de perrito')
    body = context.response.content.decode('utf8') # get the body 
    data = json.loads(body) # get the json format for the body 
    print(body)
    print(data)
    print(data['perrito']) # print the value of the element perrito 
    # if perrito does have guau guau! as a response the scenario fails
    assert data['perrito'] == 'guau guau!', "Response code is different: %s" % context.response.status_code + " Error: " + str(context.response.content)

