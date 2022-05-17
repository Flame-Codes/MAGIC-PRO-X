import os, sys
try:
    __import__("sc").Main()
except Exception as e:
    exit(str(e))
