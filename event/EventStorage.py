import json

import os

from event.Event import Event

EVENTS_TXT = 'events.txt'


def read_all_events():
    result = []
    if os.stat(EVENTS_TXT).st_size > 0:
        events = open(EVENTS_TXT, 'r')
        json_loads = json.load(events)
        for json_load in json_loads:
            event = Event(None, None, None, None, None)
            event.__dict__.update(json_load)
            result.append(event)
        events.close()
    return result


def save_events(events):
    dumps_list = []
    for event in events:
        dumps_list.append(event.__dict__)
    events_file = open('events.txt', 'w')
    json.dump(dumps_list, events_file)
    events_file.close()


def save_event(event):
    all_events = read_all_events()
    all_events.append(event)
    save_events(all_events)
