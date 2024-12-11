# In-Memory Database with Transaction Support

This project implements an in-memory key-value database that supports atomic transactions. The database allows for operations to be grouped into transactions that can either be committed or rolled back, ensuring data consistency.

## Features

- In-memory key-value storage
- Transaction support with commit and rollback capabilities
- String keys and integer values
- Atomic operations
- Comprehensive test suite

## Setup and Installation

1. Ensure you have Python 3.6+ installed on your system
2. Clone this repository
3. No additional dependencies are required

## Running the Code

To run the tests:
```bash
python -m unittest test_in_memory_db.py
```

To use the database in your own code:
```python
from in_memory_db import InMemoryDB

# Create a new database instance
db = InMemoryDB()

# Start a transaction
db.begin_transaction()

# Make some changes
db.put("key1", 100)
db.put("key2", 200)

# Commit the changes
db.commit()

# Read values
value1 = db.get("key1")  # Returns 100
value2 = db.get("key2")  # Returns 200
```

## Future Assignment Improvements

1. Add support for concurrent transactions using isolation levels (READ COMMITTED, REPEATABLE READ, etc.) to make it more realistic.
2. Include requirements for performance benchmarking and optimization tasks to teach students about database efficiency.
3. Add error handling requirements for edge cases like maximum key length, value range limits, and storage capacity.
4. Require students to implement additional database operations like delete(), update(), and list_keys() to make it more comprehensive.
5. Include a section on implementing persistence to disk, teaching students about durability in ACID properties.

## Implementation Details

The implementation uses two dictionaries:
- `main_storage`: Stores the committed data
- `transaction_storage`: Temporarily stores changes made during a transaction

Changes made in a transaction are only visible after commit. Rollback discards all changes made in the current transaction.