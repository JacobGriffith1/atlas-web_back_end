const assert = require('assert');
const calculateNumber = require('./2-calcul_chai.js');

describe('add', () => {
    const calcType = 'SUM';


    it('Numbers not rounded', () => {
        const result = calculateNumber(calcType, 1, 3);
        expect(result).to.equal(4);
    });

    it('Number rounded up', () => {
        const result = calculateNumber(calcType, 1, 3.7);
        expect(result).to.equal(5);
    });

    it('Numbers round down and up', () => {
        const result = calculateNumber(calcType, 1.2, 3.7);
        expect(result).to.equal(5);
    });

    it('Numbers both round up', () => {
        const result = calculateNumber(calcType, 1.5, 3.7);
        expect(result).to.equal(6);
    });

    it('Numbers both round down', () => {
        const result = calculateNumber(calcType, 1.4, 3.2);
        expect(result).to.equal(4);
    });
});

describe('sub', () => {
    const calcType = 'SUBTRACT';

    it('Numbers not rounded', () => {
        const result = calculateNumber(calcType, 5, 3);
        expect(result).to.equal(2);
    });

    it('Number rounded up', () => {
        const result = calculateNumber(calcType, 8, 3.7);
        expect(result).to.equal(4);
    });

    it('Numbers round down and up', () => {
        const result = calculateNumber(calcType, 10.2, 3.7);
        expect(result).to.equal(6);
    });

    it('Numbers both round up', () => {
        const result = calculateNumber(calcType, 9.5, 3.7);
        expect(result).to.equal(6);
    });

    it('Numbers both round down', () => {
        const result = calculateNumber(calcType, 5.4, 3.2);
        expect(result).to.equal(2);
    });
});

describe('div', () => {
    const calcType = 'DIVIDE';


    it('Numbers not rounded', () => {
        const result = calculateNumber(calcType, 1, 2);
        expect(result).to.equal(0.5);
    });

    it('Number rounded up', () => {
        const result = calculateNumber(calcType, 1, 3.7);
        expect(result).to.equal(0.25);
    });

    it('Numbers round down and up', () => {
        const result = calculateNumber(calcType, 1.2, 3.7);
        expect(result).to.equal(0.25);
    });

    it('Numbers both round up', () => {
        const result = calculateNumber(calcType, 1.5, 3.7);
        expect(result).to.equal(0.5);
    });

    it('Numbers both round down', () => {
        const result = calculateNumber(calcType, 1.4, 4.2);
        expect(result).to.equal(0.25);
    });

    it('Zero test case', () => {
        const result = calculateNumber(calcType, 5, 0);
        expect(result).to.equal('Error');
    });
});