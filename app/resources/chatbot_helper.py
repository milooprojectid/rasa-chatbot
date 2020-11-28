class ChatbotHelper():

    def __init__(self):
        pass

    def get_event_index(self, tracker_event):
        i = len(tracker_event) - 1
        while i >= 0 and tracker_event[i]["event"] != "bot":
            i -= 1
        return i
