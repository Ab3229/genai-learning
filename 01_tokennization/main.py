import tiktoken

enc=tiktoken.encoding_for_model("gpt-4o")

text="Hey! i am abhishek agrawal"
tokens=enc.encode(text)

print(f"Tokens : ",tokens)

decode=enc.decode( [25216, 0, 575, 939, 692, 38520, 53420, 1017, 1618, 280])
print(f"Decode token are:  {decode}")