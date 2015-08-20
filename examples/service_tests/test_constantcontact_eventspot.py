from constantcontact import ConstantContact, Attribute, Contact, Event, Fee, Item, Promocode

from datetime import datetime, timedelta
from random import randint

import json
    
printout = True

creds_file = open('creds.txt', 'r')
access_token = creds_file.readline().replace('\n', '')
api_key = creds_file.readline().replace('\n', '')
api_url = creds_file.readline().replace('\n', '')

constantcontact = ConstantContact(api_key, access_token, api_url)

print '[test] get_events'
response = constantcontact.get_events(limit = 3)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

start_date = (datetime.now() + timedelta(hours=6)).replace(minute=0)
end_date = (datetime.now() + timedelta(days=5)).replace(minute=0)

verified_email_address = constantcontact.get_verified_email_addresses('CONFIRMED')[0]['email_address']

contact = Contact()
contact.set_email_address(verified_email_address)
contact.set_first_name('Bob')
contact.set_company_name('Justice League')
contact.set_work_phone('8675309')

event = Event()
event.set_end_date(end_date.isoformat())
event.set_name('Test event '+str(randint(1000000, 9999999)))
event.set_title('please ignore')
event.set_contact(contact)
event.set_location('THE SECRET MOONBASE')
event.set_time_zone_id('US/Eastern')
event.set_type('OTHER')
event.set_start_date(start_date.isoformat())

print '[test] post_events'
response = constantcontact.post_events(event)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

event_response = response
print event_response.get_id()

print '[test] get_event'
response = constantcontact.get_event(event_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

event_response.set_name('Updated '+event_response.get_name())

print '[test] update_event'
response = constantcontact.update_event(event_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] patch_event'
response = constantcontact.patch_event(event_response, 'ACTIVE')
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

fee = Fee()
fee.set_fee(10)
fee.set_fee_scope('BOTH')
fee.set_label('Entrance Fee')
fee.set_early_fee(9)
fee.set_late_fee(11)

print '[test] post_event_fees'
response = constantcontact.post_event_fees(event_response, fee)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_event_fees'
response = constantcontact.get_event_fees(event_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

fee_response = response[0]

print '[test] get_event_fee'
response = constantcontact.get_event_fee(event_response, fee_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

fee_response.set_fee(5)

print '[test] update_event_fee'
response = constantcontact.update_event_fee(event_response, fee_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_event_fee'
response = constantcontact.delete_event_fee(event_response, fee_response)
if printout and response:
    print response
    raw_input('press enter for next test')

pc = Promocode()

pc.set_code_name('Test_Code')
pc.set_code_type('DISCOUNT')
pc.set_discount_percent(10)
pc.set_discount_scope('ORDER_TOTAL')
pc.set_is_paused(False)
pc.set_quantity_total(-1)

print '[test] post_event_promocodes'
response = constantcontact.post_event_promocodes(event_response, pc)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_event_promocodes'
response = constantcontact.get_event_promocodes(event_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

pc_response = response[0]

print '[test] get_event_promocode'
response = constantcontact.get_event_promocode(event_response, pc_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

pc_response.set_discount_percent(15)

print '[test] update_event_promocode'
response = constantcontact.update_event_promocode(event_response, pc_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_event_promocode'
response = constantcontact.delete_event_promocode(event_response, pc_response)
if printout and response:
    print response
    raw_input('press enter for next test')

item = Item()
item.set_default_quantity_total(10)
item.set_name('Cauldrons')
item.set_per_registrant_limit(1)
item.set_price(4)

print '[test] post_event_items'
response = constantcontact.post_event_items(event_response, item)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_event_items'
response = constantcontact.get_event_items(event_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

item_response = response[0]

print '[test] get_event_item'
response = constantcontact.get_event_item(event_response, item_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

item_response.set_price(3)

print '[test] update_event_item'
response = constantcontact.update_event_item(event_response, item_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

attr = Attribute()
attr.set_name('Bewitching')
attr.set_quantity_total(10)

print '[test] post_event_item_attributes'
response = constantcontact.post_event_item_attributes(event_response, item_response, attr)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] get_event_item_attrbutes'
response = constantcontact.get_event_item_attributes(event_response, item_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

attr_response = response[0]

print '[test] get_event_item_attrbute'
response = constantcontact.get_event_item_attribute(event_response, item_response, attr_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

attr_response.set_name('Alchemy')

print '[test] update_event_item_attribute'
response = constantcontact.update_event_item_attribute(event_response, item_response, attr_response)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

print '[test] delete_event_item_attribute'
response = constantcontact.delete_event_item_attribute(event_response, item_response, attr_response)
if printout and response:
    print response
    raw_input('press enter for next test')

print '[test] delete_event_item'
response = constantcontact.delete_event_item(event_response, item_response)
if printout and response:
    print response
    raw_input('press enter for next test')

event_id_with_registrants = 'Insert an id for an event with registrants'

print '[test] get_event_registrants'
response = constantcontact.get_event_registrants(event_id_with_registrants)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')

registrant = response.get_item(0)

print '[test] get_event_registrant'
response = constantcontact.get_event_registrant(event_id_with_registrants, registrant)
if printout and response:
    print json.dumps(response, indent = 4, sort_keys = True)
    raw_input('press enter for next test')



