import json

class AbstractChatBot(object):
 
    def __init__(self):
        self.conversations = []
        self.data = []
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
    def query(self, uid, q):
        print('Accepted a query string', q)
        found = False
  
        for convo in self.data:
            for  message in convo['messages']:
               if found:
                    response = message['content']
                    self.conversations[uid].append(response)
                    return response
               if (message['content'] == None):
                  continue
               found = q in message['content']
        return 'Nothing'


class BasicChatBot(AbstractChatBot):
    def __init__(self):
        super().__init__()

    def process(self, json_file):
        with open(json_file) as coded_data:
            self.data = json.loads(coded_data.read())
           
  #  def query(self, conversation_uid, query):
  #      self.conversations[conversation_uid].append(query)
  #      response = 'Basic Chat Bot says shut up, I dont want to anwser the question:' + query
  #      self.conversations[conversation_uid].append(response)
  #      return response
