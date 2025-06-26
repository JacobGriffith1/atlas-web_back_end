const expect = require('chai').expect;
const request = require('request');
const { response } = require('./api');

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

            expect(response.statusCode).to.eq(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('Cart endpoint rejects non-integer IDs', (done) => {
        request.get('http://localhost:7865/cart/hello', (error, response, body) => {
            expect(response.statusCode).to.eq(404);
            done();
        });
    });
    
    it('Cart endpoint rejects floats', (done) => {
        request.get('http://localhost:7865/cart/3.14', (error, response, body) => {
            expect(response.statusCode).to.eq(404)
            done();
        });
    });
});

describe('Available Payments endpoint', () => {
  it('GET /available_payments returns correct payment methods object', (done) => {
    request.get({
      url: 'http://localhost:7865/available_payments',
      json: true
    }, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
      done();
    });
  });
});

describe('Login endpoint', () => {
  it('POST /login with userName returns welcome message', (done) => {
    request.post({
      url: 'http://localhost:7865/login',
      json: { userName: 'Bingus' }
    }, (error, response, body) => {
      if (error) return done(error);
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome Bingus');
      done();
    });
  });
});