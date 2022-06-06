from abs import declencheur
from abs.univers import temps
from abs import proba
from abs import modifProba
from abs import condition

class DecU(declencheur.Declencheur):
    """
    U signifie 'Unique' => l'événement auquel on applique ce déclencheur ne peut s'exécuter qu'une fois maximum
    """

    def __init__(self, aproba, labelGoTo, tempsPasseEnMin):
        """
        identique à la version classique mais ne se déclenche qu'une fois maximum quoiqu'il arrive
         - tempsPasseEnMin est en général égal à 0 si l'évt est juste pour l'embiance et sans vrai temps passé
        """
        declencheur.Declencheur.__init__(self, aproba, labelGoTo)
        self.selecteur_ = None # référence vers le sélecteur qui contient ce déclencheur
        self.tempsPasseEnMin_ = tempsPasseEnMin

    def executer(self, situation):
        situation.AvanceDeXMinutes(self.tempsPasseEnMin_)
        if self.selecteur_ is not None:
            self.selecteur_.declencheurs_.remove(self)
        return self.labelGoTo_
