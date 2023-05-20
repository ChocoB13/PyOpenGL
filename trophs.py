from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial
from material.sprite import SpriteMaterial
from extras.text_texture import TextTexture
from core_ext.texture import Texture
from core_ext.mesh import Mesh

class Trophs:
    def __init__(self):
        self.ponto = 0
        pont_geo = RectangleGeometry(width=120, height=60, position=[800, 600], alignment=[1,1])
        pont_mat = TextureMaterial(TextTexture(text="Pontuação",
                                    system_font_name="Arial",
                                    font_size=50, font_color=[0, 0, 0],
                                    transparent=True,
                                    image_width=250, image_height=138,
                                    align_horizontal=0.5, align_vertical=0.1,
                                    image_border_width=4,
                                    image_border_color=[0, 0, 0]))
        self.pt_mesh = Mesh(pont_geo, pont_mat)
        sprite_geometry = RectangleGeometry(width=120, height=60, position=[800, 600], alignment=[1,1])
        sprite_material = SpriteMaterial(Texture("images/pontos.png"), {
            "billboard" : 1, 
            "tileCount" : [5, 5],
            "tileNumber" : 0
        })
        self.mesh = Mesh(sprite_geometry, sprite_material)

    
    def update(self):
        self.mesh.material.uniform_dict["tileNumber"].data = self.ponto
            
