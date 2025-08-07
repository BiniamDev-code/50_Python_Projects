# Typing Speed Tester
import time

text = "The quick brown fox jumps over the lazy dog."
print("Type this: ", text)
input("Press Enter to start...")
start = time.time()
user_input = input()
end = time.time()

wpm = (len(user_input.split()) / (end - start)) * 60
accuracy = sum(a == b for a, b in zip(user_input, text)) / len(text) * 100
print(f"WPM: {wpm:.2f}, Accuracy: {accuracy:.2f}%")
