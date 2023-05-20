from geometry.myobj import MyObject
from material.texture import TextureMaterial
from core_ext.texture import Texture
from core_ext.mesh import Mesh
from core.moveobject import moveobject
from material.phong import PhongMaterial
from material.flat import FlatMaterial



class Objects:
    def __init__(self, mat_file, obj_file=None, geometry=None):
        if geometry is not None:
            obj = geometry
        else:
            obj = MyObject(obj_file)
        mat = FlatMaterial(Texture(mat_file))
        self.mesh = Mesh(obj, mat)

    
    def update(self, input_object, delta_time):
        moveobject(self.mesh, input_object, delta_time)