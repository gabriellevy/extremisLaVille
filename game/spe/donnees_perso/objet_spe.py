from abs.donnees_perso import objet

class ObjetSpe(objet.Objet):
    def __init__(self, id, image):
        objet.Objet.__init__(self, id, image)

class EpeeTemplier(ObjetSpe):
    ID = u"Épée de templier"
    def __init__(self):
        ObjetSpe.__init__(self, EpeeTemplier.ID, "images/objets/epee_templier.png")
