import unittest

from constantcontact import Campaign, Tracking_Summary

class Test_Campaign(unittest.TestCase):
    def test_camp_init_from_dict(self):
        campaign = Campaign({'id': '123456', 'name': 'Name Goes Here'})

        self.assertEqual(campaign.get_name(), 'Name Goes Here')

    def test_camp_setter_getter(self):
        campaign = Campaign()

        campaign.set_name('Invade Russia')
        campaign.set_id('1234')

        self.assertEqual(campaign.get_status(), None)
        self.assertEqual(campaign.get_id(), '1234')
        self.assertEqual(campaign.get_name(), 'Invade Russia')

        campaign.delete_name()

        self.assertEqual(campaign.get_name(), None)

    def test_camp_sent_to_contact_lists(self):
        campaign = Campaign()

        campaign.add_sent_to_contact_lists('0')
        campaign.add_sent_to_contact_lists('1')
        campaign.add_sent_to_contact_lists('2')
        campaign.add_sent_to_contact_lists('3')
        campaign.add_sent_to_contact_lists('4')


        self.assertEqual(campaign.get_sent_to_contact_lists()[0]['id'], '0')
        self.assertEqual(campaign.get_sent_to_contact_lists()[2]['id'], '2')

        campaign.remove_sent_to_contact_lists(1)
        campaign.remove_sent_to_contact_lists_id('3')

        self.assertEqual(len(campaign.get_sent_to_contact_lists()), 3)

        campaign.clear_sent_to_contact_lists()

        self.assertEqual(campaign.get_sent_to_contact_lists(), None)

    def test_camp_tracking_summary(self):
        campaign = Campaign()
        tracking_summary = Tracking_Summary({'clicks': 123, 'opens': 456})

        self.assertEqual(campaign.get_tracking_summary(), None)

        campaign['tracking_summary'] = tracking_summary

        self.assertEqual(campaign.get_tracking_summary(), Tracking_Summary({'clicks': 123, 'opens': 456}))

        campaign.delete_tracking_summary()

        self.assertEqual(campaign.get_tracking_summary(), None)

if __name__ == '__main__':
    unittest.main()
