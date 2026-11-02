import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket


class TestFlower(unittest.TestCase):
    def test_flower_valid_zero_values(self):
        flower = Flower("blue", 0, 0)
        self.assertEqual(flower.color, "blue")
        self.assertEqual(flower.petals, 0)
        self.assertEqual(flower.price, 0)

    def test_flower_valid(self):
        flower = Flower("blue", 5, 10)
        self.assertEqual(flower.color, "blue")
        self.assertEqual(flower.petals, 5)
        self.assertEqual(flower.price, 10)

    def test_flower_invalid_color(self):
        with self.assertRaises(ValueError):
            Flower(123, 5, 10)

    def test_flower_invalid_petals(self):
        with self.assertRaises(ValueError):
            Flower("yellow", -1, 10)
        with self.assertRaises(ValueError):
            Flower("yellow", "many", 10)

    def test_flower_invalid_price(self):
        with self.assertRaises(ValueError):
            Flower("yellow", 5, -10)
        with self.assertRaises(ValueError):
            Flower("yellow", 5, "cheap")

    def test_tulip(self):
        tulip = Tulip(6, 15)
        self.assertEqual(tulip.color, "pink")
        self.assertEqual(tulip.petals, 6)
        self.assertEqual(tulip.price, 15)

    def test_rose(self):
        rose = Rose(8, 20)
        self.assertEqual(rose.color, "red")
        self.assertEqual(rose.petals, 8)
        self.assertEqual(rose.price, 20)

    def test_chamomile(self):
        chamomile = Chamomile(12, 5)
        self.assertEqual(chamomile.color, "white")
        self.assertEqual(chamomile.petals, 12)
        self.assertEqual(chamomile.price, 5)

    def test_flower_set_empty(self):
        flower_set = FlowerSet()
        self.assertEqual(flower_set.total_price(), 0)

    def test_flower_set_add_and_total(self):
        flower_set = FlowerSet()
        flower1 = Flower("blue", 5, 10)
        flower2 = Tulip(3, 20)
        flower_set.add_flower(flower1)
        flower_set.add_flower(flower2)
        self.assertEqual(flower_set.total_price(), 30)

    def test_flower_set_add_invalid(self):
        flower_set = FlowerSet()
        with self.assertRaises(ValueError):
            flower_set.add_flower("not a flower")

    def test_bucket_empty(self):
        bucket = Bucket()
        self.assertEqual(bucket.total_price(), 0)

    def test_bucket_total_price(self):
        fs1 = FlowerSet()
        fs1.add_flower(Tulip(5, 10))
        fs1.add_flower(Rose(7, 15))
        fs2 = FlowerSet()
        fs2.add_flower(Chamomile(10, 5))
        fs2.add_flower(Flower("violet", 4, 12))
        bucket = Bucket()
        bucket.add_set(fs1)
        bucket.add_set(fs2)
        self.assertEqual(bucket.total_price(), 42)

    def test_bucket_add_invalid(self):
        bucket = Bucket()
        with self.assertRaises(ValueError):
            bucket.add_set("not a flower set")

    def test_independence_of_instances(self):
        fs1 = FlowerSet()
        fs2 = FlowerSet()
        fs1.add_flower(Tulip(4, 10))
        fs2.add_flower(Rose(6, 15))
        bucket1 = Bucket()
        bucket2 = Bucket()
        bucket1.add_set(fs1)
        bucket2.add_set(fs2)
        self.assertEqual(bucket1.total_price(), 10)
        self.assertEqual(bucket2.total_price(), 15)
        self.assertNotEqual(bucket1.total_price(), bucket2.total_price())


if __name__ == '__main__':
    unittest.main()
