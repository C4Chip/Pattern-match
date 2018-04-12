import sys

def editDist(str1,str2):
    m=len(str1)
    n=len(str2)
    line1=[]
    line2=[]
    line3=[]
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    #initialize dp matrix
    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j
    #fill the dp matrix
    for i in range(1,m+1):
        for j in range(1,n+1):
 
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]                
                
            else:
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove
                                   dp[i-1][j-1])      # Replace
                                   
    x=m
    y=n
    while (x>0 or y>0):
        if str1[x-1]==str2[y-1]:
            line1.append(str1[x-1])
            line2.append("|")
            line3.append(str2[y-1])
            x=x-1
            y=y-1
        else:
            if(dp[x-1][y-1]<=dp[x-1][y] and dp[x-1][y-1]<=dp[x][y-1]):
                line1.append(str1[x-1])
                line2.append(" ")
                line3.append(str2[y-1])
                x=x-1
                y=y-1
            if(dp[x-1][y]<dp[x-1][y-1] and dp[x-1][y]<=dp[x][y-1]):
                line1.append(str1[x-1])
                line2.append(" ")
                line3.append("-")
                #line3.append(str2[y-1])
                x=x-1
            if(dp[x][y-1]<dp[x-1][y-1] and dp[x][y-1]<dp[x-1][y]):
                line1.append("-")
                #line1.append(str1[x-1])
                line2.append(" ")
                line3.append(str2[y-1])
                y=y-1


            
    #print (dp)
    str1=''.join(line1)
    str2=''.join(line2)
    str3=''.join(line3)
    
    print (str1[::-1])
    print (str2[::-1])
    print (str3[::-1])
    
    print ("edit distance = "+repr(dp[m][n]))

f1=open(sys.argv[1],"r")
f2=open(sys.argv[2],"r")
string1=f1.read()
string1=string1.replace("\n"," ")
string2=f2.read()
string2=string2.replace("\n"," ")
f1.close()
f2.close()
print (editDist(string1,string2))


