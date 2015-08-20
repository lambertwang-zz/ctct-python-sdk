from constantcontact import ConstantContact, Billing_Plan, Partner_Account, Result_Set
from random import randint

import json
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

number = randint(0, 10000000)
phone = str(randint(100, 999))+'-'+str(randint(100, 999))+'-'+str(randint(1000, 9999))

account = Partner_Account()
account.set_username('testpartner'+str(number))
account.set_organization_name('Illuminati')
account.set_first_name('Please Help')
account.set_last_name('I\'m trapped in a software factory')
account.set_email('test'+str(number)+'@example.com')
account.set_phone(phone)
account.set_state_code('MA')
account.set_password(str(number))
account.set_country_code('US')
# TODO: Test with a real partner API key

print '[test] post_partner_accounts'
response = constantcontact.post_partner_accounts(account)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_partner_accounts'
response = constantcontact.get_partner_accounts(limit = 5)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

account = response.get_item(0)

print '[test] get_partner_billing_plan'
response = constantcontact.get_partner_accounts(account)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

plan = Billing_Plan()
plan.set_plan_type(2)

print '[test] put_partner_billing_plan'
response = constantcontact.get_partner_accounts(account, plan)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] cancel_account'
response = constantcontact.cancel_account(account)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

