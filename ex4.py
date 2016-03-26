lidi_v_tymu = 13
mandays_za_tyden = 4.0
pocet_man_weeks = lidi_v_tymu * mandays_za_tyden

print "pocet lidi v tymu je", pocet_man_weeks, "(pocitano jako lidi v tymu ",lidi_v_tymu," krat mandays za tyden", mandays_za_tyden, ")"
print "je jedna rovna dvema?", 1==2

# ex5

spolecnost = 'Accenture'
pocet_zamestnancu = 375000.0000
pocet_lidi_v_CR = 1851.0000
pocet_zamestnancu_minus_milion = pocet_zamestnancu-1000000

print "Lets see how many people are in Czech republic in Accenture: %s" %pocet_lidi_v_CR
print "And in Accenture excluding Czech republic: %d" % (pocet_zamestnancu - pocet_lidi_v_CR)
print "And percent of Czech Accenture vs. whole world: %d" % (pocet_lidi_v_CR/pocet_zamestnancu *100)
print "Lets combine text %s and numbers %d" %(spolecnost, pocet_zamestnancu)
print "Kolik by bylo ACC lidi bez milionu? Asi tolik: %d" % pocet_zamestnancu_minus_milion

# rounding!
print round(4/3)


##################### ex6

x = "There are only %d kinds of people" % 10

print ("What will this variable %r do?") % x

# you can also nest variables:
y = "Text jak svina %r"
z = 10.00
yy = True
yyy = "TRUE"

#"muzu tam nacpat cislo?"
print y % z
#"muzu tam nacpat True/False?"
print y % yy
#"muzu tam nacpat text?"
print y % yyy


#"muzu do %s nacpat cislo?"
text_y = "Text jak svina %s"
print text_y % z #muzu:)

#jo, texty taky jdou concatenovat:
#nejdriv text a pak cislo
print y % z + y % yy
#nejdriv cislo a pak text

#pry %r je nej pro debugging?!