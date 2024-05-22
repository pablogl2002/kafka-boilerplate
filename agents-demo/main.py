# import libraries
import faust

# create the app name
app = faust.App("agents-demo",)#broker='kafka://localhost')

# From the app send topic to greeting topic
greetings_topic = app.topic("greetings", value_type=str, value_serializer='raw')


# wait for the streaming data to be consumed from greeting topic and print the result. Please note the function is async
@app.agent(greetings_topic)
async def greetings_processor(stream):
    async for greeting in stream:
        print(f"Greeting is '{greeting}'")
