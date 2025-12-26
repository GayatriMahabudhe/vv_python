
"""Module to demonstrate built-in module properties."""
import sys

def print_module_properties():
    this = sys.modules[__name__]
    print(f"__name__ : {this.__name__}")
    try:
        print(f"__file__ : {this.__file__}")
    except AttributeError:
        print("__file__ : (not available)")
    print(f"__dict__ keys : {list(this.__dict__.keys())[:10]} ...")
