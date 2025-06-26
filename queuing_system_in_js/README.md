# Queueing System in JS
Project for Atlas School

## Learning Objectives
At the end of this project, be able to explain
- How to run a redis server
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and a queue

## Requirements
- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension

# Tasks

## 0. Install a Redis Instance
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/downloads/):
```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```
- Start Redis in the background with ```src/redis-server```
```
$ src/redis-server &
```
- Make sure that the server is working with a ping ```src/redis-cli ping```
```
PONG
```
- Using the Redis client again, set the value ```School``` for the key ```Holberton```
```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```
- Kill the server with the process id of the redis-server (hint: use ```ps``` and ```grep```)
```
$ kill [PID_OF_Redis_Server]
```
Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

Requirements:
- Running ```get Holberton``` in the client, should return ```School```

## 1. Node Redis Client
Install node_redis using npm

Using Babel and ES6, write a script named ```0-redis_client.js```. It should connect to the Redis server running on your machine:
- It should log to the console the message ```Redis client connected to the server``` when the connection to Redis works correctly
- It should log to the console the message ```Redis client not connected to the server: ERROR_MESSAGE``` when the connection to Redis does not work

Requirements:

- To import the library, you need to use the keyword ```import```
```
bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$ 
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
```

## 2. Node Redis Client and Basic Operations
In a file ```1-redis_op.js```, copy the code you previously wrote (```0-redis_client.js```).

Add two functions:

- ```setNewSchool```:
    - It accepts two arguments ```schoolName```, and ```value```.
    - It should set in Redis the value for the key ```schoolName```
    - It should display a confirmation message using ```redis.print```
- ```displaySchoolValue```:
    - It accepts one argument ```schoolName```.
    - It should log to the console the value for the key passed as argument
At the end of the file, call:

- ```displaySchoolValue('Holberton');```
- ```setNewSchool('HolbertonSanFrancisco', '100');```
- ```displaySchoolValue('HolbertonSanFrancisco');```
Requirements:

- Use callbacks for any of the operation, we will look at async operations later
```
bob@dylan:~$ npm run dev 1-redis_op.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
```

## 3. Node Redis Client and Async Operations
In a file ```2-redis_op_async.js```, let’s copy the code from the previous exercise (```1-redis_op.js```)

Using ```promisify```, modify the function ```displaySchoolValue``` to use ES6 ```async / await```

Same result as ```1-redis_op.js```

```
bob@dylan:~$ npm run dev 2-redis_op_async.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "2-redis_op_async.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
```

## 4. Node Redis Client and Advanced Operations
In a file named ```4-redis_advanced_op.js```, let’s use the client to store a hash value

<b>Create Hash:</b>
Using ```hset```, let’s store the following:

- The key of the hash should be ```HolbertonSchools```
- It should have a value for:
    - ```Portland=50```
    - ```Seattle=80```
    - ```New York=20```
    - ```Bogota=20```
    - ```Cali=40```
    - ```Paris=2```
- Make sure you use ```redis.print``` for each ```hset```

<b>Display Hash:</b>
Using ```hgetall```, display the object stored in Redis. It should return the following:

Requirements:

- Use callbacks for any of the operation, we will look at async operations later

```
bob@dylan:~$ npm run dev 4-redis_advanced_op.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
bob@dylan:~$
```

## 5. Node Redis Client Publisher and Subscriber
In a file named ```5-subscriber.js```, create a redis client:

- On connect, it should log the message ```Redis client connected to the server```
- On error, it should log the message ```Redis client not connected to the server: ERROR MESSAGE```
- It should subscribe to the channel ```holberton school channel```
- When it receives message on the channel ```holberton school channel```, it should log the message to the console
- When the message is ```KILL_SERVER```, it should unsubscribe and quit
In a file named ```5-publisher.js```, create a redis client:

- On connect, it should log the message ```Redis client connected to the server```
- On error, it should log the message ```Redis client not connected to the server: ERROR MESSAGE```
- Write a function named ```publishMessage```:
    - It will take two arguments: ```message``` (string), and ```time``` (integer - in ms)
    - After ```time``` millisecond:
        - The function should log to the console ```About to send MESSAGE```
        - The function should publish to the channel ```holberton school channel```, the message passed in argument after the time passed in arguments
- At the end of the file, call:
```
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
```
Requirements
- You only need one Redis server to execute the program
- You will need to have two node processes to run each script at the same time

Terminal 1:
```
bob@dylan:~$ npm run dev 5-subscriber.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-subscriber.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server
```

Terminal 2:
```
bob@dylan:~$ npm run dev 5-publisher.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-publisher.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
bob@dylan:~$ 
```

And in the same time in Terminal 1:
```
Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
[nodemon] clean exit - waiting for changes before restart
^C
bob@dylan:~$ 
```
Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call “background workers”.

## 6. Create the Job Creator


## 7. Create the Job Processor


## 8. Track Progress and Errors with Kue: Create the Job Creator


## 9. Track Progress and Errors with Kue: Create the Job Processor


## 10. Writing the Job Creation Function


## 11. Writing the Test for Job Creation


## 12. Set Up the Utils and Functions


## 13. List the Available Products


## 14. Create the Connection with Redis


## 15. Display the Current Stock for a Specific Item


## 16. In Stock?


## 17. An Express Application and Kue

