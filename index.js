'use strict';
var Alexa = require("alexa-sdk");
exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.registerHandlers(handlers);
    alexa.execute();
};

var unirest = require('unirest');

var handlers = {
    
    'LaunchRequest': function () {
        this.emit(':ask', 'Talk to me.', 'Say something.');
    },
    'ChatIntent': function() {
        var message = this.event.request.intent.slots.Message.value;
        var rep = '';
	unirest.post('http://34.250.6.241:5000')
	.header('Accept', 'application/json')
	.send({ "message": message })
	.end(function (res) {
             response = res.body
	});
        console.log(message);
        console.log(response);
        
	this.emit(":ask", response, response);
    },
    'SessionEndedRequest': function () {
        console.log('session ended!');
    },
    'Unhandled': function() {
        this.emit(':ask', 'Sorry, I didn\'t get that.');
    }
};

