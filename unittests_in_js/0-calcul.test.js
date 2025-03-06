const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('Calculator', () => {
    it('Numbers not rounded', () => {
        const result = calculateNumber(1, 3);
        assert.equal(result, 4);
    });

    it('Number rounded up', () => {
        const result = calculateNumber(1, 3.7);
        assert.equal(result, 5);
    });

    it('Numbers round down and up', () => {
        const result = calculateNumber(1.2, 3.7);
        assert.equal(result, 5);
    });

    it('Numbers both round up', () => {
        const result = calculateNumber(1.5, 3.7);
        assert.equal(result, 6);
    });
});