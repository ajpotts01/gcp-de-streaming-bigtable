from google.cloud import pubsub


class PubSubHelper:
    gcp_project: str
    topic_path: str
    publisher: pubsub.PublisherClient

    def __init__(self, gcp_project: str, topic: str):
        self.gcp_project = gcp_project
        self.topic_path = topic

    def topic_setup(self):
        # TODO: Add logging
        publisher: pubsub.PublisherClient = pubsub.PublisherClient()
        topic_path: str = publisher.topic_path(
            project=self.gcp_project, topic=self.topic_path
        )

        try:
            publisher.get_topic(topic=topic_path)
        except:
            publisher.create_topic(topic=topic_path)

        self.publisher = (
            publisher  # TODO: Consider an FP way of doing all this at some point
        )

    def topic_publish(self, events: list[str]):
        if (
            (len(events) > 0)
            and (len(self.topic_path > 0))
            and (self.publisher is not None)
        ):
            # TODO: Add logging
            for next_event in events:
                self.publisher.publish(topic=self.topic_path, data=next_event)
