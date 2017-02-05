from bs4 import BeautifulSoup
import csv
from collections import OrderedDict
import time
import json

def read_file(file):
    """Read a text file and return its contents as a list of lines"""
    with open(file, 'r', encoding = 'utf-8') as f:
        contents = f.readlines()
    return contents
def get_Json(name): 
    contents = read_file(name)
    return json.loads(extract_facebook(contents))


def extract_facebook(html_list):
    """Extract a Facebook chat HTML file to a list of dicts"""
    
    html_str = " ".join(html_list)
    
    soup = BeautifulSoup(html_str, 'html.parser')
    
    messages = []
     
     
    for i, thread in enumerate(soup.find_all('div', class_='thread')):
        convo = {}
        convo['conversation_id'] = i
        convo_messages = []
        for j, message in enumerate(reversed(thread.find_all('div', class_='message'))):
            sender = message.find('span', class_='user').string
            timestamp = message.find('span', class_='meta').string
            if timestamp:
                timestamp = time.strptime(timestamp[:timestamp.rfind('C')+1], '%A, %d %B %Y at %H:%M %Z')
                timestamp = time.mktime(timestamp)
            text = message.next_sibling.string
            if text:
                text = text.replace('\r\n', ' ')
                text = text.replace('\n', ' ')
            message = {}
            message['message_id'] = j
            message['sender'] = sender
            message['timestamp'] = timestamp
            message['content'] = text
            message['understanding'] = {}
            convo_messages.append(message)
                                        
        convo['messages'] = convo_messages
        messages.append(convo)
    messages = json.dumps(messages)
    return messages


def write_file(messages, file):
    """Write messages to CSV"""
    with open(file, 'w', newline='', encoding='utf-8') as f:
        f.write(messages)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Facebook chat HTML file")
    parser.add_argument("outfile", help="output JSON file")
    args = parser.parse_args()
    
    contents = read_file(args.infile)
    
    messages = extract_facebook(contents)
    
    write_file(messages, args.outfile)



if __name__ == '__main__':
    main()
