from .baseservice import BaseService

from .components import Account_Info, Email_Address

class AccountService(BaseService):
    # Account services endpoints
    def get_account_info(self):
        return Account_Info(self.request('get', 'account/info'))
        
    def update_account_info(self, account_info):
        account_info = self.validate_account_info(account_info)
        return Account_Info(self.request('put', 'account/info', body = account_info))

    # Email addresses are returned as standard python objects rather than a Result_Set containing Email_Address components
    def get_verified_email_addresses(self, status = 'ALL'):
        return self.request('get', 'account/verifiedemailaddresses', params = {'status': status})

    def post_verified_email_addresses(self, email):
        if type(email) is Email_Address:
            email = email.get_email_address()
        return self.request('post', 'account/verifiedemailaddresses', body = [{'email_address': email}])

    def validate_account_info(self, account_info):
        if type(account_info) is dict:
            account_info = Account_Info(account_info)
        if type(account_info) is not Account_Info:
            raise TypeError('invalid type for account_info: '+type(account_info).__name__)
            
        return account_info

