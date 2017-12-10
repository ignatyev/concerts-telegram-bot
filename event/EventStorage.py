import json

from event.Event import Event


def read_all_events():
    result = []
    events = open('events.txt', 'r')
    json_loads = json.load(events)
    for json_load in json_loads:
        event = Event(None, None, None, None)
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
