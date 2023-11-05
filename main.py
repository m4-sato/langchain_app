import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role":"system", "content": "You are a helpful assistant."},
        {"role":"user", "content":"hello! I'm John"}
    ]
)

print(response)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role":"system", "content":"You are a helpful assistant."},
        {"role":"user", "content":"hello! I'm John."},
        {"role":"assistant", "content":"Hello John! How can I assistant you today?"},
        {"role": "user", "content": "Do you know my name?"}
    ]
)

print(response)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! I'm John."}
    ],
    stream=True
)

for chunk in response:
    choice = chunk["choices"][0]
    if choice["finish_reason"] is None:
        print(choice["delta"]["content"])
        

# Chapter 3 Function Calling
def get_current_weather(location, unit="celsius"):
    weather_info = {
        "location": location,
        "unit": "celsius",
        "temperature": "25",
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

functions = [
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                "type": "string",
                "description": "The city and state, e.g. Tokyo",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
]

messages = [
    {"role": "user", "content": "What's the weather like in Tokyo?"}
]

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages,
    functions = functions
)

print(response)

response_message = response["choices"][0]["message"]

available_functions = {
    "get_current_weather": get_current_weather,
}
function_name = response_message["function_call"]["name"]
function_to_call = available_functions[function_name]
function_args = json.loads(response_message["function_call"]["arguments"])

function_response = function_to_call(
    location=function_args.get("location"),
    unit=function_args.get("unit"),
)

print(function_response)

messages.append(response_message)
messages.append(
    {"role": "function", 
    "name": function_name,
    "content": function_response,
    }
)

second_response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

print(second_response)