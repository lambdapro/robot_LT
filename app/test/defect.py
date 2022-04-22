import urllib.request as urllib2
import sys
import json
import base64
import os
import datetime

ROBOT_LISTENER_API_VERSION = 3

def end_test(data, result):
    if not result.passed:
        print('Test "%s" failed: %s' % (result.name, result.message))
        input('Press enter to continue.')

JIRA_URL = "https://lambdatest.atlassian.net/" #enter url name here

JIRA_USERNAME = "" #enter user name here
JIRA_PASSWORD = ""  # For Jira Cloud use a token generated here: https://id.atlassian.com/manage/api-tokens

JIRA_PROJECT_KEY = "DEMO" #Your project key
JIRA_ISSUE_TYPE = "Bug"

def jira_rest_call(data):
    # Set the root JIRA URL, and encode the username and password
    url = JIRA_URL + '/rest/api/2/issue/'
    combined = JIRA_USERNAME+':'+JIRA_PASSWORD
    base64string = base64.b64encode(bytes(combined, 'utf-8'))
    print(base64string)
    # Build the request
    restreq = urllib2.Request(url)
    restreq.add_header('Content-Type', 'application/json')
    restreq.add_header("Authorization", "Basic "+base64string.decode());

    # Send the request and grab JSON response
    response = urllib2.urlopen(restreq, data)

    # Load into a JSON object and return that to the calling function
    return json.loads(response.read())

def generate_summary():
    return "Summary - " + '{date:%Y-%m-%d %H:%M}'.format(date=datetime.datetime.now())

def generate_description(data):
    return data

def generate_issue_data(summary, description):
    # Build the JSON to post to JIRA
    json_data = '''
    {
        "fields":{
            "project":{
                "key":"%s"
            },
            "summary": "%s",    
            "issuetype":{
                "name":"%s"
            },
            "description": "%s"
        } 
    } ''' % (JIRA_PROJECT_KEY, summary, JIRA_ISSUE_TYPE, description)
    return json_data.encode()
json_response = jira_rest_call(generate_issue_data(generate_summary(), generate_description("TEST DESCRIPTION")))
issue_key = json_response['key']
print("Created issue ", issue_key)
