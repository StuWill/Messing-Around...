alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 0
new_message = ''

message = input('Please enter a message: ')
key = int(input('Please enter a key: '))

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    new_position = (position + key) % 26
    new_character = alphabet[new_position]
    new_message += new_character
  else:
    new_message += character
print('The shifted message is: ', new_message)

