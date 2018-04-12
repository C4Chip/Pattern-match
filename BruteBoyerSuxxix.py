import sys
import timeit
def bruteforce(pat, txt):
    M = len(pat)
    N = len(txt)
    count = 0
    start=timeit.default_timer()
    for i in xrange(N-M + 1):		
        for j in xrange(M):
            if txt[i + j] != pat[j]:
                break
        if j == M-1: 
            count=count+1
    end=timeit.default_timer()
    time=end-start
    print ('Brute Force:'+repr(time)+'s')

def boyer(pat,txt):
    alphabet=set(txt) #get all alphabet
    lastoccurance=dict()
    for letter in alphabet:
        lastoccurance[letter]=pat.rfind(letter)
    m=len(pat)
    n=len(txt)
    i=m-1
    j=m-1
    count=0
    start=timeit.default_timer()
    while i<n:
        if txt[i]==pat[j]:
            if j==0:
                count=count+1
                i=i+m
            else:
                i-=1
                j-=1
        else:
            l=lastoccurance[txt[j]]
            i=i+m-min(j,l+1)
            j=m-1
    end=timeit.default_timer()
    print 'Boyer Moore:'+repr(end-start)+'s'

def bisect_left(array, query, seq, lo=0, hi=None): #binar Suffix Array pattern matching
    if lo < 0:
        
    if hi is None: #by default len(array)
        hi = len(array)
    while lo < hi: 
        mid = (lo+hi)//2 #set the middle to binary search
        if seq[array[mid]:] < query:
            lo = mid+1
        else:
            hi = mid

    def match_at(i):
        return seq[i: i + len(query)] == query

    if not match_at(array[lo]):
        return 

    # array[lo] is one match
    # now we walk backwards to find the first match
    first = lo
    start=timeit.default_timer()
    while first > 0 and match_at(array[first - 1]):
        first -= 1

    # and walk forwards to find the last match
    last = lo
    while match_at(array[last]):
        last += 1
    end=timeit.default_timer()
    print ('occurrences: '+repr(len(array[first:last])))
    print ('Suffix Array: '+repr(end-start)+'s')



f1=open(sys.argv[1],"r")# 主串
string1=f1.read()
f2=open(sys.argv[2],"r")#SA
lines=f2.readlines()
f3=open(sys.argv[3],"r")#pattern
pats=f3.readlines()
lines=map(long,lines)
print ('text: ')
for pat in pats:
    pat=pat[:-1]
    bisect_left(lines,pat, string1)
    bruteforce(pat,string1)
    boyer(pat,string1)
