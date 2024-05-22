# import libraries
import faust
import random

# create the appand send the topic named greetings
app = faust.App("producer-consumer-demo")
greetings_topic = app.topic(
    "greetings", value_type=str, value_serializer='raw')


# Run after every interval of 5 sec. Generate random data and send it to topic. Please note the function is async
@app.timer(interval=5)
async def generate_greeting():
    prefix = random.choice(["First", "Second", "Third"])
    recipient = random.choice(["actor", "actress", "comedian"])
    await greetings_topic.send(value=f"{prefix} {recipient}")


# wait for the streaming data to be consumed from greeting topic and print the result. Please note the function is async
@app.agent(greetings_topic)
async def process_greetings(stream):
    async for greeting in stream:
        print(f"Greeting is '{greeting}'")
