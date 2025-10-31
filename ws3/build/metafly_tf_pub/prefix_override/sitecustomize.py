import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/min/a/khochwal/ece569-fall2025/Lab3/ws3/install'
