text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decrypt = ""
for letter in text:
    if ord(letter) == 32:
        number = ord(letter)
    elif ord(letter) < 97:
        number = ord(letter)
    elif ord(letter) >= 121:
        number = ord(letter) + 2 - 26 
    else:
        number = ord(letter) + 2
    decrypt = decrypt + chr(number)

print(decrypt)
