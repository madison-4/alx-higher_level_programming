#!/usr/bin/node
// a function that revereses a list

exports.esrever = function (list) {
    let place = [];
    for (let i = (list.length - 1); i >= 0; i--) {
       place.push(list[i]);
    }
    return place;
};
