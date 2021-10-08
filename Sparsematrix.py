def matchingStrings(strings, queries):
    # Write your code here

    result=[]
    n=len(strings)
    q=len (queries)
    for i in range (q):
        count = 0
        for j in range (n):
            if queries[i]==strings[j]:
                count+=1
        result.append(count)
    print (list(result))
s=["ab","ab","bbc","ba"]
qu=["ab","bbc","ca"]
matchingStrings(s,qu)