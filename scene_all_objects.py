import math
import pathlib
import sys

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[2])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.sphere import SphereGeometry
from extras.movement_rig import MovementRig
from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial
from core_ext.texture import Texture
from light.ambient import AmbientLight
from light.directional import DirectionalLight
from light.point import PointLight
from core.settings import Settings
from core_ext.group import Group
from objetos import Objects
import game_fuctions as gf
from trophs import Trophs
from game_stats import GameStats
from material.lambert import LambertMaterial
from material.phong import PhongMaterial
from material.flat import FlatMaterial
from foods import Food


class Example(Base):
    """
    Render the axes and the rotated xy-grid.
    Add box movement: WASDRF(move), QE(turn), TG(look).
    """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0.1, 6, 10])
        self.camera.rotate_x(43.5)
        self.gm_settings = Settings()


        ambient = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient)
        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional)
        point = PointLight(color=[0.9, 0, 0], position=[1, 1, 0.8])
        self.scene.add(point)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 4, 8])
        self.scene.add(self.rig)

        self.pan = Objects('texture/metal_preto.jpg', 'obj_files/fryingPan1.obj')
        self.pan.mesh.set_position([0, 0, 0])
        self.pan.mesh.scale(1.5)
        self.scene.add(self.pan.mesh)

        sky_geometry = SphereGeometry(radius=50)
        """sky_material = TextureMaterial(
            texture=Texture(file_name="texture/stars.png"),
            property_dict={"repeatUV": [2, 2]}
            #property_dict={"offsetUV": [50, 50]}
        )"""
        sky_material = LambertMaterial(
            texture=Texture(file_name="texture/stars.png"),
            #property_dict={"repeatUV": [2, 2]}
            #property_dict={"offsetUV": [50, 50]}
        )
        sky = Mesh(sky_geometry, sky_material)
        self.scene.add(sky)
        floor_geometry = RectangleGeometry(width=10, height=10)
        """floor_material = TextureMaterial(
            texture=Texture(file_name="texture/floor.jpg"),
            property_dict={"repeatUV": [20, 20]}
            #property_dict={"offsetUV": [50, 50]}
        )"""
        floor_material = LambertMaterial(
            texture=Texture(file_name="texture/floor.jpg"))
        floor = Mesh(floor_geometry, floor_material)
        floor.rotate_x(-math.pi / 2)
        floor.set_position([0, -1, 0])
        self.scene.add(floor)

        self.foods = Group()
        self.objects = Group()
        self.scene.add(self.foods)
        self.scene.add(self.objects)

        # Add the Heads Up Display (HUD) layer
        self.hud_scene = Scene()
        self.hud_camera = Camera()
        self.hud_camera.set_orthographic(0, 800, 0, 600, 1, -1)

        self.pontuation = Trophs()
        self.hud_scene.add(self.pontuation.pt_mesh)
        self.hud_scene.add(self.pontuation.mesh)

        self.stats = GameStats(self.gm_settings)


    def update(self):
        gf.creat_foods(self.foods, self.gm_settings)
        gf.creat_objects(self.objects, self.gm_settings)
        self.foods.translate(0, -self.gm_settings.food_speed_factor, 0)
        self.objects.translate(0, -self.gm_settings.object_speed_factor, 0)
        self.pan.update(self.input, self.delta_time)
        gf.check_colisions_foods(self.foods, self.pan.mesh, self.pontuation)
        gf.check_colisions_objects(self.objects, self.pan.mesh, self.stats)
        gf.remove_olds(self.foods, self.objects, self.stats)
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hud_scene, self.hud_camera, clear_color=False)
        self.pontuation.update()
        


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
