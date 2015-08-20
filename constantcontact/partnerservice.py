from .baseservice import BaseService

from .components import Billing_Plan, Partner_Account, Result_Set

from datetime import datetime

class PartnerService(BaseService):
    # Partner services endpoints
    def get_partner_accounts(self, limit = 50):
        queries = {}
        queries['limit'] = limit
        
        response = self.request('get', 'partner/accounts', params = queries)
        try:
            response['results']
        except:
            return response
        # Convert dict to Components
        for i in range(len(response['results'])):
            response['results'][i] = Partner_Account(response['results'][i])
        return Result_Set(response)

    def post_partner_accounts(self, account, token = False):
        return Partner_Account(self.request('post', 'partner/accounts', params = {'oauth2_token_provided': token}, body = account))
    
    def get_partner_billing_plan(self, partner_id):
        partner_id = self.partner_to_id(partner_id)
        return Billing_Plan(self.request('get', 'partner/accounts/'+partner_id+'/plan'))
    
    def update_partner_billing_plan(self, partner_id, plan):
        partner_id = self.partner_to_id(partner_id)
        return Billing_Plan(self.request('put', 'partner/accounts/'+partner_id+'/plan', body = plan))

    def cancel_account(self, partner_id, cancel_reason = None):
        body = {'status': 'Cancelled'}
        if cancel_reason:
            body['cancel_reason'] = cancel_reason
        date = datetime.now().isoformat().split('T', 1)[0]
        body['cancel_date'] = date

        partner_id = self.partner_to_id(partner_id)

        return self.request('put', 'partner/accounts/'+partner_id+'/status', body = body)

    def partner_to_id(self, partner_id):
        if type(partner_id) is Partner_Account:
            partner_id = partner_id.get_id()
        return partner_id


