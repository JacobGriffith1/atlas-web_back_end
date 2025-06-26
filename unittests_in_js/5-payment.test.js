const sandbox = require('sinon').createSandbox();
const sendPaymentRequestToApi = require('./5-payment.js');
const Utils = require('./utils.js');

describe('Payment tests', () => {
    let spy;

    beforeEach(() => {
        spy = sandbox.spy(console, 'log');
    });

    afterEach(() => {
        sandbox.restore();
    });

    it('Check Utils: 100, 20', () => {
        const testAmount = 100, testShipping = 20;

        sendPaymentRequestToApi(testAmount, testShipping);
        sandbox.assert.calledOnceWithExactly(spy, 'The total is: 120');
    });

    it('Check Utils: 10, 10', () => {
        const testAmount = 10, testShipping = 10;

        sendPaymentRequestToApi(testAmount, testShipping);
        sandbox.assert.calledOnceWithExactly(spy, 'The total is: 20');
    });
});