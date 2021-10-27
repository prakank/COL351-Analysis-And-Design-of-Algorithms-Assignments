import random
import numpy as np
import matplotlib.pyplot as plt

p = 18181
m = 10000
n = 100

def Hash(x, n):
    return x % n

def Hash_r(x, r, p, n):
    return ((x*r) % p) % n

U = np.arange(1, m)
if __name__ == "__main__":
    max_1 = []
    max_2 = []
    for k in range(1, n+1):
        r = random.randint(1,p-1)
        #print(r)
        arr1 = [n*i for i in range(k)]
        np.random.sample()
        arr2 = np.random.choice(U, size=n-k, replace=False)
        arr1.extend(arr2)
        #print(arr1)
        array_h = [0]*n
        array_hr = [0]*n
        for val in arr1:
            array_h[Hash(val, n)]+=1
            array_hr[Hash_r(val, r, p, n)]+=1
        mx1 = max(array_h)
        mx2 = max(array_hr)
        max_1.append(mx1)
        max_2.append(mx2)
    plt.figure(figsize=(10,6))
    #plt.plot(np.arange(1, n+1), max_1, c = 'blue', linewidth = 1, label = 'Max chain length for H(.)')
    plt.plot(np.arange(1, n+1), max_2, c = 'orange', linewidth = 1)#, label = 'Max chain length for Hr(.)')
    plt.xlabel("k")
    plt.ylabel("Max chain length")
    plt.title("Max-chain-length for hash functions Hr()")
    # plt.legend()
    plt.savefig("plot_Hr.png")

    plt.figure(figsize=(10,6))
    plt.plot(np.arange(1, n+1), max_1, c = 'blue', linewidth = 1)
    #plt.plot(np.arange(1, n+1), max_2, c = 'orange', linewidth = 1, label = 'Max chain length for Hr(.)')
    plt.xlabel("k")
    plt.ylabel("Max chain length")
    plt.title("Max-chain-length for hash functions H()")
    # plt.legend()
    plt.savefig("plot_H.png")



