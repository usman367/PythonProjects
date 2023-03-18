message = input("Enter your message")
words = message.split(" ")  # Splits the input by space

emojis = {
    ":)": "😊",
    ":(": "😢"
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "

print(output)