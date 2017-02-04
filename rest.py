import json

from flask import Flask, url_for, request, abort
app = Flask(__name__)

conversations = []

@app.route('/conversation')
def new_conversation():
    conversations.append([])
    return url_for('conversation', uid=len(conversations) - 1), 201

@app.route('/conversation/<int:uid>', methods=['GET', 'POST'])
def conversation(uid):
    if not 0 <= uid < len(conversations):
        abort(404) 

    if request.method == 'GET':
        return json.dumps(conversations[uid])
    elif request.method == 'POST':
        conversations[uid].append(request.data.decode('utf-8'))
        response = 'hello'
        conversations[uid].append(response)
        return response

if __name__ == '__main__':
    app.run()
