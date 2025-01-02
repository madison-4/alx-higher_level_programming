#!/usr/bin/node
// a function that searches the number of occurrences in ana lement

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(elem => {
    if (elem === searchElement) {
      count++;
    }
  });
  return (count);
};
