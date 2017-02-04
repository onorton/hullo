'use strict';
var Alexa = require("alexa-sdk");
var appId = ''; //'amzn1.echo-sdk-ams.app.your-skill-id';

exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.appId = appId;
    alexa.registerHandlers(handlers);
    alexa.execute();
};


var handlers = {
    'ChatIntent': function() {
        var message = this.event.request.intent.slots.Message.value;
        var respond = function(message) {return 'what\'s up.'}
        var response = respond(message);
        console.log(message);
        console.log(response);
            // With a callback, use the arrow function to preserve the correct 'this' context
        this.emit(":ask", response);
    },
    'SessionEndedRequest': function () {
        console.log('session ended!');
    },
    'Unhandled': function() {
        this.emit(':ask', 'Sorry, I didn\'t get that.');
    }
};

