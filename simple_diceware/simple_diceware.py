import argparse
import pkgutil
from secrets import randbelow
from typing import Dict, List


def get_list() -> Dict[str, str]:
    wordlist = pkgutil.get_data(__name__, 'eff_large_wordlist.txt').decode('utf-8')
    return {
        number: phrase
        for [number, phrase] in [line.strip().split('\t') for line in wordlist.strip().split('\n')]
    }


def get_phrase(diceware_list: Dict[str, str]) -> str:
    key = ''
    for i in range(5):
        key = key + str(randbelow(6) + 1)
    return diceware_list[key]


def generate_password(length: int) -> str:
    if length < 1:
        raise ValueError('Password must be at least one phrase')
    diceware_list = get_list()
    return ' '.join([get_phrase(diceware_list) for i in range(length)])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'length',
        nargs='?',
        default=6,
        type=int,
        help='Number of words in the passphrase (defaults to 6)',
    )
    parsed = parser.parse_args()
    print(generate_password(parsed.length))


if __name__ == '__main__':
    main()
