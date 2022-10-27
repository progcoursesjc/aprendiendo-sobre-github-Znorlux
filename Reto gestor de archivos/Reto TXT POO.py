import collections
songs = open("songs.txt")
song_list = songs.read().split("==")
#songs_words = songs.read().split()

#CANCION 1:
def palabras_diferentes():
    print("Cancion numero 1:")
    print("=="*10)
    song1 = song_list[0].split()
    print("Tiene un total de", len(song1), " palabras")
    #print(song_list[0])
    #print(song1)
    palabras_diferentes1 = []
    for i in song1:
        for j in song1:
            if i != j and i not in palabras_diferentes1:
                palabras_diferentes1.append(i)
    #print(palabras_diferentes1)
    print("La cantidad de palabras diferentes en la primera cancion es", len(palabras_diferentes1))
    print("=="*10)

#CANCION 2:
    print("Cancion numero 2:")
    print("=="*10)
    song2 = song_list[1].split()
    print("Tiene un total de", len(song2), "palabras")
    #print(song_list[1])
    palabras_diferentes2 = []
    for k in song2:
        for r in song2:
            if k != r and k not in palabras_diferentes2:
                palabras_diferentes2.append(k)
    print("La cantidad de palabras diferentes en la segunda cancion es", len(palabras_diferentes2))
    print("=="*10)
#CANCION 3:
    print("Cancion numero 3:")
    print("=="*10)
    song3 = song_list[2].split()
    print("Tiene un total de", len(song3), "palabras")
    #print(song_list[2])
    palabras_diferentes3 = []
    for k in song3:
        for r in song3:
            if k != r and k not in palabras_diferentes3:
                palabras_diferentes3.append(k)
    print("La cantidad de palabras diferentes en la tercera cancion es", len(palabras_diferentes3))

#Palabras diferentes en todas las canciones

def palabras_dif_canciones():
    print("=="*10)
    songs = open("songs.txt")
    songs_words = songs.read().split()
    print("La cantidad de palabras de todas las canciones es", len(songs_words))
    palabras_diferentes_c = []
    for i in songs_words:
        for j in songs_words:
            if i != j and i not in palabras_diferentes_c:
                palabras_diferentes_c.append(i)
    print("La cantidad de palabras diferentes en toda la lista de canciones es:", len(palabras_diferentes_c))
    print("=="*18)

#5 palabras mas repetidas
def palabras_repetidas():
    songs = open("songs.txt")
    songs_words = songs.read().split()
    counter = collections.Counter(songs_words)
    print("Las 5 palabras mas repetidas son: ")
    for palabra, cont in counter.most_common(5):
        print(f"'{palabra}' aparece {cont} {'veces' if cont > 1 else 'vez'}.")
    print("=="*12)

#Comparaciones con stopwords
def delete_stopwords():
    songs = open("songs.txt")
    songs_words = songs.read().split()
    stopwords = open("stopwords.txt")
    stopwords_list = stopwords.read().split("\n")
    stopwords_deleted = []
    for i in songs_words:
        for j in stopwords_list:
                if i == j and i not in stopwords_deleted:
                    stopwords_deleted.append(i)
                    for w in songs_words:
                        for k in stopwords_deleted:
                            if w == k:
                                songs_words.remove(i)
    #print(stopwords_deleted)
    print(f"Se eliminaron {len(stopwords_deleted)} palabras consideradas stopwords")
    print(f"Ahora la lista con canciones tiene {len(songs_words)} palabras")

    counter = collections.Counter(songs_words)
    for palabra, cont in counter.most_common(5):
        print(f"'{palabra}' aparece {cont} {'veces' if cont > 1 else 'vez'}.")

palabras_diferentes()
palabras_dif_canciones()
palabras_repetidas()
delete_stopwords()