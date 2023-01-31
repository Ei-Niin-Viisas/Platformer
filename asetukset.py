class asetukset:
    def __init__(self, versio:int):
        self.versio = versio
    
    def arvot(self):
        if self.versio == 1:
            return 60
        else:
            return 120