import datetime
import gzip
import os

from pubsub.pub_sub_helper import PubSubHelper
from streaming_simulator.streaming_simulator import StreamingSimulator
from dotenv import load_dotenv








def main():
    streamer: StreamingSimulator = StreamingSimulator(
        gcp_project=os.getenv('GCP_PROJECT'),
        topic=os.getenv('TOPIC')
    )

if __name__ == '__main__':
    load_dotenv('../.env')
    main()