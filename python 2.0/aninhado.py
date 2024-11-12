# Dicionario anilhados
import pprint

filmsDict = {
    "inception":{
        "yearRelease": 2010,
        "imdbRating": 8.8, 
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar":{
        "yearRelease": 2014,
        "imdbRating": 8.6, 
        "genre": ["Sci-fi", "Fiction"]
    },
    "the dark knight":{
        "yearRelease": 2010,
        "imdbRating": 9.0, 
        "genre": ["Sci-fi", "Drama", "Thriller"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - buscar uma informação dentro de um dicionário aninhado
print(filmsDict["interstellar"], ["genre"])

# 2 - Adicionar novo item 
filmsDict["inception"]["director"] = "Christopher Nolan"
print(filmsDict["inception"])

# 3 - Excluir um dicionário
del filmsDict["the dark knight"]
pp.pprint(filmsDict)