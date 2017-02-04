'use strict';

var _ = require('lodash');

var rp = require('request-promise');


function Conversation() { }

Conversation.prototype.converse = 
  function(message) {
   return 'what\'s up';
  };

module.exports = Conversation;
