// 6-job_creator.js
import kue from 'kue';


const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

// Create job
const job = queue.create('push_notification_code', jobData);

// Save job to queue
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Failed to create job:', err);
  }
});

// On success
job.on('complete', () => {
  console.log('Notification job completed');
});

// On failure
job.on('failed', () => {
  console.log('Notification job failed');
});
