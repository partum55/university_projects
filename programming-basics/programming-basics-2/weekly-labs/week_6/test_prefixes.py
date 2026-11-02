import unittest
from all_prefixes import all_prefixes

class TestPrefixes(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(all_prefixes(""), set())
    def test_lead(self):
        self.assertEqual(all_prefixes("lead"), {"l", "le", "lea", "lead"})
    def test_worker(self):
        self.assertEqual(all_prefixes("worker"), {"w", "wo", "wor", "work", "worke", "worker"})
    def test_mime(self):
        self.assertEqual(all_prefixes("mime"), {"m", "mi", "mim", "mime"})
    def test_checkmates(self):
        self.assertEqual(all_prefixes("checkmates"), {"c", "ch", "che", "chec", "check", "checkm", "checkma", "checkmat", "checkmate", "checkmates"})
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
