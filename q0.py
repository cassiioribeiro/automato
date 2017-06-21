#!/usr/bin/env python
# -*- coding: utf-8 -*-

from q1 import Q1
from q2 import Q2
from q3 import Q3

import re


class Q0:

    def __init__(self, transition):
        self._final_state = False
        self._current_letter = 'Ɛ'
        self._word = None
        self._transition = transition
        self._current_state = 'Q0'

    @property
    def final_state(self):
        return self._final_state

    def start(self, word):

        self._word = word

        if self.contains_spaces() is False:
            for i in range(0, self._word.__len__(), 1):
                self._transition.list_letters.append(self._word[i])

            if self._transition.list_letters.__len__() != 0:
                self._current_letter = self._transition.current_letter

            return self.next_transition

        return True

    @property
    def next_transition(self):

        self._transition.current_transition(self._current_letter,
                                            self._current_state)

        self._transition.final_state = self.final_state

        if len(self._word) == 0:
            self._transition.pressed_enter = True
            self._transition.consumed_word = True
            return True
        elif self._current_letter == '+' or self._current_letter == '-':
            return Q1(self._transition).start()
        elif self._current_letter == '.':
            return Q2(self._transition).start()
        elif re.findall(r'[0-9]', self._current_letter) != []:
            return Q3(self._transition).start()
        elif self._transition.list_letters.__len__().__eq__(0):
            self._transition.consumed_word = True
            return True
        elif self._current_letter is None:
            self._transition.consumed_word = True
            print('asdasd')
            return True
        else:
            self._transition.consumed_word = True

            if self._transition.list_letters.__len__() != 0:
                self._transition.consumed_word = False
            return True


    def contains_spaces(self):
        if self._word.__contains__(' '):
            print('Palavra inválida!\nNão pode conter espaços.')
            return True
        return False
