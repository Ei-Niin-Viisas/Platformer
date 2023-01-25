import pygame

#Luodaan luokka/olio päävalikolle
class paaValikko:    
    #olion konstruktori
    def __init__(self, testi:str):
        self.sana = testi

    #olion testimetodi
    def tulosta(self):
        print(self.sana)

