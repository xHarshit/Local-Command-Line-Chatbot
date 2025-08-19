class ChatMemory:
    def __init__(self, max_turns=5):

        # Keeps track of recent conversation history using a sliding window.
        # max_turns: number of (user+bot) pairs to remember
        self.max_turns = max_turns
        self.history = []

    def add_message(self, speaker, message):
        # Add a message from 'User' or 'Bot' to history
        self.history.append(f"{speaker}: {message}")

        # Keep only last max_turns*2 messages (user+bot per turn)
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns*2:]

    def get_context(self):
        # Return conversation history as a single string
        return "\n".join(self.history)
