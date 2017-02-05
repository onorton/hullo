import json
from flask_cors import CORS, cross_origin
from interface import BasicChatBot

from flask import Flask, url_for, request, abort
app = Flask(__name__)
CORS(app)
chat_bot = BasicChatBot()
chat_bot.process('data/message_data.json')

@app.route('/conversation')
def new_conversation():
    uid = chat_bot.new_conversation()
    return uid, 201

@app.route('/conversation/<int:uid>', methods=['GET', 'POST'])
def conversation(uid):
    if not 0 <= uid < chat_bot.num_conversations():
        abort(404)
    if request.method == 'GET':
        return json.dumps(chat_bot.get_conversation(uid))
    elif request.method == 'POST':
        
        req = request.data.decode('utf-8')
        return chat_bot.query(uid, req)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
