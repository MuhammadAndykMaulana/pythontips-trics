# The get() method on dicts
# and its "default" argument

name_for_userid = {
	382:"Alice",
	590:"Bob",
	951:"Dilbert",
}

def greeting(userid):
	return "Hi %s! willkomen in diesem CLI" % name_for_userid.get(userid,"there")

while 1:
	#obj=greeting(userid)
	#id=input("greeting ")
	print greeting(input("greeting "))
	break
