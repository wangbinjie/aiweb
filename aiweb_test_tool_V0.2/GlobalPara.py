# -*- coding: utf-8 -*-


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue


# class GlobalPara:
#     def __init__(self):
#         self._global_dict = {}
#
#     def set_value(self, name, value):
#         self._global_dict[name] = value
#
#     def get_value(self, name, defValue=None):
#         try:
#             return self._global_dict[name]
#         except KeyError:
#             return defValue
