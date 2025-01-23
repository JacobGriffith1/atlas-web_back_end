# Caching
Project for Atlas School

## Learning Objectives
At the end of this project, understand:
- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- The purpose of a caching system
- What limits caching systems have

## Tasks

## 0. Basic Dictionary
Create a class ```BasicCache``` that inherits from ```BaseCaching``` and is a caching system:
- You must use ```self.cache_data``` - dictionary from the parent class ```BaseCaching```
- This caching system doesn't have a limit
- ```def put(self, key, item):```
    - Must assign to the dictionary ```self.cache_data``` the ```item``` value for the key ```key```.
    - ```def get(self, key):```
        - Must return the value in ```self.cache_data``` linked to ```key```.
        - If ```key``` is ```None``` or if the ```key``` doesn't exist in ```self.cache_data```, return ```None```.

## 1. FIFO Caching
Create a class ```FIFOCache``` that inherits from ```BaseCaching``` and is a caching system:
- You must use ```self.cache_data``` - dictionary from parent class ```BaseCaching```
- You can overload ```def __init__(self):``` but don't forget to call the parent init: ```super().__init__()```
- ```def put(self, key, item):```
    - Must assign to the dictionary ```self.cache_data``` the ```item``` value for the key ```key```.
    - If ```key``` or ```item``` is ```None```, this method should not do anything.
    - If the number of items in ```self.cache_data``` is higher than ```BaseCaching.MAX_ITEMS```:
        - You must discard the first item put in cache (FIFO algorithm)
        - You must print ```DISCARD:``` with the ```key``` discarded, followed by a newline
- ```def get(self, key):```
    - Must return the value in ```self.cache_data``` linked to ```key```.
    - If ```key``` is ```None``` or if the ```key``` doesn't exist in ```self.cache_data```, return ```None```.

## 2. LIFO Caching
Create a class ```LIFOCache``` that inherits from ```BaseCaching``` and is a caching system:
- You must use ```self.cache_data``` - dictionary from parent class ```BaseCaching```
- You can overload ```def __init__(self):``` but don't forget to call the parent init: ```super().__init__()```
- ```def put(self, key, item):```
    - Must assign to the dictionary ```self.cache_data``` the ```item``` value for the key ```key```.
    - If ```key``` or ```item``` is ```None```, this method should not do anything.
    - If the number of items in ```self.cache_data``` is higher than ```BaseCaching.MAX_ITEMS```:
        - You must discard the last item put in cache (LIFO algorithm)
        - You must print ```DISCARD:``` with the ```key``` discarded, followed by a newline
- ```def get(self, key):```
    - Must return the value in ```self.cache_data``` linked to ```key```.
    - If ```key``` is ```None``` or if the ```key``` doesn't exist in ```self.cache_data```, return ```None```.

## 3. LRU Caching
Create a class ```LRUCache``` that inherits from ```BaseCaching``` and is a caching system:
- You must use ```self.cache_data``` - dictionary from parent class ```BaseCaching```
- You can overload ```def __init__(self):``` but don't forget to call the parent init: ```super().__init__()```
- ```def put(self, key, item):```
    - Must assign to the dictionary ```self.cache_data``` the ```item``` value for the key ```key```.
    - If ```key``` or ```item``` is ```None```, this method should not do anything.
    - If the number of items in ```self.cache_data``` is higher than ```BaseCaching.MAX_ITEMS```:
        - You must discard the least recently used item (LRU algorithm)
        - You must print ```DISCARD:``` with the ```key``` discarded, followed by a newline
- ```def get(self, key):```
    - Must return the value in ```self.cache_data``` linked to ```key```.
    - If ```key``` is ```None``` or if the ```key``` doesn't exist in ```self.cache_data```, return ```None```.

## 4. MRU Caching
Create a class ```MRUCache``` that inherits from ```BaseCaching``` and is a caching system:
- You must use ```self.cache_data``` - dictionary from parent class ```BaseCaching```
- You can overload ```def __init__(self):``` but don't forget to call the parent init: ```super().__init__()```
- ```def put(self, key, item):```
    - Must assign to the dictionary ```self.cache_data``` the ```item``` value for the key ```key```.
    - If ```key``` or ```item``` is ```None```, this method should not do anything.
    - If the number of items in ```self.cache_data``` is higher than ```BaseCaching.MAX_ITEMS```:
        - You must discard the most recently used item (MRU algorithm)
        - You must print ```DISCARD:``` with the ```key``` discarded, followed by a newline
- ```def get(self, key):```
    - Must return the value in ```self.cache_data``` linked to ```key```.
    - If ```key``` is ```None``` or if the ```key``` doesn't exist in ```self.cache_data```, return ```None```.
