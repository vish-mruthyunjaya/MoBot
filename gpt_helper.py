import json

with open("query_instruction.txt", "rb") as f:
    query_instruction = f.read()

def get_query_prompt(user_input, past_conversations):
    prompt = f'''{query_instruction} + {user_input} + Past Conversations: {past_conversations}'''
    messages = [{
                "role": "user",
                "content": prompt
            }]
    return messages

def get_gpt_message(client, user_input, past_conversations):
    query_prompt = get_query_prompt(user_input=user_input, past_conversations=past_conversations)
    try:
        gpt_output = client.chat.completions.create(model="gpt-4-1106-preview",
                                                    temperature=0.0,
                                                    messages=query_prompt,
                                                    response_format={"type": "json_object"}
                                                    )
        return json.loads(gpt_output.choices[0].message.content)['cypher_query']
    except Exception as e:
        if e:
            print(e)
            return None
