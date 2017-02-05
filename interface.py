import json
import subprocess

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

class RNNChatBot(AbstractChatBot):
    def __init__(self, name):
        self.name = name
        super().__init__()

    # we already did our processing yonks ago
    def process(self, json_file):
        pass

    def query(self, uid, q):
        convo = self.get_conversation(uid)
        convo.append(q)

        jsons = ',\n'.join(json.dumps(msg, indent=2) for msg in convo) 
        jsons = leftpadlines(jsons, '      ')

        cmd = 'th sample.lua -checkpoint checkpoint.t7 -length 500 -start-from'

        result = subprocess.run([cmd, "'"+jsons+"'"], encoding='utf-8')

        try:
            text = result.stdout[len(jsons):]
            end = text.index('}')
            response = json.loads(text)
            convo.append(response)
            return response
        except ValueError:
            return { 'message_id': 1
                   , 'sender': self.name
                   , 'timestamp': ''
                   , 'content': 'I'm so confused!'
                   , 'understanding': {}
                   }
        
def leftpadlines(s, padding):
    return ('\n' + padding).join(s.split('\n'))
