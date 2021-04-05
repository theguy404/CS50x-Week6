import cs50

def main():
    while True:
        text = cs50.get_string("Text: ")
        if text:
            break
    
    letters = 0
    sentences = 0
    words = text.count(" ")
    
    sentences += text.count(".")
    sentences += text.count("!")
    sentences += text.count("?")
    
    letters += len(text)
    letters -= sentences
    letters -= words
    letters -= text.count(",") + text.count('"') + text.count("'") + text.count("-")
    
    L = letters / words
    L *= 100
    
    S = sentences / words
    S *= 100
    
    index = 0.0588 * L
    index -= 0.296 * S
    index -= 15.8
    index = int(index)
    
    if index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")
    
if __name__ == "__main__":
    main()