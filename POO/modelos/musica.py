class Musica:
    def __init__(self, nome, artista):
        self.nome = nome
        self.artista = artista

    def __str__(self):
        return f"{self.nome} | {self.artista} "

chicago = Musica("Chicago", "Michael Jackson")
relax = Musica("Relax My Eyes", "!!!!!")

print(chicago)
print(relax)


