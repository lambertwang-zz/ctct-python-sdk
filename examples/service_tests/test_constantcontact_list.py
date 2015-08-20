from constantcontact import ConstantContact

import json
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

print '[test] post_lists'
response = constantcontact.post_lists('Test List 213')
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_lists'
response = constantcontact.get_lists()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

for l in response:
    if l.get_name().lower() == 'test list 1':
        target_list = l
        break

print '[test] get_list'
response = constantcontact.get_list(target_list.get_id())
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

target_list.set_name('Test List 1235 new name')

print '[test] update_list'
response = constantcontact.update_list(target_list)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_list_contacts'
response = constantcontact.get_list_contacts(target_list.get_id())
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_list'
response = constantcontact.delete_list(target_list.get_id())
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')
    