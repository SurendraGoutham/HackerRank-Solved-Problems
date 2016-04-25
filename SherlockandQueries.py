'''
Created on 30-Jul-2014

@author: 00003179
'''
def sherlockandQueries(N,M,A,B,C):
    for i in xrange(1,M):
    	for j in xrange(1,N):
    		if (j % B[i]) == 0:
       			A[j] = A[j] * C[i]
    mod = (10**9)+7
    mas = [1]*(N + 1)
    for ind in xrange(M):
        mas[B[ind]] = mas[B[ind]] * C[ind] % mod
    
    for step in xrange(1, N+1):
        for a_ind in xrange(step-1, N, step):
            C[a_ind] = A[a_ind]*mas[step] % mod
    
    print ' '.join(map(str, A))
  
if __name__ == '__main__':
    N, M = map(int, raw_input().split())
    A = map(int, raw_input().strip().split(" "))
    B = map(int, raw_input().strip().split(" "))
    C = map(int, raw_input().strip().split(" "))
    sherlockandQueries(N,M,A,B,C)


