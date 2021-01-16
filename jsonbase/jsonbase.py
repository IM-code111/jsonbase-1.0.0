import os
from os import path
import json

class DatabaseError(Exception):
    pass

class DataError(Exception):
    pass

class database():
    """
    Put the name of database in the
    brakets
    """
    def __init__(self, database):
        self.db = database

    def create(self):
        """
        Creating a new database function
        """
        if path.exists(f'{self.db}.json'):
            raise DatabaseError('Database already exist')
        else:
            with open(f'{self.db}.json','w') as f:
                f.write("{}")
            return None

    def get(self):
        """
        Return all data from JSON database in dictionary
        """
        if not os.path.isfile(f'{self.db}.json'):
            raise DatabaseError('Database doesn\'t exist')
        else:
            with open(f'{self.db}.json','r') as f:
                data = json.load(f)
            return data

    def save(self, data):
        """
        Save data to JSON database
        Note: Only support dictionary
        """
        if not os.path.isfile(f'{self.db}.json'):
            raise DatabaseError('Database doesn\'t exist')
        else:
            with open(f'{self.db}.json','w') as f:
                json.dump(data, f)
            return data

    def remove(self):
        """
        Remove JSON database
        not the JSON database data
        """
        if not os.path.isfile(f'{self.db}.json'):
            raise DatabaseError('Database doesn\'t exist')
        else:
            os.remove(f'{self.db}.json')
            return None
        
    def rename(self, new_name):
        """
        Rename specific database
        """
        if not os.path.isfile(f'{self.db}.json'):
            raise DatabaseError('Database doesn\'t exist')
        else:
            os.rename(f'{self.db}.json',f'{new_name}.json')
            
    def swap(self, data1, data2):
        """
        Swap data value with other data value
        """
        if not os.path.isfile(f'{self.db}.json'):
            raise DatabaseError('Database doesn\'t exist')
        else:
            with open(f'{self.db}.json','r') as f:
                data = json.load(f)
            if data1 not in data or data2 not in data:
                raise DataError('Data not found')
            else:
                one = data[data1]
                two = data[data2]
                data[data1] = two
                data[data2] = one
                with open(f'{self.db}.json','w') as f:
                    json.dump(data, f)
                return data
    