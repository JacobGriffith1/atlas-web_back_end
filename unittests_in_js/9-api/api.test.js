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

    it('Cart endpoint handles integer IDs', (done) => {
        request.get('http://localhost:7865/cart/12', (error, response, body) => {
            if (error) return done(error);

            expect(response.statusCode).to.equal(200);
            const expected = 'Payment methods for cart 12';

            expect(body).to.equal(expected);
            done();
        });
    });

    it('Cart endpoint rejects non-integer IDs', (done) => {
        request.get('http://localhost:7865/cart/hello', (error, response, body) => {
            if (error) return done(error);

            expect(response.statusCode).to.equal(404);
            done();
        });
    });
    
});