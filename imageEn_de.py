from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("200x160")

def encrypt_image():
    #print("gyfhjekdjhgfghjk")
    file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file','*.jpg')])
    if file1 is not None :
        #print(file1)
        file_name = file1.name
        print(file_name)
        key = enter1.get(1.0, END)
        print(file_name, key)
        fl = open(file_name, 'rb')
        img = fl.read()
        fl.close()
        img = bytearray(img)
        
        for index, values in enumerate(img):
            img[index] = values^int(key)
        
        fl1 = open(file_name, 'wb')
        fl1.write(img)
        fl1.close()



b1 = Button(root, text = "Encryption", command = encrypt_image)
b1.place(x=70,y=10)

enter1 = Text(root, height=1,width=12)
enter1.place(x=50,y=50)

root.mainloop()
