import requests as r
import json
import pprint


class Linguistics(object):

    def __init__(self):
        self.api = 'https://westus.api.cognitive.microsoft.com/linguistics/v1.0'

        self.headers = {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': '4eb8ed1d0e5043428b02fbbbf72f79a1',
        }
        self.analyzers = [
            '4fa79af1-f22c-408d-98bb-b7d7aeef7f04', 
            '22a6b758-420f-4745-8a3c-46835a67c0d2', 
            '08ea174b-bfdb-4e64-987e-602f85da7f72']
        self.body = {"language": "en"}
        # self.update_analyzers()
    
    def update_analyzers(self):
        ret = r.get(self.api+'/analyzers', headers=self.headers) 
        if(ret.status_code == 200):
            response = ret.json()
            self.analyzers = [ x["id"] for x in response ]
        print(self.analyzers)

    
    def analyse_text(self, text):
        self.body['analyzerIds'] = self.analyzers
        self.body['text'] = text
        ret = r.post(self.api+'/analyze', data=json.dumps(self.body), headers=self.headers)
        print(ret)
        if(ret.status_code==200):
            response = ret.json()
            for res in response:
                pp = pprint.PrettyPrinter(indent=2)
                pp.pprint(res)
        else:
            print(ret.text)
        



if __name__ == '__main__':
    l = Linguistics()
    l.analyse_text('Hello my name is mickey!! What is yours?')
