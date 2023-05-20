from geometry.myobj import MyObject
from material.texture import TextureMaterial
from core_ext.texture import Texture
from core_ext.mesh import Mesh
import random
from material.phong import PhongMaterial


class Food:
    def __init__(self, obj_file, mat_file, gm_settings):
        super().__init__()
        self.gm_settings = gm_settings
        obj = MyObject(obj_file)
        mat = PhongMaterial(Texture(mat_file))
                                    #property_dict={"wireframe":True})
        self.mesh = Mesh(obj, mat)
        positions = [-5, 0, 5]
        self.mesh.set_position([random.choice(positions), random.randrange(10, 50), random.choice(positions)])
        self.mesh.scale(0.4)


    def update(self):
        """move alimento pra baixo"""
        self.mesh.translate(0, -self.gm_settings.food_speed_factor, 0)
        