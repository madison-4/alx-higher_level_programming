#!/usr/bin/node
// This is ti expport a function that uses a callback
/**
 * It executes the function the given number of times
 * It expports the given function
 */
exports.addmeMaybe = function (x, theFunction) {
  const num = parseInt(x);
  theFunction(num + 1);
};