with open ("books/frankenstein.txt") as f:
    content = f.read()
    print (content)
    words = content.split()
    count = len(words)
    print (len(words))