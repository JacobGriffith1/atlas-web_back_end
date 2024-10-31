export default function cleanSet(set, startString) {
  if (!set && !startString && !(set instanceof Set) && typeof startString !== 'string') {
    return '';
  }

  const vals = [];

  for (const value of set.values()) {
    if (typeof value === 'string' && value.startsWith(startString)) {
      const valSub = value.substring(startString.length);

      if (valSub && valSub !== value) {
        vals.push(valSub);
      }
    }
  }
  return vals.join('-');
}