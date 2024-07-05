import string
import argparse
from random import choices
class PasswordGenerator:

    
    def generator(length=16, upper=False, lower=False, digit=False, pun=False):
        character = ''

        if upper:
            character += string.ascii_uppercase
        if lower:
            character += string.ascii_lowercase
        if digit:
            character += string.digits
        if pun:
            character += string.punctuation
        if character == '':
            character += string.ascii_letters

        return ''.join(choices(character, k=length))

    
    def main():
        parse = argparse.ArgumentParser(description='Password Generator')
        parse.add_argument('length', type=int, help='Length of the password')
        parse.add_argument(
            '-u', '--upper', help='Include upper case characters', action='store_true')
        parse.add_argument(
            '-l', '--lower', help='Include lower case characters', action='store_true')
        parse.add_argument(
            '-d', '--digit', help='Include digit characters', action='store_true')
        parse.add_argument(
            '-p', '--pun', help='Include punctuation characters', action='store_true')

        args = parse.parse_args()
        password = PasswordGenerator.generator(
            length=args.length,
            upper=args.upper,
            lower=args.lower,
            digit=args.digit,
            pun=args.pun)

        print(password)

if __name__ == '__main__':
    PasswordGenerator.main()
