#!/usr/bin/env python
''' Encode and decode the simple caesar cipher. '''

import string


class Caesar:
    '''Caesar cipher implementation for the West CSC crypto toolkit.
    Implements @amillerrhodes' improved algorithm from https://stackoverflow.com/a/8895517.
    '''

    def __init__(self, alphabet: str = string.ascii_lowercase):
        self._alphabet: str = alphabet

    def use_alphabet(self, alphabet: str = string.ascii_lowercase) -> None:
        ''' Change the alphabet used by methods of this class.
        Args:
            alphabet (str): The avaliable alphabets are 
                ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
                ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                digits = '0123456789'
                hexdigits = '0123456789abcdefABCDEF'
                octdigits = '01234567'
                printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
        '''
        self._alphabet: str = alphabet

    def encode(self, plaintext: str, shift: int) -> str:
        '''Alphabetically shift each letter in plaintext forward by shift.

        Args:
            plaintext (str): The encoded string you want to decode.
            shift (int): The shift used to encode the string.

        Returns:
            The plaintext string.
        '''
        shifted_alphabet = self._alphabet[shift:] + self._alphabet[:shift]
        table = str.maketrans(self._alphabet, shifted_alphabet)
        return plaintext.translate(table)

    def decode(self, ciphertext: str, shift: int) -> str:
        '''Undo alphabetic shift to decode the caesar cipher.

        Args:
            ciphertext (str): The encoded string you want to decode.
            shift (int): The shift used to encode the string.

        Returns:
            The plaintext string.
        '''
        shifted_alphabet: str = self._alphabet[shift:] + self._alphabet[:shift]
        table: str = str.maketrans(shifted_alphabet, self._alphabet)
        return ciphertext.translate(table)
    
    def brute_force(self, ciphertext: str) -> None:
        '''Try all possibile shifts to decode by brute force

        Args:
            ciphertext (str): The encoded string you want to decode.
        
        Returns:
            Prints out all possible plaintexts.
        '''
        print('Attempting auto-decode with ciphertext', ciphertext)
        for i in self._alphabet.length:
            print(i, decode(ciphertext, i))