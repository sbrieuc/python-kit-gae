#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'brieuc'


class DummyCache(object):

    def get(self, key):
        return None

    def set(self, key, value):
        pass