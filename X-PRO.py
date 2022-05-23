import os, sys
try:
    __import__("flame").Main()
except Exception as e:
    exit(str(e))
