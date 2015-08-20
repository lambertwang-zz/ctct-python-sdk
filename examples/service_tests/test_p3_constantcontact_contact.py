from constantcontact import ConstantContact, Contact
from random import randint

import json
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

test_email = 'test'+str(randint(1000000, 9999999))+'@example.com'

print('[test] get_contacts')
response = constantcontact.get_contacts(limit = 5)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

next_page = response.get_next_page()

print('[test] get_next_page')
response = constantcontact.next_page(next_page)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

contact_lists = constantcontact.get_lists()

for l in contact_lists:
    if l.get_name().lower() == 'general interest':
        list_id = l.get_id()
        break

print('[test] post_contacts')
contact = Contact()
contact.add_list_id(list_id)
contact.add_list_id('1481737116')
contact.set_email_address(test_email)
response = constantcontact.post_contacts(contact)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact by email')
response = constantcontact.get_contacts(email = test_email)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')
contact = response['results'][0]
contact_id = contact.get_id()

print('[test] get_contact')
response = constantcontact.get_contact(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] update_contact')
new_contact = Contact()
new_contact.set_first_name('updated contact name 2')
new_contact.set_email_address(test_email)
new_contact.set_lists(contact.get_lists())
new_contact.set_id(contact.get_id())
response = constantcontact.update_contact(new_contact)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_tracking')
response = constantcontact.get_contact_tracking(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_tracking_summary')
response =  constantcontact.get_contact_tracking_summary(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_bounces')
response = constantcontact.get_contact_bounces(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_clicks')
response = constantcontact.get_contact_clicks(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_forwards')
response = constantcontact.get_contact_forwards(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_opens')
response = constantcontact.get_contact_opens(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_sends')
response =  constantcontact.get_contact_sends(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_unsubscribes')
response =  constantcontact.get_contact_unsubscribes(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] get_contact_report_by_campaign')
response =  constantcontact.get_contact_report_by_campaign(contact_id)
if printout and response:
    print(json.dumps(response, indent = 4, sort_keys = True))
    input('press enter for next test')

print('[test] delete_contact')
response = constantcontact.delete_contact(contact_id)
if printout and response:
    print(response)
