from solution_3 import Album, Song, Music
import datetime

menu = ('1.Включить песню. \n'
        '2.Поставить на паузу. \n'
        '3.Выключить песню. \n'
        '4.Ничего. \n')

with open('songs.txt', encoding='utf-8') as f_1:
    for n in f_1:
        info = n.split(';')
        if '\n' in info[4]:
            info[4] = info[4][:-1]
        Song(info[0], info[1], info[2], info[3], info[4])

with open('albums.txt', encoding='utf-8') as f_2:
    for n in f_2:
        info = n.split(';')
        Album(info[0], info[1], info[2])


def main():
    flag_1 = False
    while not flag_1:
        print(menu)
        try:
            answer = int(input('Ваш ответ: '))
            flag_1 = True
        except ValueError:
            print('Ошибка!')
        if answer == 1:
            flag_2 = False
            while not flag_2:
                for i in range(len(Song.all_songs)):
                    print(f'{str(i + 1)}.{Song.all_songs[i]}')
                try:
                    ans = int(input('Какую песню хотите включить? '))
                    if ans > len(Song.all_songs) or ans <= 0:
                        print('Ошибка!')
                    else:
                        flag_2 = True
                except ValueError:
                    print('Ошибка!')
            Music(Song.all_songs[ans - 1])
            print(Music.start(Music.playing_song[0]))
            while datetime.datetime.now() <= Music.playing_song[0].fnsh:
                time_diff = Music.playing_song[0].fnsh - datetime.datetime.now()
                Music.playing_song[0].last = datetime.timedelta(seconds=time_diff.total_seconds())
                main()
            if datetime.datetime.now() == Music.playing_song[0].fnsh:
                print(Music.finish(Music.playing_song[0]))
                main()
        elif answer == 2:
            if Music.playing_song:
                print(Music.pause(Music.playing_song[0]))

            else:
                print('Песня не включена!')
            main()
        elif answer == 3:
            if Music.playing_song:
                print(Music.finish(Music.playing_song[0]))
            else:
                print('Песня не включена!')
            main()


print('Здравствуйте! Что хотите сделать?')
main()
