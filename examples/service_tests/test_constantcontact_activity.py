from constantcontact import ConstantContact, Contact, Multipart_Activity

import json
    
from random import randint

printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

contact1 = Contact()
contact1.set_email_address('dumbledore@example.com')
contact1.set_first_name('Albus')

contact2 = Contact()
contact2.set_email_address('snape@example.com')
contact2.set_first_name('Severus')

import_data = []
import_data.append(contact1)
import_data.append(contact2)

contact_lists = constantcontact.get_lists()

for l in contact_lists:
    if l.get_name().lower() == 'general interest':
        general_interest = [l.get_id()]
    elif l.get_name().lower() == 'test list 1':
        test_list = [l.get_id()]

columns = ['EMAIL', 'FIRST NAME']

print '[test] import_contacts'
response = constantcontact.import_contacts(import_data, general_interest, columns)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] remove_contacts'
for i in range(len(import_data)):
    import_data[i].pop('first_name', None)
response = constantcontact.remove_contacts(import_data, test_list)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] clear_contact_lists'
response = constantcontact.clear_contact_lists(test_list)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] export_contacts'
response = constantcontact.export_contacts(columns, general_interest)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

export_activity_id = response.get_id()

print '[test] activity_status_report'
response = constantcontact.activities_status_report()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] individual_activity_status'
response = constantcontact.individual_activity_status(export_activity_id)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')
 
file_name = 'Put a completed export files activity url here'

print '[test] get_export_file'
response = constantcontact.get_export_file(file_name)
if printout and response:
    print response.content
    raw_input('press enter for next test')

multipart_activity = Multipart_Activity()

multipart_activity.set_data(open('multipart_import.csv', 'rb'))
multipart_activity.set_file_name('multipart_import_test'+str(randint(1000000, 9999999))+'.csv')
multipart_activity.set_lists(general_interest[0])

print '[test] multipart_import'
response = constantcontact.multipart_import_contacts(multipart_activity)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

multipart_activity.set_data(open('multipart_remove.csv', 'rb'))
multipart_activity.set_file_name('multipart_remove_test'+str(randint(1000000, 9999999))+'.csv')

print '[test] multipart_remove'
response = constantcontact.multipart_remove_contacts(multipart_activity)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')


