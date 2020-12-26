from datetime import datetime

class ChatbotHelper():

    def get_event_index(self, tracker_event):
        i = len(tracker_event) - 1
        while i >= 0 and tracker_event[i]["event"] != "bot":
            i -= 1
        return i

class EventHelper():

    datetime_format = '%Y-%m-%d %H:%M:%S.%f'

    def get_events(self, event_list):
        data = []

        for row in event_list:
            if 'tanggal' in row and 'detail' in row:
                data.append(row)

        result = []

        if data:
            sorted_data = sorted(data, key=lambda k: datetime.strptime(k['tanggal'], self.datetime_format), reverse=True)
            for data in sorted_data[:5]:
                result.append('- {} - {}/{}/{}'.format(data['tanggal'],
                                                    data['detail']['nama'], 
                                                    data['detail']['jenis'], 
                                                    data['detail']['kategori'])) 
        
            return '\n\n'.join(result)

        return
