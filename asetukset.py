class asetukset:
    def __init__(self, versio:int):
        self.versio = versio
    
    def arvot(self):
        if self.versio == 1:
            lista = [60, 720, 1280]
            return lista
        else:
            return [120, 1080, 1920]