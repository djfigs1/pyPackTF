import unittest, json

class CommunityPricesTests(unittest.TestCase):

    def setUp(self):
        from pyPackTF import CommunityPrices

        CP = CommunityPrices("N/A", offline=True)
        json_file = open('sample_json/community_prices.json', 'r')
        file_json = json.load(json_file)
        CP.loadJSON(file_json)

        self.CP = CP

    def test_CurrentTime(self):
        self.assertEqual(self.CP.getCurrentTime(), 1469643121)

    def test_IsValid(self):
        from pyPackTF import CommunityPrices

        CP = CommunityPrices("N/A", offline=True)
        json_file = open('sample_json/community_prices.json', 'r')
        file_json = json.load(json_file)
        CP.loadJSON(file_json)

        self.assertEqual(self.CP.isResponseSuccessful(), True)

    def test_FailureMessage(self):
        from pyPackTF import Exceptions

        with self.assertRaises(Exceptions.NoErrorMessage):
            self.CP.getMessage()

    def test_Item_Price(self):
        test_item = self.CP.getCommunityItems()[0]

        price = test_item.getPrice(6)
        self.assertEqual(type(price), float)

    def test_Item_Qualities(self):
        test_item = self.CP.getCommunityItems()[0]
        qualities = test_item.getQualities()

        self.assertEqual(len(qualities), 1)

    def test_Item_Defindex(self):
        test_item = self.CP.getCommunityItems()[0]
        defindex = test_item.getDefIndexes()

        self.assertEqual(defindex[0], 781)

    def test_Item_Difference(self):
        test_item = self.CP.getCommunityItems()[0]
        difference = test_item.getDifference(6)

        self.assertEqual(difference, -0.34)

    def test_Item_LastUpdated(self):
        test_item = self.CP.getCommunityItems()[0]
        last_updated = test_item.getLastUpdated(6)

        self.assertEqual(last_updated, 1459527840)

    def test_Item_Currency(self):
        test_item = self.CP.getCommunityItems()[0]
        currency = test_item.getCurrency(6)

        self.assertEqual(currency, "metal")