import unittest
from in_memory_db import InMemoryDB, TransactionError

class TestInMemoryDB(unittest.TestCase):
    def setUp(self):
        self.db = InMemoryDB()
    
    def test_get_nonexistent_key(self):
        self.assertIsNone(self.db.get("A"))
    
    def test_put_without_transaction(self):
        with self.assertRaises(TransactionError):
            self.db.put("A", 5)
    
    def test_basic_transaction(self):
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.assertIsNone(self.db.get("A"))  # Not committed yet
        self.db.commit()
        self.assertEqual(self.db.get("A"), 5)
    
    def test_rollback(self):
        self.db.begin_transaction()
        self.db.put("B", 10)
        self.db.rollback()
        self.assertIsNone(self.db.get("B"))
    
    def test_multiple_updates_in_transaction(self):
        self.db.begin_transaction()
        self.db.put("A", 5)
        self.db.put("A", 6)
        self.db.commit()
        self.assertEqual(self.db.get("A"), 6)
    
    def test_commit_without_transaction(self):
        with self.assertRaises(TransactionError):
            self.db.commit()
    
    def test_rollback_without_transaction(self):
        with self.assertRaises(TransactionError):
            self.db.rollback()
    
    def test_nested_transaction_not_allowed(self):
        self.db.begin_transaction()
        with self.assertRaises(TransactionError):
            self.db.begin_transaction()

if __name__ == '__main__':
    unittest.main()