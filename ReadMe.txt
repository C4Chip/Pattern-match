using py 2.7
how to run
1. editDistance.py
   python editDist.py <file1.txt> <file2.txt>
in my case
   python editDist.py dna1.txt dna2.txt
expect outpu:

ACATACGATACAGACGATCGGCTAGAATCCACCAGCTACAGCTAG-T-C---GATACA-G
||||||||||| | || |||||||||||||||||||||||||| | | ||| | |
ACATACGATAC--A-GA--GGCTAGAATCCACCAGCTACAGCTAGTTACAAGGATCGATG
CACGAATCGCTAAACAG-CTCGATCGATCGCTAGCTGATCGATACTTACCACAGCTGATC
|||||| |||||||| || | | ||||||||||||||||||||||||||||| |
CACGAA---CTAAACAGACTAG-TTTCTCGCTAGCTGATCGATACTTACCACAGCTAAAA
GATGCTATT-TAGCTAGCT-CGTAGTA
||||||||| | | |||| | ||
GATGCTATTATTG-GAGCTAATTTTTA
edit distance = 34



2. BruteBoyerSuxxix.py
   python BruteBoyerSuffix.py text.txt text.sa text.pat

in my case
   python BruteBoyerSuffix.py testBook.txt suffix.txt patterns.pat
expect output:
text: "testBook.txt"
pattern: "the"
occurrences: 11411
Suffix Array: 0.0001 s
Brute Force: 0.565772 s
Boyer-Moore: 0.416118 s
text: "testBook.txt"
pattern: "Raskolnikov"
occurrences: 784
Suffix Array: 0.0001 s
Brute Force: 0.618492 s
Boyer-Moore: 0.126854 s
text: "testBook.txt"
pattern: "dishevelled"
occurrences: 1
Suffix Array: 9.10000000003e-05 s
Brute Force: 0.59254 s
Boyer-Moore: 0.121932 s

in suffix array, using binary search to get the pattern


3. how to get suffix array
   python suffixArray testBook.txt
