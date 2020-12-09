def cryptoMachine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    value = keys[-1] + keys[0:-1]

    encryptDic = dict(zip(keys, value))
    decryptDic = dict(zip(value, keys))

    msg = input("Enter the Secret Message")
    mode = input("Enter the mode : E or D")

    if mode.upper() =='E':
        newMsg = ''.join([encryptDic[letter] for letter in msg.lower()])
    elif mode.upper() == 'D':
        newMsg = ''.join([decryptDic[letter] for letter in msg.lower()])
    else :
        print("Enter Correct choice")
    
    return newMsg

print(cryptoMachine())
