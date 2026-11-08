import json, collections, sys
import sys
tris=json.load(open(sys.argv[1]))
def key(v): return (round(v[0]*1e4),round(v[1]*1e4),round(v[2]*1e4))
for name,t in tris.items():
    e=collections.Counter(); degenerate=0
    for a,b,c in t:
        ka,kb,kc=key(a),key(b),key(c)
        if len({ka,kb,kc})<3: degenerate+=1; continue
        for p,q in ((ka,kb),(kb,kc),(kc,ka)): e[(p,q)]+=1
    unmatched=sum(1 for (p,q),n in e.items() if e.get((q,p),0)!=n)
    nonman=sum(1 for n in e.values() if n>1)
    print(f'{name:16s} tris={len(t):6d} unmatched_edges={unmatched:5d} nonmanifold_edges={nonman:4d} collapsed={degenerate}')
