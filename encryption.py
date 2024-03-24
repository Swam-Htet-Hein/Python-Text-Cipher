from keys import keys
import time

user_input = input("Enter the message\n : ")
# convert string message into  list message
message = []
for letter in user_input:
  message.append(letter)

# setting for keys
max_setting = len(keys)
setting = int(input(f"Enter setting number from 0 to {max_setting-1}: "))
reset_setting = 0

# encrpyt message with the keys
encrpyt_index = []
for i in range(len(message)):
  for key_index in range(len(keys[setting])):
    if message[i] == keys[setting][key_index]:
      encrpyt_index.append(key_index)
  setting += 1
  if setting == max_setting:
    setting = reset_setting

# with encrpyt_index, turn index into charaters
# display is also important as keys
display = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "/", "{", "}", "[", "]", "\'", "\"", "?", ".", ",", ":", ";", "<", ">", "|", "_", "=", "`", "~"]

display_message_list = []
for i in encrpyt_index:
  display_message_list.append(display[i])

display_message = "".join(display_message_list)
print(display_message)

time.sleep(10)