import json

class AbstractChatBot(object):
    data = []  
 
    def __init__(self):
        self.conversations = []
        pass

    def num_conversations(self):
        return len(self.conversations)
    
    def new_conversation(self):
        self.conversations.append([])
        return len(self.conversations) - 1

    def get_conversation(self, uid):
        return self.conversations[uid]

    def process(self, json_file):
        data = json.loads(json_file)
        print('Process some json file')
    def query(self, query):
        print('Accepted a query string', query)
        found = False
        for convo in data:
            for  message in convo:
                if found:
                    return message['text']
                found = query in message['text']
                   
       
        return 'Nothing'


class BasicChatBot(AbstractChatBot):
    def __init__(self):
        super()

    def process(self, json_file):
        with open(json_file) as coded_data:
            data = json.load(coded_data)
           
    def query(self, conversation_uid, query):
        self.conversations[conversation_uid].append(query)
        response = 'Basic Chat Bot says shut up, I dont want to anwser the question:' + query
        self.conversations[conversation_uid].append(response)
        return response
