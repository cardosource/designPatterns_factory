from abc import ABCMeta, abstractclassmethod


class Artefato(metaclass=ABCMeta):

    @abstractclassmethod
    def conteudo(self):
        pass


class Social(Artefato):

    def conteudo(self):
        print("pão vacina e educação")

class Tecnologia(Artefato):
    def conteudo(self):
        print("Filosofia Open Source...")


    
"""Fabrica """


class Frabricar:

    def criar_conteudo(self,  gerar):
        return eval(gerar)().conteudo()


#Solicitar
rodar= Frabricar()
conteudo = input("Qual movimento apoiaria  [tecnologia ou social")
rodar.criar_conteudo(conteudo)
