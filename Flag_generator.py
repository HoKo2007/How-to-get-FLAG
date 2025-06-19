import base64 as b, itertools as i

def ψ(z): return ''.join(map(chr, z))

def α(s): return b.b64decode(s.encode()).decode()

def β(x): return bytes.fromhex(x).decode()




