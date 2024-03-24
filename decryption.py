from keys import keys
import time

display = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "/", "{", "}", "[", "]", "\'", "\"", "?", ".", ",", ":", ";", "<", ">", "|", "_", "=", "`", "~"]

user_input = input("Enter the message you've recieve\n : ")

# extract encrypt index from message you've recieve with display list
encrypt_index = []
for i in user_input:
  encrypt_index.append(display.index(i))

# setting for keys
setting = int(input("Enter setting number : "))
max_setting = len(keys)
reset_setting = 0

# decrypt message with encrypt index
decrpyt_message_list = []
for key_index in encrypt_index:
  decrpyt_message_list.append(keys[setting][key_index])
  setting += 1
  if setting == max_setting:
    setting = reset_setting

decrypt_message = "".join(decrpyt_message_list)
print(decrypt_message)

time.sleep(10)