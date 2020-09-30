"""
Maria Ines Vasquez Figueroa
18250
Gráficas
DR2 Lights & Shadows
Sphere
"""

import numpy as np
from gl import *
from mathLib import *


WHITE = color(1,1,1)

class Material(object):
    # Un material como visto en Unity que rige como se comportara con la luz. Como los materiales de roca, ladrillo, entre otros
    def __init__(self, diffuse = WHITE, spec = 0):
        # color pero se esparce cuando tiene luz
        self.diffuse = diffuse
        self.spec = spec


class Intersect(object): #función que devuelve la distancia de la intersección
    def __init__(self, distance, point, normal, sceneObject):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject

class AmbientLight(object):
    def __init__(self, strength = 0, _color = WHITE):
        self.strength = strength
        self.color = _color

class PointLight(object):
    def __init__(self, position = (0,0,0), _color = WHITE, intensity = 1):
        self.position = position
        self.intensity = intensity
        self.color = _color


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        
        # Regresa falso o verdadero si hace interseccion con una esfera

        # Formula para un punto en un rayo
        # t es igual a la distancia en el rayo
        # P = O + tD
        # P0 = O + t0 * D
        # P1 = O + t1 * D
        #d va a ser la magnitud de un vector que es
        #perpendicular entre el rayo y el centro de la esfera
        # d > radio, el rayo no intersecta
        #tca es el vector que va del orign al punto perpendicular al centro
        #L = np.subtract(self.center, orig)
        Lp=subtract(self.center[0],orig[0],self.center[1],orig[1],self.center[2],orig[2])#funciona
        
       
        tcap=dot(Lp,dir[0], dir[1], dir[2])#funciona
        
        lp=frobenius(Lp) #funciona magnitud de L
        
        d = (lp**2 - tcap**2) ** 0.5
        if d > self.radius:
            return None

        # thc es la distancia de P1 al punto perpendicular al centro
        thc = (self.radius ** 2 - d**2) ** 0.5
        t0 = tcap - thc
        t1 = tcap + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0: # t0 tiene el valor de t1
            return None
        #hit = np.add(orig, t0 * np.array(dir))
        """print(orig)
        print(t0 * np.array(dir))
        print(hit)
        print(add(orig, multiN(t0,dir)))"""
        hitp=add(orig, multiN(t0,dir))
        #print("-------------------------------------------------------")

        #norm = np.subtract( hit, self.center )
        norm2=subtract(hitp[0], self.center[0],hitp[1],self.center[1],hitp[2],self.center[2])#funciona
        #norm = norm / np.linalg.norm(norm)
        norm2=division(norm2, frobenius(norm2))
        """print(norm)
        print(norm2)"""

        return Intersect(distance = t0,
                         point = hitp,
                         normal = norm2,
                         sceneObject = self)

