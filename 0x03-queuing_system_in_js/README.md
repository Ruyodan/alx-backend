# 0x03. Queuing System in JS
#### `Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

![1486e02a78cdf7b4557c](https://github.com/samuelselasi/alx-backend/assets/85158665/097e8d98-a1d8-4880-9a08-dd0819320f55)

## Resources
### Read or watch:

* [Redis quick start](https://redis.io/docs/install/install-redis/)
* [Redis client interface](https://redis.io/docs/connect/cli/)
* [Redis client for Node JS](https://github.com/redis/node-redis)
* [Kue](https://github.com/Automattic/kue) *deprecated but still use in the industry*

## Requirements
* All of your code will be compiled/interpreted on Ubuntu `18.04`, `Node 12.x`, and `Redis 5.0.7`
* All of your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `js` extension

## Required Files for the Project
### [package.json](./package.json)
### [.babelrc](./.babelrc)
### and...
**Don’t forget to run `$ npm install` when you have the `package.json`**

## Tasks

[0. Install a redis instance](./dump.rdb)

Download, extract, and compile the latest stable `Redis` version (higher than `5.0.7` - [https://redis.io/download/](https://redis.io/download/)):
```
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
```
* Start Redis in the background with `src/redis-server`
```
src/redis-server &
```
* Make sure that the server is working with a ping `src/redis-cli ping`
```
PONG
```
* Using the Redis client again, set the value `School` for the key `Holberton`
```
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
```
* Kill the server with the process id of the redis-server (hint: use `ps` and `grep`)
```
$ kill [PID_OF_Redis_Server]
```
Copy the `dump.rdb` from the `redis-5.0.7` directory into the root of the Queuing project.

### Requirements:

* Running `get Holberton` in the client, should return `School`


[1. Node Redis Client](./0-redis_client.js)

Install [node_redis](https://github.com/redis/node-redis) using `npm`

Using `Babel` and `ES6`, write a script named `0-redis_client.js`. It should connect to the Redis server running on your machine:

* It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly
* It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work

### Requirements:

* To import the library, you need to use the keyword `import`
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

[2. Node Redis client and basic operations](./1-redis_op.js)

In a file `1-redis_op.js`, copy the code you previously wrote (`0-redis_client.js`).

**Add two functions**:

* `setNewSchool`:
	* It accepts two arguments `schoolName`, and `value.`
	* It should set in Redis the value for the key `schoolName`
	* It should display a confirmation message using `redis.print`
* `displaySchoolValue`:
	* It accepts one argument `schoolName.`
	* It should log to the console the `value` for the `key` passed as argument

**At the end of the file, call**:

* `displaySchoolValue('Holberton');`
* `setNewSchool('HolbertonSanFrancisco', '100');`
* `displaySchoolValue('HolbertonSanFrancisco');`

### Requirements:

* Use `callbacks` for any of the operation, we will look at `async` operations later
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

[3. Node Redis client and async operations](./2-redis_op_async.js)

In a file `2-redis_op_async.js`, let’s copy the code from the previous exercise (`1-redis_op.js`)

Using `promisify`, modify the function `displaySchoolValue` to use ES6 `async / await`

Same result as `1-redis_op.js`
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

[4. Node Redis client and advanced operations](./4-redis_advanced_op.js)

In a file named `4-redis_advanced_op.js`, let’s use the client to store a hash value

### Create Hash:
Using `hset`, let’s store the following:

* The key of the hash should be `HolbertonSchools`
* It should have a value for:
	* `Portland=50`
	* `Seattle=80`
	* `New York=20`
	* `Bogota=20`
	* `Cali=40`
	* `Paris=2`
* Make sure you use `redis.print` for each `hset`

### Display Hash:
Using `hgetall`, display the object stored in Redis. It should return the following:

### Requirements:

* Use `callbacks` for any of the operation, we will look at `async` operations later
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

