'use strict';

  module.change_code = 1;

  var _ = require('lodash');

  var Alexa = require('alexa-app');

  var app = new Alexa.app('conversation');

  var Conversation = require('./conversation');

  app.launch(function(req, res) {

  var prompt = 'Talk to me.';

  res.say(prompt).reprompt(prompt).shouldEndSession(false);

});

	app.intent('conversation', {

	 'slots': {

	    'MESSAGE': 'TEXT'

	  },

	  'utterances': ['{-|MESSAGE}']

	},

	 function(req, res) {

	    //get the slot

	    var message = req.slot('MESSAGE');

	    var reprompt = 'Tell me something.';

	if (_.isEmpty(message)) {

	      var prompt = 'I didn\'t hear anything.';

	      res.say(prompt).reprompt(reprompt).shouldEndSession(false);

	      return true;

	    } else {

	     var conversation = new Conversation();

	     var response = conversation.converse(message);

	     console.log(response);

	     res.say(response).send();


	      return false;

	    }

	  }

	);

exports.handler = function(event, context) {

};
module.exports = app;
