// 2-redis_op_async.js
import { createClient, print } from 'redis';
import { promisify } from 'util'


const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // redis.print
}

// Promisify 'get' method
const getAsync = promisify(client.get).bind(client);

// Async displaySchoolValue
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName); // Await results from Redis
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving key ${schoolName}: ${err.message}`);
  }
}


displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
