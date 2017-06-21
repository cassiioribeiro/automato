#!/usr/bin/env python
# -*- coding: utf-8 -*-

from transition import Transition
from q0 import Q0

class Automaton:

    def __init__(self):
        self._digit_alphabet = (0, 1, 2, 3, 4, 5, 7, 8, 9)
        self._symbol_alphabet = ('E', '+', '-', '.')
        self._letter_list = []
        self._word = None
        self.choose = True

        self._finished = False

        self._transition = Transition()
        self._q0 = Q0(self._transition)

    def main(self):
        self.choose = True

        while self.choose:
            self._transition.final_state = False
            self._transition.consumed_word = False
            self._transition.pressed_enter = False
            self._transition.list_transition.clear()
            self._transition.list_letters.clear()
            self._letter_list.clear()
            self._finished = False
            self._word = None

            self.start()

            a = str(input('\n\nDigite qualquer tecla para inserir outra palavra,'
                      ' ou (n) para sair: \n'))
            if a.__eq__('n'):
                self.choose = False
            else:
                self.choose = True

    def show_result(self, finished, consumed):
        if self._transition.pressed_enter:
            word = 'Ɛ'
        else:
            word = self._word
        print(
            'Alfabeto: ' +
            str(self._symbol_alphabet)+ '-' +
            str(self._digit_alphabet)+
            '\n\nPalavra: ' + word +
            '\nTransições: ' + self._transition.all_transitions
            )
        if finished and consumed and (self._transition.final_state or self._transition.pressed_enter):
            print('\nPalavra aceita!')
        else:
            print('\nPalavra não aceita!')

    def start(self):

        print('\nDigite a palavra a ser conhecida: ')
        self._word = str(input())

        while self._finished is False:
            self._finished = self._q0.start(self._word)
            consumed = self._transition.consumed_word

        self.show_result(self._finished, consumed)



if __name__ == '__main__':
    a = Automaton()
    a.main()
