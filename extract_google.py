import csv
from collections import OrderedDict
import json


def read_file(file):
    """Read a text file and return its contents as a list of lines"""
    with open(file, 'r', encoding = 'utf-8') as f:
        contents = f.readlines()
    return contents


def extract_google(json_list):
    """Extract a Google Hangouts JSON file to a list of dicts"""
    json_text = ' '.join(json_list)
    json_dict = json.loads(json_text)
    
    people = dict()
    messages = list()
    
    for i, conversation in enumerate(json_dict['conversation_state']):
        for person in conversation['conversation_state']['conversation']['participant_data']:
            person_id = person['id']['chat_id']
            people[person_id] = person.get('fallback_name', '')
        for j, message in enumerate(conversation['conversation_state']['event']):
            text = message.get('chat_message', {}).get('message_content', {}).get('segment', [{}])[0].get('text', None)
            if text:
                text = text.replace('\r\n', ' ')
                text = text.replace('\n', ' ')
            timestamp = message['timestamp']
            sender_id = message['sender_id']['chat_id']
            sender = people.get(sender_id, '')
            messages.append(OrderedDict([('thread', i), 
                                         ('message', j), 
                                         ('sender', sender), 
                                         ('timestamp', timestamp), 
                                         ('text', text)]))
    
    return messages


def write_file(messages, file):
    """Write messages to CSV"""
    with open(file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in messages:
            writer.writerow([value for value in line.values()])


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Google Hangouts JSON file")
    parser.add_argument("outfile", help="output CSV file")
    args = parser.parse_args()
    
    contents = read_file(args.infile)
    
    messages = extract_google(contents)
    
    write_file(messages, args.outfile)


if __name__ == '__main__':
    main()