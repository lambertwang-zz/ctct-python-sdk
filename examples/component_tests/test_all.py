import unittest

if __name__ == '__main__':
    try:
        exec('print \'Python 2\'')
    except:
        print('Python 3')

    # Generally, tests for simple components, like Activity_Report, Address, and Email_Address are not necessary.
    from test_account_info import Test_Account_Info
    from test_campaign import Test_Campaign
    from test_contact import Test_Contact
    from test_event import Test_Event
    from test_item import Test_Item
    from test_promocode import Test_Promocode
    from test_result_set import Test_Result_Set

    unittest.main()