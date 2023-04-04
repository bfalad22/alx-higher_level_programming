#!/usr/bin/python3

"""
This module is made up of a function that prints a text with 2 new lines after each of these characters: ". ? and :"

"""

def text_indentation(text):
    """ Function that prints 2 new lines after the characters: ". ? and :"

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string

    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences and print them with 2 new lines in between
    sentences = text.split(".")
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip()
        if sentences[i]:
            print(sentences[i] + ".")
            if i < len(sentences) - 1:
                print("\n")

    sentences = [sentence for sentence in sentences if sentence]
    questions = []
    for sentence in sentences:
        questions += sentence.split("?")
    for i in range(len(questions)):
        questions[i] = questions[i].strip()
        if questions[i]:
            print(questions[i] + "?")
            if i < len(questions) - 1:
                print("\n")

    questions = [question for question in questions if question]
    for sentence in questions:
        parts = sentence.split(":")
        for i in range(len(parts)):
            parts[i] = parts[i].strip()
            if parts[i]:
                print(parts[i] + ":")
                if i < len(parts) - 1:
                    print("\n")
