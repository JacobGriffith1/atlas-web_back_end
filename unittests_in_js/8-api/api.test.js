const expect = require('chai').expect;
const request = require('request');

describe('Index page', () => {

    it('Status code check, default endpoint message', (done) => {
        request.get('http://localhost:7865', (error, response, body) => {
            if (error) return done(error);

            expect(response.statusCode).to.equal(200);
            const expected = 'Welcome to the payment system';

            expect(body).to.equal(expected);
            done();
        });
    });

});