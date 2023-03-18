# Simple version
# def greet_user():
#     print("Hi there!")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user()
# print("Finish")


# With parameters and arguments
# def greet_user(firstName, lastName):
#     print(f"Hi there! {firstName} {lastName}")
#     print("Welcome aboard")
#
#
# print("Start")
# greet_user("Usman", "Shahid")
# # With Keyword Arguments, you improve the readability of our code
# greet_user(lastName="Smith", firstName="John")
# print("Finish")


# With a return statement
# By default all methods return None, if we don't make it return anything ourselves
# def square(number):
#     # This will return a number instead of None
#     return number * number
#
#     # This will return None, after it prints the result
#     #return print(number * number)
#
#
# print(square(3))


# Emoji Converter Example:
def emoji_converter(message):
    words = message.split(" ")  # Splits the input by space
    output = ""

    # Using a dictionary
    emojis = {
        ":)": "😊",
        ":(": "😢"
    }

    for word in words:
        output += emojis.get(word, word) + " "

    return output


# Outside our function
message = input("Enter your message")
result = emoji_converter(message)
print(result)