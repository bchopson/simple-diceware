from secrets import randbelow
from typing import Dict, List


def get_list() -> Dict[str, str]:
    with open('diceware.wordlist.asc') as f:
        return {
            number: phrase
            for [number, phrase] in [line.strip().split('\t') for line in f.readlines()]
        }


def get_phrase(diceware_list: Dict[str, str]) -> str:
    key = ''
    for i in range(5):
        key = key + str(randbelow(6) + 1)
    return diceware_list[key]


def generate_password(length: int) -> List[str]:
    if i < 1:
        raise ValueError('Password must be at least one phrase')
    diceware_list = get_list()
    return ' '.join([get_phrase(diceware_list) for i in range(length)])
