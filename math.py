from math import *
import random as R, re

M = int(input('Mode (0/1): ') == '1')  # 0 — base, 1 — the whole math
C, Z = R.choice, R.randint
I = lambda f: lambda *a: 1. * f(*map(int, a))
G = lambda x: gamma(x*(x>0))
E = {**globals(), 'tg': tan, 'ctg': lambda x: 1/tan(x), 'sec': lambda x: 1/cos(x), 'cosec': lambda x: 1/sin(x), 'arcsin': asin, 'arccos': acos, 'arctg': atan, 'arcctg': lambda x: pi/2-atan(x), 'arcsec': lambda x: acos(1/x), 'arccosec': lambda x: asin(1/x), 'arctg2': atan2, 'sh': sinh, 'ch': cosh, 'th': tanh, 'cth': lambda x: 1/tanh(x), 'sech': lambda x: 1/cosh(x), 'csch': lambda x: 1/sinh(x), 'arsh': asinh, 'arch': acosh, 'arth': atanh, 'arcth': lambda x: atanh(1/x), 'ln': log, 'lg': log10, 'gamma': G, 'lgamma': lambda x: lgamma(x*(x>0)), 'beta': lambda x, y: G(x)*G(y)/G(x+y), 'fact': I(factorial), 'dfact': I(lambda n: prod(range(n, 0, -2))), 'subfact': I(lambda n: round(factorial(n)/e)+0**n), 'C': I(comb), 'A': I(perm), 'gcd': I(gcd), 'lcm': I(lcm), 'abs': fabs, 'sgn': lambda x: 1.*((x>0)-(x<0)), 'floor': lambda x: 1.*floor(x), 'ceil': lambda x: 1.*ceil(x), 'frac': lambda x: round(x%1, 6), 'phi': (1+5**.5)/2}
O = '+ - * / ** // %'.split()[:4+3*M]
U = 'sin cos tg ctg sec cosec arcsin arccos arctg arcctg arcsec arccosec sh ch th cth sech csch arsh arch arth arcth ln lg log2 gamma lgamma erf erfc sgn floor ceil frac'.split()
B = 'C A gcd lcm hypot beta arctg2'.split()
N = lambda: str(C((Z(-9, 9), Z(-99, 99)/100 or .5, C(('pi', 'e', 'phi', 'tau')))[:1+2*M]))
F = lambda t, f=0, o='': f"({t})" if t[0]=='-' and not f or '**' in o and (t[0] in '-!' or '**' in t) else t

def T():
    a, f, n = N(), C(B), Z(0, 8)
    p = f"({a})" if a<'0' else a
    return C((a, C((f"{a[a<'0':]}**0.5", f"{p}**(1/3)", f"e**{p}", f"|{a}|", f"{Z(0,6)}!", f"{Z(0,7)}!!", f"!{Z(0,5)}")), f"{C(U)}({a})", f"{f}({Z(1,9)*C((-1,1))}, {Z(1,9)*C((-1,1))})" if f in ('gcd','lcm') else f"{f}({n}, {Z(0,n)})" if f in 'CA' else f"{f}({a}, {N()})")[:1+3*M])

try:
    while 1:
        a, b, c, p, q = T(), T(), T(), C(O), C(O)
        x = C((f"{F(a,1,p)} {p} {F(b,0,p)}",)*3 + (f"{F(a,1,p)} {p} {F(b,0,p+q)} {q} {F(c,0,q)}", f"({F(a,1,p)} {p} {F(b,0,p)}) {q} {F(c,0,q)}", f"{F(a,1,p)} {p} ({F(b,1,q)} {q} {F(c,0,q)})"))
        w = C('abs sqrt sin cos tg ctg sh ch ln erf floor ceil'.split())
        x = x if Z(1, 5) > M else f"|{x}|" if w=='abs' else f"({x})**0.5" if w=='sqrt' else f"{w}({x})"
        try:
            s = x
            for k, r in ((r'\(-([^()]+)\)\*\*\(1/3\)', r'(-\1**(1/3))'), (r'(\d+)!!', r'dfact(\1)'), (r'(\d+)!', r'fact(\1)'), (r'!(\d+)', r'subfact(\1)'), (r'\|([^| ]+)\|', r'abs(\1)'), (r'\|([^|]+)\|', r'abs(\1)'), (r'(?<![.\w])(\d+)(?![.\w])', r'\1.')): s = re.sub(k, r, s)
            v = eval(s, E)
            assert (0 < abs(r := round(v, 2)) <= 1e5 or v == 0) and v % 1 <= M
        except: continue
        ans = r if r % 1 else int(r)
        try: assert round(float(input(f"{x} = ").replace(',', '.')), 2) == ans
        except Exception: print(ans)
except (KeyboardInterrupt, EOFError): pass
