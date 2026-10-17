from math import *
import random as R, re

ch, ri = R.choice, R.randint
I = lambda f: lambda *a: 1. * f(*map(int, a))
dfact = I(lambda n: prod(range(n, 0, -2)))
subfact = I(lambda n: round(factorial(n) / e) + 0 ** n)

ENV = {
    **globals(), 'tg': tan, 'ctg': lambda x: 1 / tan(x), 'sec': lambda x: 1 / cos(x), 'cosec': lambda x: 1 / sin(x),
    'arcsin': asin, 'arccos': acos, 'arctg': atan, 'arcctg': lambda x: pi / 2 - atan(x),
    'arcsec': lambda x: acos(1 / x), 'arccosec': lambda x: asin(1 / x), 'arctg2': atan2,
    'sh': sinh, 'ch': cosh, 'th': tanh, 'cth': lambda x: 1 / tanh(x), 'sech': lambda x: 1 / cosh(x), 'csch': lambda x: 1 / sinh(x),
    'arsh': asinh, 'arch': acosh, 'arth': atanh, 'arcth': lambda x: atanh(1 / x),
    'ln': log, 'lg': log10, 'beta': lambda x, y: gamma(x) * gamma(y) / gamma(x + y),
    'fact': I(factorial), 'C': I(comb), 'A': I(perm), 'gcd': I(gcd), 'lcm': I(lcm),
    'abs': fabs, 'sgn': lambda x: (x > 0) - (x < 0), 'frac': lambda x: round(x % 1, 6), 'phi': (1 + 5 ** .5) / 2
}

OPS = '+ - * / ** // %'.split()
UF = 'sin cos tg ctg sec cosec arcsin arccos arctg arcctg arcsec arccosec sh ch th cth sech csch arsh arch arth arcth ln lg log2 gamma lgamma erf erfc sgn floor ceil frac'.split()
BF = 'C A gcd lcm hypot beta arctg2'.split()
nz = lambda a, b: ch([x for x in range(a, b + 1) if x])
num = lambda: str(ri(-9, 9) if R.random() < .4 else round(nz(-99, 99) / 100, 2) if R.random() < .67 else ch(('pi', 'e', 'phi', 'tau')))

def term():
    k = ch((0, 0, 1, 1, 2, 2, 3))
    if k < 1: return num()
    if k < 2:
        s, a = ch(('sqrt', 'cbrt', 'exp', 'abs', '!', '!!', 's!')), num()
        return {'sqrt': f"({ch([*range(10), *[round(x/100, 2) for x in range(1, 100)], 'pi', 'e'])})**0.5",
                'cbrt': f"(-(({a[1:]})**(1/3)))" if a[0] == '-' else f"({a})**(1/3)",
                'exp': f"e**({ri(-5, 5) if R.random() < .2 else round(nz(-99, 99)/100, 2)})",
                'abs': f"|{a}|", '!': f"{ri(0, 6)}!", '!!': f"{ri(0, 7)}!!", 's!': f"!{ri(0, 5)}"}[s]
    if k < 3:
        f = ch(UF)
        a = round(nz(-95, 95) / 100, 2) if f in ('arcsin', 'arccos', 'arth') else round(nz(-99, 99) / 10, 2) if f in ('arcsec', 'arccosec', 'arcth') and abs(x := nz(-99, 99)) > 10 else round(ri(10, 50) / 10, 2) if f == 'arch' else ch([*range(1, 10), 'e', 'pi']) if f in ('ln', 'lg', 'log2') else round(ri(10, 500) / 100, 2) if 'gamma' in f else num()
        return f"{f}({a})"
    f, n = ch(BF), ri(0, 8)
    return f"{f}({nz(-9, 9)}, {nz(-9, 9)})" if f in ('gcd', 'lcm') else f"{f}({n}, {ri(0, n)})" if f in 'CA' else f"{f}({ri(1, 9)/2}, {ri(1, 9)/2})" if f == 'beta' else f"{f}({num()}, {num()})"

fmt = lambda t, f=0, o='': f"({t})" if (t[0] == '-' and t[1] not in '(|' and not f) or (o == '**' and (t[0] == '-' or '**' in t)) else t

while 1:
    t1, t2, t3, o1, o2 = term(), term(), term(), ch(OPS), ch(OPS)
    x = f"{fmt(t1, 1, o1)} {o1} {fmt(t2)}" if R.random() < .5 else ch((f"{fmt(t1, 1, o1)} {o1} {fmt(t2, 0, o2)} {o2} {fmt(t3)}", f"({fmt(t1, 1, o1)} {o1} {fmt(t2)}) {o2} {fmt(t3)}", f"{fmt(t1, 1, o1)} {o1} ({fmt(t2, 1, o2)} {o2} {fmt(t3)})"))
    if R.random() < .2:
        w = ch('abs sqrt sin cos tg ctg sh ch ln erf floor ceil'.split())
        x = f"|{x}|" if w == 'abs' else f"({x})**0.5" if w == 'sqrt' else f"{w}({x})"
    try:
        s = x
        for p, r in ((r'!(\d+)', r'subfact(\1)'), (r'(\d+)!!', r'dfact(\1)'), (r'(\d+)!', r'fact(\1)'), (r'\|([^| ]+)\|', r'abs(\1)'), (r'\|([^|]+)\|', r'abs(\1)'), (r'(?<![.\w])(\d+)(?![.\w])', r'\1.')): s = re.sub(p, r, s)
        v = eval(s, {"__builtins__": {}}, ENV)
        if isnan(v) or isinf(v) or abs(v) > 1e5 or (v and not (a := round(v, 2))): continue
        a = int(a := round(v, 2)) if a == int(a) else a
        try:
            if round(float(input(f"{x} = ").replace(',', '.')), 2) != a: print(a)
        except ValueError: print(a)
    except (KeyboardInterrupt, EOFError): break
    except Exception: pass
