from event.Event import Event


def read_all_events():
    result = []
    with open('events.txt', 'r') as events:
        for line in events.readlines():
            split = line.split(" ")
            result.append(Event(split[0], split[1], split[2], split[3]))
    return result
