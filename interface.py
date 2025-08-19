from model_loader import load_model
from chat_memory import ChatMemory

def main():
    print("Chatbot started! Type '/exit' to quit.\n")

    generator = load_model()
    memory = ChatMemory(max_turns=3)  # remembers last 3 turns

    while True:
        user_input = input("User: ")

        if user_input.strip().lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        # Add user input to memory
        memory.add_message("User", user_input)

        # Build conversation context (last 3 turns)
        context = memory.get_context()

        # Format prompt for Flan-T5
        prompt = f"Conversation so far:\n{context}\nBot:"

        # Generate answer
        response = generator(
            prompt,
            max_new_tokens=100,
            num_beams=2,
            no_repeat_ngram_size=2
        )[0]['generated_text']

        # Extract only bot reply (after last "Bot:")
        if "Bot:" in response:
            bot_reply = response.split("Bot:")[-1].strip()
        else:
            bot_reply = response.strip()

        # Save bot reply
        memory.add_message("Bot", bot_reply)

        print("Bot:", bot_reply)

if __name__ == "__main__":
    main()
