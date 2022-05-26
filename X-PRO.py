import os, sys
try:
    __import__("flame1").Main()
except Exception as e:
    exit(str(e))
