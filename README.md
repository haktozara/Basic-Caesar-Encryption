# Caesar Cipher Encryption
### What is the Caesar Cipher?

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3:

- **Plaintext**: `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`
- **Ciphertext**: `D E F G H I J K L M N O P Q R S T U V W X Y Z A B C`

If you encrypt the letter `A` with a shift of 3, it becomes `D`. Similarly, `B` becomes `E`, `C` becomes `F`, and so on. The alphabet wraps around, so `X` becomes `A`, `Y` becomes `B`, and `Z` becomes `C`.

### How Does It Work?

1. **Choose a Shift Value**: This is the number of positions each letter will be shifted. For instance, a shift of 3 means each letter will move three places down the alphabet.
  
2. **Encrypting Text**: To encrypt a message, replace each letter in the plaintext with the letter that is a fixed number of positions down the alphabet. For example, with a shift of 3, the plaintext `HELLO` would be encrypted to `KHOOR`.

3. **Decrypting Text**: To decrypt, you simply reverse the shift. For a shift of 3, you would shift each letter in the ciphertext back by 3 positions to reveal the original plaintext.

### Example

- **Plaintext**: `HELLO`
- **Shift**: 3
- **Ciphertext**: `KHOOR`

### Strengths and Weaknesses

- **Strengths**: It’s easy to implement and understand. It provides a basic introduction to encryption techniques.
  
- **Weaknesses**: It’s not very secure by modern standards. With only 25 possible shifts (excluding a shift of 0), it’s vulnerable to a brute-force attack, where an attacker simply tries all possible shifts to decipher the message.

In this repository, we perform the following task:
Create a program that can encrypt and decrypt ext using the caesar cipher algorithm. Allow users to input a message and a shoft value to preform encryption and decryption. 
