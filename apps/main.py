import faust
from confluent_kafka.admin import AdminClient, NewTopic
import os

network = os.getenv("KAFKA_NETWORK")
app = faust.App("agent-dealer", broker=f'kafka://{network}')

kafka_broker_config = {
    'bootstrap.servers': network
}

def create_kafka_topics():
    admin_client = AdminClient(kafka_broker_config)

    topics = [
        NewTopic('hello_world', num_partitions=1, replication_factor=1),
        NewTopic('hello_world.reply', num_partitions=1, replication_factor=1)
    ]

    fs = admin_client.create_topics(topics)

    for topic, f in fs.items():
        try:
            f.result()
            print(f"Topic {topic} created successfully")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

create_kafka_topics()

hello_topic = app.topic("hello_world", value_type=str, value_serializer='raw')
@app.agent(hello_topic)
async def hello_processor(stream):
    async for event in stream.events():
        t = app.topic("hello_world.reply", value_type=str, value_serializer='raw')
        await t.send(value="Hello World")
        print(f"{event.message.topic}: '{event.value}'")
