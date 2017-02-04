'use strict';
var Alexa = require("alexa-sdk");

exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.registerHandlers(handlers);
    alexa.execute();
};


var handlers = {
    
    'LaunchRequest': function () {
        this.emit(':ask', 'Talk to me.', 'Say something.');
    },
    'ChatIntent': function() {
        var message = this.event.request.intent.slots.Message.value;
        var respond = function(message) {return 'what\'s up.'}
        var response = respond(message);
        console.log(message);
        console.log(response);
        
	this.emit(":ask", response);
    },
    'SessionEndedRequest': function () {
        console.log('session ended!');
    },
    'Unhandled': function() {
        this.emit(':ask', 'Sorry, I didn\'t get that.');
    }
};

