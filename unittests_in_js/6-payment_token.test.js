const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token.js');

describe('getPaymentTokenFromAPI', () => {

    it('Correct data sent', (done) => {
        getPaymentTokenFromAPI(true)
        .then((result) => {
            const expected = { data: 'Successful response from the API' };
            expect(result).to.deep.equal(expected);
            done();
        })
        .catch(done);
    });

});