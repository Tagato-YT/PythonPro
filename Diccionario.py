meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una Respuesta hacia una Broma",
            "SHEESH": "ligera desaprobacion",
            "CREEPY": "Aterrador o de miedo",
            "AGGRO": "Ponerse agresivo o enojarse",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("Esa palabra no esta en nuesto dicionario")
