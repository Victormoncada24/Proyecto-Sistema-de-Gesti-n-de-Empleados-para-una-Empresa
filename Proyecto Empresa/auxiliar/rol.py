# ro.py
class Rol:
    def __init__(self, nombre, permisos):
        self.nombre = nombre
        self.permisos = permisos

class Autenticacion:
    def __init__(self):
        self.usuarios = {"admin": "1234"}  # Ejemplo simple de usuario

    def autenticar_usuario(self, usuario, contrasena):
        return self.usuarios.get(usuario) == contrasena

    def agregar_usuario(self, usuario, contrasena):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = contrasena

    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            del self.usuarios[usuario]
