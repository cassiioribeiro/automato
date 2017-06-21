#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Transition:

    def __init__(self):
        self._list_transition = []
        self._list_letters = []
        self._final_state = False
        self._consumed_word = False
        self._pressed_enter = False

    @property
    def final_state(self):
        return self._final_state

    @final_state.setter
    def final_state(self, state):
        self._final_state = state

    @property
    def list_transition(self):
        return self._list_transition

    @property
    def last_transition(self):
        return self._list_transition[0][0]

    @property
    def current_state(self):
        return self._list_transition[0][1]

    def current_transition(self, letter, state):
        self._list_transition.append((letter, state))

    @property
    def all_transitions(self):
        return str(self._list_transition)

    @property
    def consumed_word(self):
        return self._consumed_word

    @consumed_word.setter
    def consumed_word(self, bool):
        self._consumed_word = bool

    @property
    def list_letters(self):
        return self._list_letters

    @list_letters.setter
    def list_letters(self, list_letters):
        self._list_letters = list_letters

    @property
    def current_letter(self):
        return self._list_letters[0]

    @property
    def pressed_enter(self):
        return self._pressed_enter

    @pressed_enter.setter
    def pressed_enter(self, pressed):
        self._pressed_enter = pressed
