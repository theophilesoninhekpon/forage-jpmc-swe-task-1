import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      if (quote['stock'] == 'ABC'):
        self.assertEqual(getDataPoint(quote), ('ABC', 120.48, 121.2, 120.84))
      elif (quote['stock'] == 'DEF'):
        self.assertEqual(getDataPoint(quote), ('DEF', 117.87, 121.68, 119.775))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      if (quote['stock'] == 'ABC'):
        self.assertEqual(getRatio(quote['top_bid']['price'], quote['top_ask']['price']), 1.010738255033557)
      elif (quote['stock'] == 'DEF'):
        self.assertEqual(getRatio(quote['top_bid']['price'], quote['top_ask']['price']), 0.9686883629191322)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
