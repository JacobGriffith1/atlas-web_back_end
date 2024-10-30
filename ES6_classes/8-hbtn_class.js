export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](cls) {
    if (cls === 'number') {
      return this._size;
    }
    if (cls === 'string') {
      return this._location;
    }
    return this;
  }
}
