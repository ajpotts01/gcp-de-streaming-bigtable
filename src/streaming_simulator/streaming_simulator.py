import datetime
import gzip
import os
import time

from pubsub.pub_sub_helper import PubSubHelper

class StreamingSimulator():
    TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    INPUT_PATH: str = '../data'

    publisher: PubSubHelper
    start_time: datetime
    first_obs_time: datetime

    def __init__(self, gcp_project: str, topic: str):
        self.publisher: PubSubHelper = PubSubHelper(
            gcp_project=gcp_project,
            topic=topic
        )

        self.publisher.topic_setup()        

    def get_timestamp(self, line: str) -> datetime:        
        line = line.decode('utf-8')

        timestamp = line.split(',')[0]
        return datetime.datetime.strptime(timestamp, self.TIME_FORMAT)
    
    def peek_timestamp(self, zip) -> datetime:
        pos = zip.tell()
        line = zip.readline()
        zip.seek(pos)
        return self.get_timestamp

    def start_sim(self):
        self.start_time: datetime = datetime.datetime.utcnow()

        input_files = os.listdir(self.INPUT_PATH)

        for next_file in input_files:
            with gzip.open(f'{self.INPUT_PATH}/{next_file}', 'rb') as file_ref:
                header = file_ref.readline() # Just done to skip the header
                self.first_obs_time: datetime = self.peek_timestamp(file_ref)
                self.run_sim(file_ref)
    
    def compute_sleep_secs(self, obs_time):
        time_elapsed_total: int = (datetime.datetime.utcnow() - self.start_time).seconds
        time_elapsed_sim = ((obs_time - self.first_obs_time).days * 86400.0 + (obs_time - self.first_obs_time).seconds) / self.speed_factor
        time_to_sleep = time_elapsed_sim - time_elapsed_total
        return time_to_sleep

    def run_sim(self, data):
        events_to_publish = list()

        for next_line in data:
            event_data = next_line
            obs_time: datetime = self.get_timestamp(event_data)

            if self.compute_sleep_secs(obs_time) > 1:
                self.publisher.topic_publish(events_to_publish)
                events_to_publish = list()

                time_to_sleep = self.compute_sleep_secs(obs_time)
                if time_to_sleep > 0:
                    time.sleep(time_to_sleep)

            events_to_publish.append(event_data)

        if (len(events_to_publish) > 0):
            self.publisher.topic_publish(events_to_publish)



