#-------------------------------------------------------------------------------
# Name:        parser https://afisha.sevastopol.press/movie
# Purpose:
#
# Author:      092goncharvv
#
# Created:     01.03.2018
# Copyright:   (c) 092goncharvv 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import bs4, requests
import operator
'''
Метод парсит https://afisha.sevastopol.press/movie фильмы текущего
выводя информацию в виде строки
'''
def cinemaRead():
    url_cinema='https://afisha.sevastopol.press/movie'
    s=requests.get(url_cinema)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    films=[]
    move=''
    try:
        cinema_list=b.select('.col-2-3 .row')[1]
        for cinema in cinema_list.select('.col-1-2'):
            films.append('***************\n')

            nameFilm=cinema.select('h2')[0].getText()
            films.append(''.join([nameFilm,'\n']))
            janrFilm=cinema.select('.genre')[0].getText()
            films.append(''.join([janrFilm,'\n']))

            seances=cinema.select('.seance td')
            for seance in seances:
                films.append(''.join([str(seance.getText()),'\n']))


        for film in films:
            move=''.join([move,film])
        return move

    except:
        print('not correct match css')

'''
Метод парсит https://afisha.sevastopol.press/movie фильмы текущего
выводя информацию в виде словаря
'''
def cinema_Read():
    url_cinema='https://afisha.sevastopol.press/movie'
    s=requests.get(url_cinema)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    CinemaKys=[]
    CinemaValues=[]
    listGroupkino=[]
    listGroupSeance=[] # Список сеансов в кинотеатре
    listGrafSeance=[] #Список словарей содержащих информацию о сеансах по кинотеатрам
    films={} # итоговый словарь

    i=0
    j=0
    try:
        cinema_list=b.select('.col-2-3 .row')[1]

        for cinema in cinema_list.select('.col-1-2'):
            nameCinema=cinema.select('h2')[0].getText()

            CinemaKys.append(nameCinema)
            janrCinema=cinema.select('.genre')[0].getText()
            CinemaValues.append(janrCinema)
            seances=cinema.select('.seance td')


            listKinoteatr=list()
            listSeance=[]
            for count in range(len(seances)):
              if count%2==0:
                    listKinoteatr.append(seances[count].getText())

              else:
                listSeance.append(seances[count].getText().split(' ')[:-1])


            listGroupkino.append(listKinoteatr)
            listGroupSeance.append(listSeance)

            grafSeance={}
            i=0
            for kinoteatr in  listGroupkino[j]:

                grafSeance[kinoteatr]=listGroupSeance[j][i]

                listGrafSeance.append(grafSeance)
                i=+1

            j=+1

        h=0
        for k in CinemaKys:
            films[k]=[CinemaValues[h],listGrafSeance[h]]
            h=+1
        return films
    except:
        print('not correct match css')


def sortKeysDict(dicObg):
    listDicKeys=dicObg.keys()
    listKeysSort=list(listDicKeys)
    listKeysSort.sort()
    return listKeysSort

