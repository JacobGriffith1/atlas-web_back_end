const Utils = require('./utils.js');
const sinon = require('sinon');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    const paymentSum = Utils.calculateNumber('SUM', totalAmount, totalShipping);
    console.log(`The total is: ${paymentSum}`);
}

module.exports = sendPaymentRequestToApi;