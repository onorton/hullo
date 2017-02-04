'use strict';
var chai = require('chai');

var chaiAsPromised = require('chai-as-promised');

chai.use(chaiAsPromised);

var expect = chai.expect;

var Conversation = require('../conversation');



describe('Conversation', function() {
  var subject = new Conversation();

  var airport_code;

  describe('#converse', function() {
 
    context('with valid entry', function() {
 
      it('returns expected response', function() {

        var message = 'hello';
        var response = 'what\'s up';

	var value = subject.converse(message).then(function(obj) {

	    return obj;

        });

	return expect(value).to.eventually.eq(response);

      });

    });

   });

});
