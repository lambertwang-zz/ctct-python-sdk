from constantcontact import ConstantContact, Account_Info

import json
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

print '[test] get_account_info'
response = constantcontact.get_account_info()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] put_account_info'
account_info = Account_Info()
account_info.set_phone('1234567890')
account_info.set_state_code('MA')

response = constantcontact.update_account_info(account_info)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_verified_email_addresses'
response = constantcontact.get_verified_email_addresses()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] post_verified_email_addresses'
response = constantcontact.post_verified_email_addresses('test@example.com')
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')
