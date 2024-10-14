import os
import google.generativeai as genai
import config_key

# Configure the API key
genai.configure(api_key=config_key.api_key)

# Initialize the chat history
chat_history = []

def Ai(query):
    global chat_history  # To maintain the chat history across function calls

    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Convert chat_history to the expected format for the API
    formatted_history = [
        {"role": "user" if i % 2 == 0 else "model", "parts": [{"text": entry["content"]}]}
        for i, entry in enumerate(chat_history)
    ]

    # Start the chat session with the existing history
    chat_session = model.start_chat(
        history=formatted_history  # Correctly formatted chat history
    )

    # Add the user's query to the prompt
    full_prompt = query

    # Send the message and get the response
    response = chat_session.send_message(full_prompt)

    # Append the query and response to the history in the proper format
    chat_history.append({"content": query})  # User's query
    chat_history.append({"content": response.text})  # Model's response

    return response.text

# Example of using the function
# print(Ai("What is the capital of France?"))
# print(Ai("Who is the president of the United States?"))
