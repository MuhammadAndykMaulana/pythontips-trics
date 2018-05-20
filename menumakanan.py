import time

print """Tersedia Makanan dengan Menu:
 [ ] Kabuli
 [ ] Gulai
 [*] Rawon
 [ ] Soto
 [ ] Rujak"""

options = ['Kabuli', 'Gulai', 'Rawon', 'Soto', 'Rujak']
a=input("Masukkan pilihan menu makanan: ")

def draw_menu(options, selected_index):
    for counter, option in enumerate(options,1):
        if counter == selected_index:
           print " [*] %s" % option
        else:
           print " [ ] %s" % option

draw_menu(options, a)
print "Anda memesan makanan {}".format(options[a-1])
