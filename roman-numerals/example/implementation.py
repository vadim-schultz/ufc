def to_roman(num):
    result = ""
    while num > 0:
        if num >= 1000:
            result += "M"
            num -= 1000
        elif num >= 900:
            result += "CM"
            num -= 900
        elif num >= 500:
            result += "D"
            num -= 500
        elif num >= 400:
            result += "CD"
            num -= 400
        elif num >= 100:
            result += "C"
            num -= 100
        elif num >= 90:
            result += "XC"
            num -= 90
        elif num >= 50:
            result += "L"
            num -= 50
        elif num >= 40:
            result += "XL"
            num -= 40
        elif num >= 10:
            result += "X"
            num -= 10
        elif num >= 9:
            result += "IX"
            num -= 9
        elif num >= 5:
            result += "V"
            num -= 5
        elif num >= 4:
            result += "IV"
            num -= 4
        else:
            result += "I"
            num -= 1
    return result


def from_roman(s):
    result = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in ("CM", "CD", "XC", "XL", "IX", "IV"):
            if s[i:i+2] == "CM":
                result += 900
            elif s[i:i+2] == "CD":
                result += 400
            elif s[i:i+2] == "XC":
                result += 90
            elif s[i:i+2] == "XL":
                result += 40
            elif s[i:i+2] == "IX":
                result += 9
            elif s[i:i+2] == "IV":
                result += 4
            i += 2
        else:
            if s[i] == "M":
                result += 1000
            elif s[i] == "D":
                result += 500
            elif s[i] == "C":
                result += 100
            elif s[i] == "L":
                result += 50
            elif s[i] == "X":
                result += 10
            elif s[i] == "V":
                result += 5
            elif s[i] == "I":
                result += 1
            i += 1
    return result
