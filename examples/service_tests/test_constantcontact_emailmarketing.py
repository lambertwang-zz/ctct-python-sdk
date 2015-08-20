from constantcontact import ConstantContact, Campaign, Schedule
from random import randint

from datetime import datetime, timedelta

import json
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

print '[test] get_campaigns'
response = constantcontact.get_campaigns()
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

campaign = response.get_item(0).get_id()

for c in response.get_set():
    if c.get_status() == 'SENT':
        sent_campaign = c
        break

print '[test] get_campaign'
response = constantcontact.get_campaign(campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

verified_email = constantcontact.get_verified_email_addresses('CONFIRMED')[0]['email_address']

print '[test] add_campaign'
new_campaign = Campaign()
new_campaign.set_name('Test Campaign '+str(randint(10000000, 99999999)))
new_campaign.set_subject('Test Subject')
new_campaign.set_from_name('Skeletor')
new_campaign.set_from_email(verified_email)
new_campaign.set_reply_to_email(verified_email)
new_campaign.set_email_content('<html><body><h1>BEHOLD, THE POWER OF SKELETOR!</h1></body></html>')
new_campaign.set_text_content('Behold, the power of Skeletor!')

lists = constantcontact.get_lists()
for contact_list in lists:
    if contact_list.get_name().lower() == 'general interest':
        send_to = contact_list

new_campaign.add_sent_to_contact_lists(send_to)

response = constantcontact.post_campaigns(new_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')
new_id = response['id']
new_campaign = response

print '[test] update_campaign'
new_campaign.set_subject('Updated Test Subject')
response = constantcontact.update_campaign(new_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

# This endpoint will send out an email.
'''
print '[test] campaign_test_send'
response = constantcontact.test_send_campaign(new_campaign, [verified_email], 'HTML_AND_TEXT', 'python SDK test')
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')
'''

print '[test] preview_campaign'
response = constantcontact.preview_campaign(new_id)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

schedule = Schedule()
tomorrow = (datetime.now() + timedelta(days=1)).replace(minute=0)
schedule.set_scheduled_date(tomorrow.isoformat())

print '[test] post_campaign_schedule'
response = constantcontact.post_campaign_schedules(new_campaign, schedule)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

schedule = response

print '[test] get_campaign_schedules'
response = constantcontact.get_campaign_schedules(new_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_schedule'
response = constantcontact.get_campaign_schedule(new_campaign, schedule)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

tomorrowtomorrow = tomorrow + timedelta(days=1)
schedule.set_scheduled_date(tomorrowtomorrow.isoformat())

print '[test] update_campaign_schedule'
response = constantcontact.update_campaign_schedule(new_campaign, schedule)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_campaign_schedule'
response = constantcontact.delete_campaign_schedule(new_campaign, schedule)
if printout and response:
    print response
    raw_input('press enter for next test')

print '[test] get_campaign_summary'
response = constantcontact.get_campaign_summary_report(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_bounces'
response = constantcontact.get_campaign_bounces(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_clicks'
response = constantcontact.get_campaign_clicks(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_forwards'
response = constantcontact.get_campaign_forwards(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_opens'
response = constantcontact.get_campaign_opens(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_sends'
response = constantcontact.get_campaign_sends(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_unsubscribes'
response = constantcontact.get_campaign_unsubscribes(sent_campaign)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_campaign_clicks_by_link_id'
response = constantcontact.get_campaign_clicks_by_link_id(sent_campaign, '1')
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_campaigns'
response = constantcontact.delete_campaign(new_id)
if printout and response:
    print response
    raw_input('press enter for next test')
