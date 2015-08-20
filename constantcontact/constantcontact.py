##
# A simple python program utilizing the constant contact API
##

from .accountservice import AccountService
from .activityservice import ActivityService
from .contactservice import ContactService
from .emailmarketingservice import EmailMarketing
from .eventspotservice import EventSpotService
from .listservice import ListService
from .mylibraryservice import MyLibraryService
from .partnerservice import PartnerService

class ConstantContact:
    # The base url is the Constant Contact v2 API
    def __init__(self, client_id, token, base_url = 'https://api.constantcontact.com/v2'):
        self.__init_services__(client_id, token, base_url)

    def __init_services__(self, client_id, token, base_url):
        # Initialize services
        self.account_service = AccountService(client_id, token, base_url)
        self.emailmarketing_service = EmailMarketing(client_id, token, base_url)
        self.mylibrary_service = MyLibraryService(client_id, token, base_url)
        self.activity_service = ActivityService(client_id, token, base_url)
        self.contact_service = ContactService(client_id, token, base_url)
        self.list_service = ListService(client_id, token, base_url)
        self.partner_service = PartnerService(client_id, token, base_url)
        self.eventspot_service = EventSpotService(client_id, token, base_url)

    # Token info endpoint
    def get_token_info(self):
        return self.account_service.token_info()

    # Account services endpoints
    def get_account_info(self):
        return self.account_service.get_account_info()
    def update_account_info(self, account_info):
        return self.account_service.update_account_info(account_info)
    def get_verified_email_addresses(self, status = 'ALL'):
        return self.account_service.get_verified_email_addresses(status)
    def post_verified_email_addresses(self, email):
        return self.account_service.post_verified_email_addresses(email)

    # Email Marketing Endpoints
    def get_campaigns(self, limit = 50, modified_since = None, status = 'ALL'):
        return self.emailmarketing_service.get_campaigns(limit, modified_since, status)
    def post_campaigns(self, campaign):
        return self.emailmarketing_service.post_campaigns(campaign)
    def get_campaign(self, campaign_id, updateSummary = False):
        return self.emailmarketing_service.get_campaign(campaign_id, updateSummary)
    def update_campaign(self, campaign):
        return self.emailmarketing_service.update_campaign(campaign)
    def delete_campaign(self, campaign_id):
        return self.emailmarketing_service.delete_campaign(campaign_id)

    def test_send_campaign(self, campaign_id, email_addresses, format, personal_message):
        return self.emailmarketing_service.test_send_campaign(campaign_id, email_addresses, format, personal_message)
    def preview_campaign(self, campaign_id):
        return self.emailmarketing_service.preview_campaign(campaign_id)

    def get_campaign_schedules(self, campaign_id):
        return self.emailmarketing_service.get_campaign_schedules(campaign_id)
    def post_campaign_schedules(self, campaign_id, schedule):
        return self.emailmarketing_service.post_campaign_schedules(campaign_id, schedule)
    def get_campaign_schedule(self, campaign_id, schedule_id):
        return self.emailmarketing_service.get_campaign_schedule(campaign_id, schedule_id)
    def update_campaign_schedule(self, campaign_id, schedule):
        return self.emailmarketing_service.update_campaign_schedule(campaign_id, schedule)
    def delete_campaign_schedule(self, campaign_id, schedule_id):
        return self.emailmarketing_service.delete_campaign_schedule(campaign_id, schedule_id)

    def get_campaign_summary_report(self, campaign_id, updateSummary = False):
        return self.emailmarketing_service.get_campaign_summary_report(campaign_id, updateSummary)
    def get_campaign_bounces(self, campaign_id, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_bounces(campaign_id, created_since, limit)
    def get_campaign_clicks(self, campaign_id, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_clicks(campaign_id, created_since, limit)
    def get_campaign_forwards(self, campaign_id, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_forwards(campaign_id, created_since, limit)
    def get_campaign_opens(self, campaign_id, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_opens(campaign_id, created_since, limit)
    def get_campaign_sends(self, campaign_id, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_sends(campaign_id, created_since, limit)
    def get_campaign_unsubscribes(self, campaign_id, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_unsubscribes(campaign_id, created_since, limit)
    def get_campaign_clicks_by_link_id(self, campaign_id, link_id = None, created_since = None, limit = 500):
        return self.emailmarketing_service.get_campaign_clicks_by_link_id(campaign_id, link_id, created_since, limit)

    # My Library Endpoints
    def get_files(self, limit = 50, sort_by = 'CREATED_DATE_DESC', source = 'ALL', file_type = 'ALL'):
        return self.mylibrary_service.get_files(limit, sort_by, source, file_type)
    def post_files(self, multipart_file):
        return self.mylibrary_service.post_files(multipart_file)
    def get_files_upload_status(self, file_ids):
        return self.mylibrary_service.get_files_upload_status(file_ids)
    def get_file(self, file_id):
        return self.mylibrary_service.get_file( file_id)
    def update_file(self, mylibrary_file, include_payload = True):
        return self.mylibrary_service.update_file(mylibrary_file, include_payload)
    def delete_file(self, file_id):
        return self.mylibrary_service.delete_file(file_id)

    def get_folders(self, limit = 50, sort_by = 'CREATED_DATE_DESC'):
        return self.mylibrary_service.get_folders(limit, sort_by)
    def post_folders(self, folder):
        return self.mylibrary_service.post_folders(folder)
    def get_folder(self, folder_id):
        return self.mylibrary_service.get_folder(folder_id)
    def update_folder(self, folder):
        return self.mylibrary_service.update_folder(folder)
    def delete_folder(self, folder_id):
        return self.mylibrary_service.delete_folder(folder_id)
    def get_folder_files(self, folder_id, limit = 50):
        return self.mylibrary_service.get_folder_files(folder_id, limit)
    def move_folder_files(self, folder_id, file_ids):
        return self.mylibrary_service.move_folder_files(folder_id, file_ids)

    def get_trash(self, limit = 50, sort_by = 'CREATED_DATE_DESC', file_type = 'ALL'):
        return self.mylibrary_service.get_trash(limit, sort_by, file_type)
    def delete_trash(self):
        return self.mylibrary_service.delete_trash()
    def get_mylibrary_info(self):
        return self.mylibrary_service.get_mylibrary_info()

    # Activity services endpoints
    def import_contacts(self, import_data, lists, columns):
        return self.activity_service.import_contacts(import_data, lists, columns)
    def remove_contacts(self, import_data, lists):
        return self.activity_service.remove_contacts(import_data, lists)
    def clear_contact_lists(self, lists):
        return self.activity_service.clear_contact_lists(lists)
    def export_contacts(self, columns, lists, sort_by = 'EMAIL_ADDRESS', file_type = 'CSV', export_added_by = False, export_date_added = False):
        return self.activity_service.export_contacts(columns, lists, sort_by, file_type, export_added_by, export_date_added)
    def get_export_file(self, file_name):
        return self.activity_service.get_export_file(file_name)
    def multipart_import_contacts(self, multipart_activity):
        return self.activity_service.multipart_import_contacts(multipart_activity)
    def multipart_remove_contacts(self, multipart_activity):
        return self.activity_service.multipart_remove_contacts(multipart_activity)
    def activities_status_report(self, type_query = None, status = 'ALL'):
        return self.activity_service.activities_status_report(type_query, status)
    def individual_activity_status(self, activity_id):
        return self.activity_service.individual_activity_status(activity_id)

    # Contacts services endpoints
    def get_contacts(self, email = None, limit = 50, modified_since = None, status = 'ALL'):
        return self.contact_service.get_contacts(email, limit, modified_since, status)
    def post_contacts(self, contact, action_by = 'ACTION_BY_OWNER'):
        return self.contact_service.post_contacts(contact, action_by)
    def get_contact(self, contact_id):
        return self.contact_service.get_contact(contact_id)
    def update_contact(self, contact, action_by = 'ACTION_BY_OWNER'):
        return self.contact_service.update_contact(contact, action_by)
    def delete_contact(self, contact_id):
        return self.contact_service.delete_contact(contact_id)

    # Contacts tracking endpoints
    def get_contact_tracking(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_tracking(contact_id, created_since, limit)
    def get_contact_tracking_summary(self, contact_id):
        return self.contact_service.get_contact_tracking_summary(contact_id)
    def get_contact_bounces(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_bounces(contact_id, created_since, limit)
    def get_contact_clicks(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_clicks(contact_id, created_since, limit)
    def get_contact_forwards(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_forwards(contact_id, created_since, limit)
    def get_contact_opens(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_opens(contact_id, created_since, limit)
    def get_contact_sends(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_sends(contact_id, created_since, limit)
    def get_contact_unsubscribes(self, contact_id, created_since = None, limit = 500):
        return self.contact_service.get_contact_unsubscribes(contact_id, created_since, limit)
    def get_contact_report_by_campaign(self, contact_id):
        return self.contact_service.get_contact_report_by_campaign(contact_id)
    
    # Contact List services endpoints
    def get_lists(self, modified_since = None):
        return self.list_service.get_lists(modified_since)
    def post_lists(self, list_name, status = 'ACTIVE'):
        return self.list_service.post_lists(list_name, status)
    def get_list(self, list_id):
        return self.list_service.get_list(list_id)
    def update_list(self, contact_list):
        return self.list_service.update_list(contact_list)
    def delete_list(self, list_id):
        return self.list_service.delete_list(list_id)
    def get_list_contacts(self, list_id, limit = 50, modified_since = None):
        return self.list_service.get_list_contacts(list_id, limit, modified_since)

    # Partner services endpoints
    def get_events(self, limit = 50):
        return self.eventspot_service.get_events(limit)
    def post_events(self, event):
        return self.eventspot_service.post_events(event)
    def get_event(self, event_id):
        return self.eventspot_service.get_event(event_id)
    def update_event(self, event):
        return self.eventspot_service.update_event(event)
    def patch_event(self, event_id, value):
        return self.eventspot_service.patch_event(event_id, value)

    def get_event_promocodes(self, event_id):
        return self.eventspot_service.get_event_promocodes(event_id)
    def post_event_promocodes(self, event_id, promocode):
        return self.eventspot_service.post_event_promocodes(event_id, promocode)
    def get_event_promocode(self, event_id, promocode_id):
        return self.eventspot_service.get_event_promocode(event_id, promocode_id)
    def update_event_promocode(self, event_id, promocode):
        return self.eventspot_service.update_event_promocode(event_id, promocode)
    def delete_event_promocode(self, event_id, promocode_id):
        return self.eventspot_service.delete_event_promocode(event_id, promocode_id)

    def get_event_fees(self, event_id):
        return self.eventspot_service.get_event_fees(event_id)
    def post_event_fees(self, event_id, fee):
        return self.eventspot_service.post_event_fees(event_id, fee)
    def get_event_fee(self, event_id, fee_id):
        return self.eventspot_service.get_event_fee(event_id, fee_id)
    def update_event_fee(self, event_id, fee):
        return self.eventspot_service.update_event_fee(event_id, fee)
    def delete_event_fee(self, event_id, fee_id):
        return self.eventspot_service.delete_event_fee(event_id, fee_id)

    def get_event_items(self, event_id):
        return self.eventspot_service.get_event_items(event_id)
    def post_event_items(self, event_id, item):
        return self.eventspot_service.post_event_items(event_id, item)
    def get_event_item(self, event_id, item_id):
        return self.eventspot_service.get_event_item(event_id, item_id)
    def update_event_item(self, event_id, item):
        return self.eventspot_service.update_event_item(event_id, item)
    def delete_event_item(self, event_id, item_id):
        return self.eventspot_service.delete_event_item(event_id, item_id)

    def get_event_item_attributes(self, event_id, item_id):
        return self.eventspot_service.get_event_item_attributes(event_id, item_id)
    def post_event_item_attributes(self, event_id, item_id, attribute):
        return self.eventspot_service.post_event_item_attributes(event_id, item_id, attribute)
    def get_event_item_attribute(self, event_id, item_id, attribute_id):
        return self.eventspot_service.get_event_item_attribute(event_id, item_id, attribute_id)
    def update_event_item_attribute(self, event_id, item_id, attribute):
        return self.eventspot_service.update_event_item_attribute(event_id, item_id, attribute)
    def delete_event_item_attribute(self, event_id, item_id, attribute_id):
        return self.eventspot_service.delete_event_item_attribute(event_id, item_id, attribute_id)

    def get_event_registrants(self, event_id, limit = 50):
        return self.eventspot_service.get_event_registrants(event_id, limit)
    def get_event_registrant(self, event_id, registrant_id):
        return self.eventspot_service.get_event_registrant(event_id, registrant_id)

    # Partner services endpoints
    def get_partner_accounts(self, limit = 50):
        return self.partner_service.get_partner_accounts(limit)
    def post_partner_accounts(self, account, token = False):
        return self.partner_service.post_partner_accounts(account, token)
    def get_partner_billing_plan(self, partner_id):
        return self.partner_service.get_partner_billing_plan(account_id)
    def update_partner_billing_plan(self, partner_id, plan):
        return self.partner_service.update_partner_billing_plan(account_id, plan)
    def cancel_account(self, partner_id):
        return self.partner_service.cancel_account(account_id)

    # Paginated results
    def next_page(self, page_uri):
        return self.account_service.next_page(page_uri)
