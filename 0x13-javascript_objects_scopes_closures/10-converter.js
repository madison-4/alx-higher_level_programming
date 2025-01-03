#!/usr/bin/node
// a function to convert numbers to diff bases

exports.converter = function (base) {
  function convert (arg) {
    return parseInt(arg, 10).toString(base);
  }
  return convert;
};
