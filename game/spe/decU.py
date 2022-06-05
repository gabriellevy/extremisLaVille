from abs import declencheur
from abs.univers import temps
from abs import proba
from abs import modifProba
from abs import condition

class DecU(declencheur.Declencheur):
    """
    U signifie 'Unique' => l'événement auquel on applique ce déclencheur ne peut s'exécuter qu'une fois maximum
    """

    def __init__(self, aproba, labelGoTo):
        """
        identique à la version classique mais ne se déclenche qu'une fois maximum quoiqu'il arrive
        """
        declencheur.Declencheur.__init__(self, aproba, labelGoTo)
        self.selecteur_ = None # référence vers le sélecteur qui contient ce déclencheur

    def executer(self):
        # cette exécution ne doit plus jamais arriver : on lui met une proba à 0 :
        # self.proba_ = proba.Proba(0)
        if self.selecteur_ is not None:
            self.selecteur_.declencheurs_.remove(self)
        return self.labelGoTo_
