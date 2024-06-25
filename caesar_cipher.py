def caesar_cipher(text, shift):
  result = ''
  for char in text:
    if char.isalpha():
      start = ord('a') if char.islower() else ord('A')
      shifted_char = chr((ord(char) - start + shift) % 26 + start)
    else:
      shifted_char = char
    result += shifted_char
  return result

def main():
  text = input("Enter the text: ")
  shift = int(input("Enter the shift value: "))

  encrypted_text = caesar_cipher(text, shift)
  decrypted_text = caesar_cipher(encrypted_text, -shift)

  print("Encrypted Text:", encrypted_text)
  print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
  main()
