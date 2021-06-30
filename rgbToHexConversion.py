# A function that converts rgb decimal numbers to hexidecimal.

'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''
# (0  1  2  3  4  5  6  7  8  9   A   B   C   D   E   F).
# Steps to convert decimal to hex:
# Divide the number by 16.
# Get the integer quotient (d) for the next iteration.
# Get the remainder for the hex digit (multiply decimal by 16).
# Repeat the steps until the quotient is equal to 0.

'''def rgb(r, g, b):
    hexDict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexConv = []
    for d in [r, g, b]:
        hexVal = []
        if d > 255:
            d = 255
        elif d < 0:
            d = 0
        for h in range(2):
            d = d / 16
            decRem = int((d - int(d)) * 16)
            hexVal.append(hexDict[decRem])
        hexVal.reverse()
        hexConv.append(''.join(hexVal))
    return ''.join(hexConv)
'''

def rgb(r, g, b):
    hexColor = []
    for v in [r, g, b]:
        if v <= 0:
            v = 0
        if v > 255:
            v = 255
        if len(hex(v)[2:]) < 2:
            hexColor.append("0" + str(hex(v)[2:]))
        else:
            hexColor.append(str(hex(v)[2:]))
    return ''.join(hexColor).upper()

print(
    rgb(255, 255, 255), # returns FFFFFF
    rgb(255, 255, 300), # returns FFFFFF
    rgb(0,0,0), # returns 000000
    rgb(148, 0, 211) # returns 9400D3
)