import numpy as np

#calc eigen vals & vect by using qr method
def qrmethod(m):
    x = m
    y = np.eye(m.shape[0])
    for i in range(6):
        q, r = np.linalg.qr(x)
        y = np.dot(y, q)
        x = np.dot(r, q)
    return np.diag(x), y

#calc right singular vect(MtM)
def findRightSing(m):
    return np.dot(m.transpose(), m)

#get sigma
def getSigma(n,mat,val):
    for i in range(n):
        mat[i] = np.sqrt(abs(val[i]))
#get U
def getU(u,n,val):
    for i in range (n):
        u[:,i] = u[:,i]/np.sqrt(np.abs(val[i]))

#decompose m -> U sigma Vt
def svdmethod(m):
    #init
    V = findRightSing(m)
    eigVal, eigVec = qrmethod(V)

    #sort eigen vals & vec
    idx = eigVal.argsort()[::-1]
    eigVal = eigVal[idx]
    eigVec = eigVec[:,idx]
    eigVal = eigVal[eigVal != 0.0] #discard 0
    k = len(eigVal)

    #init U, sigma, Vt
    U = np.dot(m,eigVec[:,:k])
    sigma = np.zeros(k)
    Vt = eigVec.transpose()

    #get U, sigma
    getSigma(k,sigma,eigVal)
    getU(U,k,eigVal)
    return U, sigma, Vt