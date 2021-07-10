def convert_emojis(input_msg):
    words = input_msg.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(convert_emojis(message))
