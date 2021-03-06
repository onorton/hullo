import extract_facebook
import extract_google
import json
import operator
import functools
from extract_linguistics import Linguistics

def extract_data(facebook, google):
    data = []
    if(facebook and facebook != 'None'):
    	data.append(extract_facebook.get_Json(facebook))
    if(google and google != 'None'):
        data.append(extract_google.get_Json(google))
    return join_data(data)

def join_data(data):
    return functools.reduce(operator.add, [], data)


def write_file(messages, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        f.write(messages)

def add_linguistics(data):
    l = Linguistics()
    for k, v in data.items():
        pass
    return data

def convert_for_ml(filename):
    strings = []
    with open(filename, 'r') as f:
        data = json.load(f)
        for convo in data:
            for message in convo['messages']:
                if('content' in message):
                    strings.append(message['content'])

    return strings

def main(linguistics=False):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Facebook chat HTML file")
    parser.add_argument("google", help="Google hangouts")
    parser.add_argument("outfile", default="data/message_data.json" , help="output JSON file")
    args = parser.parse_args()

    messages = extract_data(args.infile, args.google)

    if(linguistics):
        messages = add_linguistics(messages)
 
    write_file(json.dumps(messages, indent=2), args.outfile)


if __name__ == '__main__':
    main()



