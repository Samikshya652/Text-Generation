import random
from collections import defaultdict

class MarkovChainTextGenerator:
    def _init_(self):
        self.model = defaultdict(list)

    def train(self, text, n=2):
        """Train Markov model with n-grams (default bigram)"""
        words = text.split()
        for i in range(len(words) - n):
            key = tuple(words[i:i + n - 1])  # context window
            next_word = words[i + n - 1]
            self.model[key].append(next_word)

    def generate(self, length=50):
        """Generate text of given word length"""
        if not self.model:
            return ""

        start = random.choice(list(self.model.keys()))
        output = list(start)

        for _ in range(length - len(start)):
            key = tuple(output[-(len(start)):])
            next_words = self.model.get(key)
            if not next_words:
                break
            next_word = random.choice(next_words)
            output.append(next_word)

        return ' '.join(output)


# -------------------------------
# 🔁 Example Usage
# -------------------------------
if _name_ == "_main_":
    sample_text = """
    The quick brown fox jumps over the lazy dog. The dog barked and the fox ran into the forest. 
    In the forest, the fox met another fox. They became friends and hunted together under the moonlight.
    """

    generator = MarkovChainTextGenerator()
    generator.train(sample_text, n=2)  # Bigram model
    generated = generator.generate(30)

    print("Generated Text:\n")
    print(generated)