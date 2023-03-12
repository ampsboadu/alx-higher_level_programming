#!/usr/bin/python3
def multiple_returns(sentence):
    lght = len(sentence)
    f_char = sentence[0] if lght > 0 else None
    return (lght, f_char)
