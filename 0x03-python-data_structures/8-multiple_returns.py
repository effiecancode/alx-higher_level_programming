#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        char0 = None
    else:
        char0 = sentence[0]
        result = multiple_returns(sentence)
            print("length: {:d} - First character: {:c}".format(result[0], result[1]))
