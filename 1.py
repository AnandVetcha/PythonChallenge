#!/usr/bin/python3.5

####### Initialize Procedures #####
def DecryptMessage(text):
    ### To decrypt we need to shift all characters from a-z by 2 characters towards right
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
    return decrypt


####### Script Begins ##############
## Copy the message displayed on the webpage into below variable
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decrypt = DecryptMessage(text)
print("Decrypted message:")
print(decrypt+"\n")

solution =  DecryptMessage("map")
print("Link for next puzzle:")
print("http://www.pythonchallenge.com/pc/def/"+solution+".html")
