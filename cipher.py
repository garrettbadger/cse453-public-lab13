##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        pass

    def get_author(self):
        # TODO: Return your name
        return "Garrett Badger"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "Vigenere"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "Author: Gustavus J. Simmons " \
            "Title: Vigenere Ciper " \
        "https://www.britannica.com/topic/Vigenere-cipher"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = "encrypt(plaintext, password):\n" \
            "    conv_text <- [ord(c) for c in plaintext] \n" \
            "    conv_pass <- [ord(c) for c in plaintext] \n" \
            "    x=1 \n" \
            "    FOR i in range(0, len(plaintext)): \n" \
            "        IF i > len(conv_pass)-1: \n" \
            "            conv_text[i] = conv_text[i] + conv_pass[i-x] \n" \
            "            x+=1 \n" \
            "        ELSE \n" \
            "            conv_text[i] = conv_text[i] + conv_pass[i] \n" \
            "        WHILE conv_text[i] > 126: \n" \
            "            conv_text[i] -=95\n" \
            "        WHILE conv_text[i] < 32: \n" \
            "            conv_text[i] +=95\n" \
            "    FOR i in range(0, len(conv_text)): \n" \
            "        cipher_text += chr(conv_text[i]) \n" \
            "    RETUN cipher_text \n\n" 

        # The decrypt pseudocode
        pc += "decrypt(plaintext, password):\n" \
            "    conv_text <- [ord(c) for c in plaintext] \n" \
            "    conv_pass <- [ord(c) for c in plaintext] \n" \
            "    x=1 \n" \
            "    FOR i in range(0, len(plaintext)): \n" \
            "        IF i > len(conv_pass)-1: \n" \
            "            conv_text[i] = conv_text[i] - conv_pass[i-x] \n" \
            "            x+=1 \n" \
            "        ELSE \n" \
            "            conv_text[i] = conv_text[i] - conv_pass[i] \n" \
            "        WHILE conv_text[i] > 126: \n" \
            "            conv_text[i] -=95\n" \
            "        WHILE conv_text[i] < 32: \n" \
            "            conv_text[i] +=95\n" \
            "    FOR i in range(0, len(conv_text)): \n" \
            "        cipher_text += chr(conv_text[i]) \n" \
            "    RETUN cipher_text \n\n" 
        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        # TODO - Add your code here
        cipher_text = ""
        conv_text = [ord(c) for c in plaintext]
        conv_pass = [ord(c) for c in password]
        x=1
        for i in range(0, len(plaintext)):
            if i > len(conv_pass)-1:
                conv_text[i] = conv_text[i] + conv_pass[i-x]
                x+=1
            else:
                conv_text[i] = conv_text[i] + conv_pass[i]
            while conv_text[i] > 126:
                conv_text[i] -= 95
            while conv_text[i] < 32:
                conv_text[i] += 95
        for i in range(0, len(conv_text)):
            cipher_text +=chr(conv_text[i])
        return cipher_text
        

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        
        # TODO - Add your code here
        cipher_text = ""
        conv_text = [ord(c) for c in ciphertext]
        conv_pass = [ord(c) for c in password]
        x=1
        for i in range(0, len(ciphertext)):
            if i > len(conv_pass)-1:
                conv_text[i] = conv_text[i] - conv_pass[i-x]
                x+=1
            else:
                conv_text[i] = conv_text[i] - conv_pass[i]
            while conv_text[i] > 126:
                conv_text[i] -= 95
            while conv_text[i] < 32:
                conv_text[i] += 95
        for i in range(0, len(conv_text)):
            cipher_text +=chr(conv_text[i])
        return cipher_text
        