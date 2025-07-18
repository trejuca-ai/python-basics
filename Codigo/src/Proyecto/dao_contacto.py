import sqlite3
from contacto import Contacto

NOMBRE_BD = "./src/Proyecto/contactos.db"
class DaoContacto:
    def __init__(self, nombre_bd=NOMBRE_BD):
        self.conn = sqlite3.connect(nombre_bd)
        
    def alta_contacto(self, contacto: Contacto):
        with self.conn:
            self.conn.execute("""
                INSERT INTO contacto (nombre, primer_apellido, segundo_apellido, email)
                VALUES(?, ?, ? ,?)                  
            """, (contacto.nombre, contacto.primer_apellido, contacto.segundo_apellido, contacto.email))
        
