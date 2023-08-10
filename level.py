import pygame
from support import import_csv_layout

class level: 
    def _init_(self,level_data,surface):
        self.display_surface = surface 

        terrain_layout = import_csv_layout(level_data['terrain'])

    def run(self):
        
        pass
