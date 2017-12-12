from UyghurSyllabification import *

# TODO: _ change to hemze 

sample = "hemme adem tuğuluşidinla erkin, izzet-hörmet ve hoquqta bab-baraver bolup tuğulğan.\
 ular eqilge ve vicdanğa ige hemde bir-birige qérindaşliq munasivitige xas roh bilen muamile qilişi kérek."

# sample = "alim."

words = sample.split(" ")
syl = UyghurSyllabification()

for w in words:
    print("%s : %s" % (w, syl.syllabication(w.lower())))

