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
            #print(''.join(['Название фильма: ',nameFilm]))
            #print(''.join(['Жанр: ', janrFilm]))
            seances=cinema.select('.seance td')
            for seance in seances:
                films.append(''.join([str(seance.getText()),'\n']))

                #print(''.join(['', str(seance.getText())]))
            #print('')
#         print(films)

        for film in films:
            move=''.join([move,film])
        return move

    except:
        print('not correct match css')
        #return films

def cinema_Read():
    url_cinema='https://afisha.sevastopol.press/movie'
    s=requests.get(url_cinema)
    b=bs4.BeautifulSoup(s.text, "html.parser")
    CinemaKys=[]
    CinemaValues=[]
    listSeance=[]
    listKinoteatr=[]
    grafSeance={}
    films={}
    move=''
    i=0
    try:
        cinema_list=b.select('.col-2-3 .row')[1]
        for cinema in cinema_list.select('.col-1-2'):

            nameCinema=cinema.select('h2')[0].getText()
            CinemaKys.append(nameCinema)
            #nmaeCinemaKys.append(''.join([nameFilm,'\n']))
            janrCinema=cinema.select('.genre')[0].getText()
            CinemaValues.append(janrCinema)

            seances=cinema.select('.seance td')
            #print(seances[0].getText())
            #films[nameCinema]=janrCinema
            #films1=sorted(films.items,kye=operator.itemgetter(0))

            #print(len(seances))
            listKinoteatr.clear()
            listSeance.clear()
            i=0
            for count in range(len(seances)):
              if count%2==0:
                    listKinoteatr.append(seances[count].getText())
              else:
                listSeance.append(seances[count].getText())
            for kinoteatr in  listKinoteatr:
                grafSeance[kinoteatr]=listSeance[i].split(' ')
                i+=i

            #print(listKinoteatr)
            #print(listSeance)
            #grafSeance[listKinoteatr]=listSeance
            #print(grafSeance)
            films[nameCinema]=[janrCinema,grafSeance]

                #print(''.join(['', str(seance.getText())]))
            #print('')
        print(films)

 #       for film in films:
 #           move=''.join([move,film])
        return films

    except:
        print('not correct match css')
        #return films

if __name__ =='__main__':
    cinema_Read()
