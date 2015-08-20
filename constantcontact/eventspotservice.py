from .baseservice import BaseService

from .components import Attribute, Event, Fee, Item, Promocode, Registrant, Result_Set

class EventSpotService(BaseService):
    # EventSpot endpoints
    # Events Collection
    def get_events(self, limit = 50):
        queries = {}
        queries['limit'] = limit

        response = self.request('get', 'eventspot/events', params = queries)
        try:
            response['results']
        except:
            return response
        # Convert dict to Components
        for i in range(len(response['results'])):
            response['results'][i] = Event(response['results'][i])
        return Result_Set(response)
    def post_events(self, event):
        event = self.validate_event(event)
        return Event(self.request('post', 'eventspot/events', body = event))

    # Individual Event
    def get_event(self, event_id):
        event_id = self.event_to_id(event_id)
        return Event(self.request('get', 'eventspot/events/'+event_id))
    def update_event(self, event):
        event = self.validate_event(event)
        return Event(self.request('put', 'eventspot/events/'+event.get_id(), body = event))
    # Currently, only the REPLACE operation is supported and the status path value is allowed
    def patch_event(self, event_id, value):
        event_id = self.event_to_id(event_id)
        patch = [{'op': 'REPLACE', 'path': '#/status', 'value': value}]
        return Event(self.request('patch', 'eventspot/events/'+event_id, body = patch))
    
    # Event Fees
    # Returns a list of fees rather than a resultset of fees
    def get_event_fees(self, event_id):
        event_id = self.event_to_id(event_id)
        response = self.request('get', 'eventspot/events/'+event_id+'/fees')
        for i in range(len(response)):
            response[i] = Fee(response[i])
        return response
    def post_event_fees(self, event_id, fee):
        event_id = self.event_to_id(event_id)
        fee = self.validate_fee(fee)
        return Fee(self.request('post', 'eventspot/events/'+event_id+'/fees', body = fee))
    def get_event_fee(self, event_id, fee_id):
        event_id = self.event_to_id(event_id)
        fee_id = self.fee_to_id(fee_id)
        return Fee(self.request('get', 'eventspot/events/'+event_id+'/fees/'+fee_id))
    def update_event_fee(self, event_id, fee):
        event_id = self.event_to_id(event_id)
        fee = self.validate_fee(fee)
        return Fee(self.request('put', 'eventspot/events/'+event_id+'/fees/'+fee.get_id(), body = fee))
    def delete_event_fee(self, event_id, fee_id):
        event_id = self.event_to_id(event_id)
        fee_id = self.fee_to_id(fee_id)
        return self.request('delete', 'eventspot/events/'+event_id+'/fees/'+fee_id)
    
    def get_event_promocodes(self, event_id):
        event_id = self.event_to_id(event_id)
        response = self.request('get', 'eventspot/events/'+event_id+'/promocodes')
        for i in range(len(response)):
            response[i] = Promocode(response[i])
        return response
    def post_event_promocodes(self, event_id, promocode):
        event_id = self.event_to_id(event_id)
        promocode = self.validate_promocode(promocode)
        return Promocode(self.request('post', 'eventspot/events/'+event_id+'/promocodes', body = promocode))
    def get_event_promocode(self, event_id, promocode_id):
        event_id = self.event_to_id(event_id)
        promocode_id = self.promocode_to_id(promocode_id)
        return Promocode(self.request('get', 'eventspot/events/'+event_id+'/promocodes/'+promocode_id))
    def update_event_promocode(self, event_id, promocode):
        event_id = self.event_to_id(event_id)
        promocode = self.validate_promocode(promocode)
        return Promocode(self.request('put', 'eventspot/events/'+event_id+'/promocodes/'+promocode.get_id(), body = promocode))
    def delete_event_promocode(self, event_id, promocode_id):
        event_id = self.event_to_id(event_id)
        promocode_id = self.promocode_to_id(promocode_id)
        return self.request('delete', 'eventspot/events/'+event_id+'/promocodes/'+promocode_id)

    def get_event_items(self, event_id):
        event_id = self.event_to_id(event_id)
        response = self.request('get', 'eventspot/events/'+event_id+'/items')
        for i in range(len(response)):
            response[i] = Item(response[i])
        return response
    def post_event_items(self, event_id, item):
        event_id = self.event_to_id(event_id)
        item = self.validate_item(item)
        return Item(self.request('post', 'eventspot/events/'+event_id+'/items', body = item))
    def get_event_item(self, event_id, item_id):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        return Item(self.request('get', 'eventspot/events/'+event_id+'/items/'+item_id))
    def update_event_item(self, event_id, item):
        event_id = self.event_to_id(event_id)
        item = self.validate_item(item)
        return Item(self.request('put', 'eventspot/events/'+event_id+'/items/'+item.get_id(), body = item))
    def delete_event_item(self, event_id, item_id):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        return self.request('delete', 'eventspot/events/'+event_id+'/items/'+item_id)
    
    def get_event_item_attributes(self, event_id, item_id):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        response = self.request('get', 'eventspot/events/'+event_id+'/items/'+item_id+'/attributes')
        for i in range(len(response)):
            response[i] = Attribute(response[i])
        return response
    def post_event_item_attributes(self, event_id, item_id, attribute):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        attribute = self.validate_attribute(attribute)
        return Attribute(self.request('post', 'eventspot/events/'+event_id+'/items/'+item_id+'/attributes', body = attribute))
    def get_event_item_attribute(self, event_id, item_id, attribute_id):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        attribute_id = self.attribute_to_id(attribute_id)
        return Attribute(self.request('get', 'eventspot/events/'+event_id+'/items/'+item_id+'/attributes/'+attribute_id))
    def update_event_item_attribute(self, event_id, item_id, attribute):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        attribute = self.validate_attribute(attribute)
        return Attribute(self.request('put', 'eventspot/events/'+event_id+'/items/'+item_id+'/attributes/'+attribute.get_id(), body = attribute))
    def delete_event_item_attribute(self, event_id, item_id, attribute_id):
        event_id = self.event_to_id(event_id)
        item_id = self.item_to_id(item_id)
        attribute_id = self.attribute_to_id(attribute_id)
        return self.request('delete', 'eventspot/events/'+event_id+'/items/'+item_id+'/attributes/'+attribute_id)
    
    def get_event_registrants(self, event_id, limit = 50):
        queries = {}
        queries['limit'] = limit

        event_id = self.event_to_id(event_id)

        response = self.request('get', 'eventspot/events/'+event_id+'/registrants', params = queries)
        # Convert dict to Components
        for i in range(len(response['results'])):
            response['results'][i] = Registrant(response['results'][i])
        return Result_Set(response)

    def get_event_registrant(self, event_id, registrant_id):
        event_id = self.event_to_id(event_id)
        if type(registrant_id) is Registrant:
            registrant_id = registrant_id.get_id()
        return Registrant(self.request('get', 'eventspot/events/'+event_id+'/registrants/'+registrant_id))

    def validate_event(self, event):
        if type(event) is dict:
            event = Event(event)
        if type(event) is not Event:
            raise TypeError('invalid type for event: '+type(event).__name__)

        return event

    def validate_fee(self, fee):
        if type(fee) is dict:
            fee = Fee(fee)
        if type(fee) is not Fee:
            raise TypeError('invalid type for fee: '+type(fee).__name__)

        return fee

    def validate_promocode(self, promocode):
        if type(promocode) is dict:
            promocode = Promocode(promocode)
        if type(promocode) is not Promocode:
            raise TypeError('invalid type for promocode: '+type(promocode).__name__)

        return promocode

    def validate_item(self, item):
        if type(item) is dict:
            item = Item(item)
        if type(item) is not Item:
            raise TypeError('invalid type for item: '+type(item).__name__)

        return item

    def validate_attribute(self, attribute):
        if type(attribute) is dict:
            attribute = Attribute(attribute)
        if type(attribute) is not Attribute:
            raise TypeError('invalid type for attribute: '+type(attribute).__name__)

        return attribute

    def event_to_id(self, event_id):
        if type(event_id) is Event:
            event_id = event_id.get_id()
        return event_id

    def fee_to_id(self, fee_id):
        if type(fee_id) is Fee:
            fee_id = fee_id.get_id()
        return fee_id

    def promocode_to_id(self, promocode_id):
        if type(promocode_id) is Promocode:
            promocode_id = promocode_id.get_id()
        return promocode_id

    def item_to_id(self, item_id):
        if type(item_id) is Item:
            item_id = item_id.get_id()
        return item_id

    def attribute_to_id(self, attribute_id):
        if type(attribute_id) is Attribute:
            attribute_id = attribute_id.get_id()
        return attribute_id
