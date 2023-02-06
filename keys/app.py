#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List, Dict
from collections import Counter
import secrets as sec


class CmdLine:
    """
    Class that creates password as an object and can apply various methods
    for updates and validation

    Attributes:
        chars: list of characters available for random password creation
        length: desired length of password

    Methods:
        create_password: Creates password from input list of chars
        remove_chars: Input is a string of unwanted characters.
            Method removes these characters from the password string
            and replaces them with new characters
        remove_repeats: Removes duplicate values from
            password string. Replaces duplicates with
            new characters from chars list

    """

    password = ""

    def __init__(self, chars: List[str], length: int) -> None:
        self.chars: List[str] = chars
        self.length: int = length

    def create_password(self) -> None:
        CmdLine.password = "".join(
            [sec.choice(self.chars) for num in range(self.length)]
        )

    def remove_chars(self, removals: str) -> None:
        for char in removals:
            if char in CmdLine.password:
                self.chars.remove(char)
                new_char = sec.choice(self.chars)
                CmdLine.password = self.password.replace(char, new_char)

    def remove_repeats(self) -> None:
        pw_dict: Dict[str, int] = Counter(CmdLine.password)

        self.remove_chars("".join(list(pw_dict.keys())))

        while len(pw_dict) < self.length:
            new_char = sec.choice(self.chars)
            pw_dict[new_char] += 1

        CmdLine.password = "".join(list(pw_dict.keys()))

    def get_password(self) -> str:
        return CmdLine.password
