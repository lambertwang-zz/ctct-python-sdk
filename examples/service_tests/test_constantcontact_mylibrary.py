from constantcontact import ConstantContact

from constantcontact import Mylibrary_File, Mylibrary_Folder, Multipart_File

import json

from random import randint
import codecs
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

multipart = Multipart_File()

multipart.set_data(open('constant_contact_logo.png', 'rb'))
multipart.set_description('The Constant Contact logo')
multipart.set_file_name('Constant Contact logo'+str(randint(1000000, 9999999)))
multipart.set_file_type('PNG')
multipart.set_folder_id(0)
multipart.set_source('MyComputer')

print '[test] add_files'
response = constantcontact.post_files(multipart)
if printout and response:
    print response
    raw_input('press enter for next test')

print '[test] get_files'
response = constantcontact.get_files(limit = 2)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

all_files = response.get_set()

print '[test] get_files_upload_status'
response = constantcontact.get_files_upload_status(all_files)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_file'
response = constantcontact.get_file(all_files[0])
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

updated_file = all_files[0]
updated_file.set_name('Updated file name'+str(randint(1000000, 9999999)))

print '[test] update_file'
response = constantcontact.update_file(updated_file)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

new_folder = Mylibrary_Folder()
new_folder.set_name('test_folder'+str(randint(1000000, 9999999)))

print '[test] post_folders'
response = constantcontact.post_folders(new_folder)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

folder_response = response

print '[test] get_folders'
response = constantcontact.get_folders(limit = 4)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_folder'
response = constantcontact.get_folder(folder_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

folder_response.set_name('new_test_folder_name'+str(randint(1000000, 9999999)))

print '[test] update_folder'
response = constantcontact.update_folder(folder_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] move_folder_files'
response = constantcontact.move_folder_files(folder_response, all_files)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_folder_files'
response = constantcontact.get_folder_files(folder_response, limit = 5)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_files'
response = constantcontact.delete_file(updated_file)
if printout and response:
    print response
    raw_input('press enter for next test')
    
print '[test] delete_folders'
response = constantcontact.delete_folder(folder_response)
if printout and response:
    print response
    raw_input('press enter for next test')

print '[test] get_trash'
response = constantcontact.get_trash()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_trash'
response = constantcontact.delete_trash()
if printout and response:
    print response
    raw_input('press enter for next test')

print '[test] get_mylibrary_info'
response = constantcontact.get_mylibrary_info()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')




