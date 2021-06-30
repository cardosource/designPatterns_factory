from abc import ABCMeta, abstractclassmethod

class Sessao(metaclass=ABCMeta):

     @abstractclassmethod
     def  __repr__(self) -> str:
         pass


class Anime(Sessao):

    def  __repr__(self)-> str :
         return 'Continuar'

class NovoAnime(Sessao):

    def  __repr__(self)-> str :
         return 'Novo Catalogo'

class Indicacao(Sessao):
    def  __repr__(self) -> str:
         return ' Erased - A cidade Onde Só Eu Não Existo'

class Temporada(Sessao):
    def  __repr__(self)-> str :
         return '1 Temporada'

class  Genero(Sessao):
    def  __repr__(self)-> str :
         return 'Mistério, Ficção científica, Suspense'

class  Perfil(metaclass=ABCMeta):
    def __init__(self) -> str:
        self.sessoes =[]
        self.criar_perfil()

    @abstractclassmethod
    def criar_perfil(self):
        pass

    def get_sessao(self):
        return self.sessoes

    def add_sessao(self,sessao):
        self.sessoes.append(sessao)



class OtakuUm(Perfil):
    def criar_perfil(self):
        self.add_sessao(Anime())
        self.add_sessao(Temporada())
        self.add_sessao(Genero())

class OtakuDois(Perfil):
    def criar_perfil(self):
        self.add_sessao(Temporada())
        self.add_sessao(Indicacao())

class OtakuTres(Perfil):
    def criar_perfil(self):
        self.add_sessao(NovoAnime())
        self.add_sessao(Indicacao())
        self.add_sessao(Temporada())



if __name__ == '__main__':
    perfil_um = OtakuUm()
    perfil_dois =  OtakuDois()
    perfil_tres =  OtakuTres()

    print(f' {type(perfil_um).__name__}  assistindo')
    print(f' Anime  {perfil_um.get_sessao()}\n')

    print(f'{type(perfil_dois).__name__}  assistindo')
    print(f'Anime  {perfil_dois.get_sessao()}\n')

    print(f'{type(perfil_tres).__name__}  assistindo')
    print(f'Anime  {perfil_tres.get_sessao()}\n')
