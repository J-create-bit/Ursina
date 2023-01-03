from ursina import*
from ursina.prefabs.\
    first_person_controller \
    import FirstPersonController

from ursina.shaders import\
    lit_with_shadows_shader

#Window
app = Ursina(borderless=False)
random.seed(0)
Entity.default_shader = \
    lit_with_shadows_shader
window.size = (400, 700)

#Making the lava
ground = Entity(
    model='plane',
    collider='box',
    scale=64,
    color=color.red
    )

#Making the player    
player = FirstPersonController()
player.position = Vec3(0,2,0)

#Making the definition of the cube(platform) 
class cube(Entity):
    def __init__(self,
                    position=(0,0,0)):
                super().__init__(
                    position=position,
                    model='cube',
                    scale=(1,1),
                    origin_y=.5,
                    color=color.light_gray,
                    collider='box',
                    )
#create cubes                    
cube(position=(0,1,0))

for z in range(30):
    cube(position=(random.randint(1, 6),1,z))

#main loop    
def update():
    if player.position.y <=-2:
        player.position = Vec3(0,10,0)

#ground position        
ground.position = Vec3(0,-3,0)
  
Sky()

app.run()
