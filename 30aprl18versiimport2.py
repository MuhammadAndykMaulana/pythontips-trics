import operator

xs={'a': 4, 'b': 3, 'c': 2, 'd': 1}
while 1:
	srt=sorted(xs.items(),key=operator.itemgetter(1))
	print srt
	break
