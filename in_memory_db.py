class TransactionError(Exception):
    """Custom exception for transaction-related errors"""
    pass

class InMemoryDB:
    def __init__(self):
        self.main_storage = {}  # Main database storage
        self.transaction_storage = None  # Transaction buffer
        self.transaction_in_progress = False
    
    def get(self, key: str) -> int:
        """
        Get the value for a key from the database.
        Returns None if the key doesn't exist.
        """
        # Only return from main storage - transaction changes are not visible
        # until committed
        return self.main_storage.get(key)
    
    def put(self, key: str, val: int) -> None:
        """
        Store a key-value pair in the database.
        Raises TransactionError if no transaction is in progress.
        """
        if not self.transaction_in_progress:
            raise TransactionError("No transaction in progress")
        
        # Store in transaction buffer only
        self.transaction_storage[key] = val
    
    def begin_transaction(self) -> None:
        """
        Start a new transaction.
        Raises TransactionError if a transaction is already in progress.
        """
        if self.transaction_in_progress:
            raise TransactionError("Transaction already in progress")
        
        self.transaction_in_progress = True
        self.transaction_storage = {}
    
    def commit(self) -> None:
        """
        Commit the current transaction.
        Raises TransactionError if no transaction is in progress.
        """
        if not self.transaction_in_progress:
            raise TransactionError("No transaction in progress")
        
        # Apply changes from transaction to main storage
        self.main_storage.update(self.transaction_storage)
        self._end_transaction()
    
    def rollback(self) -> None:
        """
        Rollback the current transaction.
        Raises TransactionError if no transaction is in progress.
        """
        if not self.transaction_in_progress:
            raise TransactionError("No transaction in progress")
        
        self._end_transaction()
    
    def _end_transaction(self) -> None:
        """Helper method to clean up after a transaction"""
        self.transaction_storage = None
        self.transaction_in_progress = False