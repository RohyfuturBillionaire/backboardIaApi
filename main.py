import asyncio
from backboard import BackboardClient

async def main():
    client = BackboardClient("espr_drC5Q2Xtw3ecXdkqb7RFj9U3Gq1Vk1Xb6nbSB2il11A")
    assistant = await client.create_assistant(name="My first Assistant",system_prompt="You're a helpful assistant that responds concisely.")
    print("Assistant created with ID:", assistant.assistant_id)
    thread = await client.create_thread(assistant.assistant_id)
    print("Thread created with ID:", thread.thread_id)
    response = await client.add_message(thread.thread_id, content="What is the capital of France?", stream=False)
    print("Response:", response)
    full_content =""
    async for chunk in await client.add_message(thread.thread_id, content="What is the capital of France?", stream=True):
        if chunk.get("type")=="content_streaming":
            content_piece = chunk.get("content", "")
            full_content += content_piece
            print(content_piece, end="", flush=True)
        elif chunk.get("type")=="run_ended":
            break
    print ("\nFull response:", full_content)
    response = await client.add_message(thread_id=thread.thread_id, content="What is its population?", stream=False)
    print(f"Assistant:", {response.content})
    full_content =""
    async for chunk in await client.add_message(
        thread_id=thread.thread_id, 
        content="What is its population?", 
        stream=True):
        if chunk.get("type")=="content_streaming":
            content_piece = chunk.get("content", "")
            full_content += content_piece
            print(content_piece, end="", flush=True)
        elif chunk.get("type")=="run_ended":
            break
    print ("\nFull response:", full_content)
asyncio.run(main())