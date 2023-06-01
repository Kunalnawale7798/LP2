name = input("hello! whats your name?\n")
age = int(input("nice to meet you,{}. How old are you?\n".format(name)))

if age < 18:
    print("I'm sorry but you are too young to enroll in college.")
else:
    collegeName = input("which college are you interested in?\n")
    print("thank you for your interest in {}. Our admission team will contact you soon.".format(collegeName))