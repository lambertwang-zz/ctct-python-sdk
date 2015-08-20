from .baseservice import BaseService

from .components import Activity_Report, Campaign, Email_Address, Result_Set, Schedule, Tracking_Summary

class EmailMarketing(BaseService):

    # Email Marketing Endpoints
    def get_campaigns(self, limit = 50, modified_since = None, status = 'ALL'):
        queries = {}

        if modified_since is not None:
            queries['modified_since'] = modified_since

        queries['status'] = status
        queries['limit'] = limit

        response = self.request('get', 'emailmarketing/campaigns', params = queries)
        try:
            response['results']
        except:
            return response
        for i in range(len(response['results'])):
            response['results'][i] = Campaign(response['results'][i])
        return Result_Set(response)

    def post_campaigns(self, campaign):
        campaign = self.validate_campaign(campaign)
        return Campaign(self.request('post', 'emailmarketing/campaigns', body = campaign))

    # Methods that are passed in a campaign_id will also accept a Campaign component.
    def get_campaign(self, campaign_id, updateSummary = False):
        queries = {}
        if updateSummary:
            queries[updateSummary] = 'true'

        campaign_id = self.campaign_to_id(campaign_id)
        return Campaign(self.request('get', 'emailmarketing/campaigns/'+campaign_id, params = queries))

    def update_campaign(self, campaign):
        campaign = self.validate_campaign(campaign)
        if not campaign.get_id():
            raise AttributeError('missing Campaign.id')
        return Campaign(self.request('put', 'emailmarketing/campaigns/'+campaign.get_id(), body = campaign))

    def delete_campaign(self, campaign_id):
        campaign_id = self.campaign_to_id(campaign_id)
        return self.request('delete', 'emailmarketing/campaigns/'+campaign_id)

    # Email Marketing Testing Endpoints
    # Accepts an array of strings or an array of Email_Addresses for email_addresses
    # Accepts strings for format and personal_message
    def test_send_campaign(self, campaign_id, email_addresses, format, personal_message):
        test_send_body = {}
        # Convert Email_Address to string
        for i in range(len(email_addresses)):
            if type(email_addresses[i]) is Email_Address:
                email_addresses[i] = email_addresses[i].get_email_address()

        test_send_body['email_addresses'] = email_addresses
        test_send_body['format'] = format.upper()
        test_send_body['personal_message'] = personal_message
        
        campaign_id = self.campaign_to_id(campaign_id)
        return self.request('post', 'emailmarketing/campaigns/'+campaign_id+'/tests', body = test_send_body)

    def preview_campaign(self, campaign_id):
        campaign_id = self.campaign_to_id(campaign_id)
        return self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/preview')

    # Email Marketing Scheduling Endpoints
    # Returns a list of schedules rather than a Result_Set
    def get_campaign_schedules(self, campaign_id):
        campaign_id = self.campaign_to_id(campaign_id)
        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/schedules')
        try:
            response['results']
        except:
            return response
        for i in range(len(response)):
            response[i] = Schedule(response[i])
        return response
    # Accepts an ISO-8601 date as a string or a Schedule component
    def post_campaign_schedules(self, campaign_id, schedule):
        campaign_id = self.campaign_to_id(campaign_id)
        if type(schedule) is str:
            schedule = {'scheduled_date': schedule}

        response = self.request('post', 'emailmarketing/campaigns/'+campaign_id+'/schedules', body = schedule)
        return Schedule(response)

    def get_campaign_schedule(self, campaign_id, schedule_id):
        campaign_id = self.campaign_to_id(campaign_id)
        schedule_id = self.schedule_to_id(schedule_id)
        return Schedule(self.request('get', 'emailmarketing/campaigns/' + campaign_id + '/schedules/' + schedule_id))

    def update_campaign_schedule(self, campaign_id, schedule):
        campaign_id = self.campaign_to_id(campaign_id)
        schedule = self.validate_schedule(schedule)
        return Schedule(self.request('put', 'emailmarketing/campaigns/'+campaign_id+'/schedules/'+schedule.get_id(), body = schedule))

    def delete_campaign_schedule(self, campaign_id, schedule_id):
        campaign_id = self.campaign_to_id(campaign_id)
        schedule_id = self.schedule_to_id(schedule_id)
        return self.request('delete', 'emailmarketing/campaigns/'+campaign_id+'/schedules/'+schedule_id)

    # Email Marketing Tracking Endpoints
    def get_campaign_summary_report(self, campaign_id, updateSummary = False):
        if updateSummary:
            queries = {'updateSummary': 'true'}
        else:
            queries = {'updateSummary': 'false'}
        campaign_id = self.campaign_to_id(campaign_id)
        return Tracking_Summary(self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/tracking/reports/summary', params = queries))
            
    def get_campaign_bounces(self, campaign_id, created_since = None, limit = 500):
        campaign_id = self.campaign_to_id(campaign_id)
        queries = self.tracking_queries(created_since, limit)

        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/tracking/bounces', params = queries)
        
        return self.tracking_result_set(response)

    def get_campaign_clicks(self, campaign_id, created_since = None, limit = 500):
        campaign_id = self.campaign_to_id(campaign_id)
        queries = self.tracking_queries(created_since, limit)

        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/tracking/clicks', params = queries)
        
        return self.tracking_result_set(response)

    def get_campaign_forwards(self, campaign_id, created_since = None, limit = 500):
        campaign_id = self.campaign_to_id(campaign_id)
        queries = self.tracking_queries(created_since, limit)
        
        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/tracking/forwards', params = queries)
        
        return self.tracking_result_set(response)

    def get_campaign_opens(self, campaign_id, created_since = None, limit = 500):
        campaign_id = self.campaign_to_id(campaign_id)
        queries = self.tracking_queries(created_since, limit)
        
        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id +'/tracking/opens', params = queries)
        
        return self.tracking_result_set(response)

    def get_campaign_sends(self, campaign_id, created_since = None, limit = 500):
        campaign_id = self.campaign_to_id(campaign_id)
        queries = self.tracking_queries(created_since, limit)
        
        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/tracking/sends', params = queries)
        
        return self.tracking_result_set(response)

    def get_campaign_unsubscribes(self, campaign_id, created_since = None, limit = 500):
        campaign_id = self.campaign_to_id(campaign_id)
        queries = self.tracking_queries(created_since, limit)
        
        response = self.request('get', 'emailmarketing/campaigns/'+campaign_id+'/tracking/unsubscribes', params = queries)

        return self.tracking_result_set(response)

    def get_campaign_clicks_by_link_id(self, campaign_id, link_id = None, created_since = None, limit = 500):
        queries = self.tracking_queries(created_since, limit)

        campaign_id = self.campaign_to_id(campaign_id)
        url = 'emailmarketing/campaigns/'+campaign_id+'/tracking/clicks'
        if link_id:
            url = url + '/' + link_id
        response = self.request('get', url, params = queries)

        return self.tracking_result_set(response)

    def campaign_to_id(self, campaign):
        if type(campaign) is Campaign:
            campaign = campaign.get_id()
        return campaign

    def schedule_to_id(self, schedule):
        if type(schedule) is Schedule:
            schedule = schedule.get_id()
        return schedule

    def validate_campaign(self, campaign):
        if type(campaign) is dict:
            campaign = Campaign(campaign)
        if type(campaign) is not Campaign:
            raise TypeError('invalid type for campaign: '+type(campaign).__name__)
        return campaign

    def validate_schedule(self, schedule):
        if type(schedule) is dict:
            schedule = Schedule(schedule)
        if type(schedule) is not Schedule:
            raise TypeError('invalid type for schedule: '+type(schedule).__name__)
        return schedule

    def tracking_queries(self, created_since, limit):
        queries = {}

        if created_since is not None:
            queries['created_since'] = created_since
        
        queries['limit'] = limit

        return queries

    def tracking_result_set(self, tracking_response):
        try:
            tracking_response['results']
        except:
            return tracking_response
        for i in range(len(tracking_response['results'])):
            tracking_response['results'][i] = Activity_Report(tracking_response['results'][i])
        return Result_Set(tracking_response)


