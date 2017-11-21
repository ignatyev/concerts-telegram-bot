from event.Event import Event


def read_all_events():
    result = []
    events = open('events.txt', 'r')
    for line in events.readlines():
        split = line.split(" ")
        result.append(Event(split[0], split[1], split[2], split[3]))
    events.close()
    return result


def save_event(event):
    print('saving event: ' + event)
    events = open('events.txt', 'a')
    events.write(event)
    events.write('\n')
    events.close()
