#a=[x*x for x in range(77)]
	#x +=1
#print a
new_range  = [i * i for i in range(input("masukkan range ")) if i % 2 == 0]
print new_range

S = [x**2 for x in range (input("Masukkan range/batas S gan: "))]
print S
V = [2**i for i in range(input("Masukkan range V gan: "))]
print V
M = [x for x in S if x % 2 == 0]
print M
