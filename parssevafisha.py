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
            #print('+++')
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

    