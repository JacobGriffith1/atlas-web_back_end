export default function updateUniqueItems() {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  map.array.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });
}
