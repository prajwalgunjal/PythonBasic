if __name__ == "__main__":
    s = input("Enter a String : ")
    words = s.split('.')
    reversed_words = [word[::-1] for word in words]
    reversed_string = '.'.join(reversed_words)
    print(reversed_string[::-1])