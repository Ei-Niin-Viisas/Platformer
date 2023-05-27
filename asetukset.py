# tiilien määrä tarvitaan grafiikan oikein piirtämistä varten ja tiilien koko myös.
# niillä myös määräytyy ruudun korkeus.
vertical_tile_number = 11
tile_size = 64
screen_height = vertical_tile_number * tile_size
screen_widht = 1280


class asetukset:
    def __init__(self, versio: int):
        self.versio = versio

    # Palauttaa peli-ikkunan resoluution
    def arvot(self):
        if self.versio == 1:
            lista = [60, screen_height, screen_widht]
            return lista
