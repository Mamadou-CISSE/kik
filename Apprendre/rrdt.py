#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rrdtool
import os
import os
import shutil
import tempfile

"""def create():
    data_sources = [
        'DS:load1:GAUGE:600:0:U',
        'DS:load5:GAUGE:600:0:U',
        'DS:load15:GAUGE:600:0:U',
    ]
    rras = [
        'RRA:AVERAGE:0.5:1:600',
        'RRA:AVERAGE:0.5:6:700',
        'RRA:AVERAGE:0.5:24:775',
        'RRA:AVERAGE:0.5:288:797',
        'RRA:MAX:0.5:1:600',
        'RRA:MAX:0.5:6:700',
        'RRA:MAX:0.5:24:775',
        'RRA:MAX:0.5:288:797',
        'RRA:MIN:0.5:1:600',
        'RRA:MIN:0.5:6:700',
        'RRA:MIN:0.5:24:775',
        'RRA:MIN:0.5:288:797',
    ]

    rrdtool.create('pyload.rrd',
                   '--step', '300',
                   data_sources,
                   rras)


def main():
    create()

if __name__ == '__main__':
    main()"""
""" pour afficher tous les fichier et dossier de MOSECENTRE"""
"""for element in os.listdir('/Users/Mamadou/Downloads/MESOCENTRE 2'):
   if os.path.isdir(element):
       print("'%s' un dossier" % element)
   else:
       print("'%s' est un fichier" % element)"""
"""for i in range(101, 393):
    a = "/Users/Mamadou/Downloads/MESOCENTRE 2/Nagios_rrd_data/hpc-n"
    for element in os.listdir(a + str(i)):
        if element.endswith('.rrd'):
            print("'%s' est un fichier texte" % element)"""

#fichier = open('/Users/Mamadou/Downloads/MESOCENTRE 2/Nagios_rrd_data/hpc-n101/_HOST_.rrd', 'r')


for i in range(101, 393):
    for element in os.listdir('/Users/Mamadou/Downloads/MESOCENTRE 2/Nagios_rrd_data/hpc-n101'):
        if element.endswith('.rrd'):
            filename1 = tempfile.mktemp(".csv")
            open(filename1, "w").close()
            element = filename1 + ".copy"
            shutil.copy(filename1, element)

            print("'%s' est un fichier texte" % element)


"""for i in range(101, 393):
    a = "/Users/Mamadou/Downloads/MESOCENTRE/Nagios_rrd_data/hpc-n"
    for element in os.listdir(a + str(i)):
        if element.endswith('.rrd'):
            filename1 = tempfile.mktemp(".csv")
            open(filename1, "w").close()
            element = filename1 + ".copy"
            shutil.copy(filename1, element)

            print("'%s' est un fichier texte" % element)"""



"""for dossier, sous_dossiers, fichiers in os.walk('/Users/Mamadou/Downloads/MESOCENTRE 2/Nagios_rrd_data/hpc-n*'):
    #print('##### %s #####' % dossier)
    #print("Sous dossiers : %s" % sous_dossiers)
   # print("Fichiers : %s" % fichiers)
    if fichiers.endswith('.rrd'):
        print("'%s' est un fichier texte" % fichiers)"""


#Je veux rentre a l'interieure de hpc-n pour recupérée les ichiers .rrd mais j'arrive pas