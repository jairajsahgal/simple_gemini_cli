import google.generativeai as genai
import os
from rich.console import Console

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
console = Console()
chat = model.start_chat()
console.print("Enter 'exit' to quit: ", style="green")
console.print("Enter your prompt: ", style="red")
while True:
    response = None
    prompt = input(">> ")
    if prompt == "exit" or prompt == "exit;":
        break
    status_task = console.status("[bold cyan]Please wait...")
    with status_task:
        while response is None:
            response = chat.send_message(prompt)
    console.print(response.text)
    print("\n")

console.print("Thank you for using Gemini Pro!", style="green")
