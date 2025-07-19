import sqlite3
from contacto import Contacto
from sqlite3 import OperationalError, IntegrityError
import logging

# Constante con la ruta de la base de datos
NOMBRE_BD = "./src/Proyecto/contactos.db"

# Constante con la ruta del archivo de log
LOG_PATH = "./src/Proyecto/app.log"

class DaoContacto:
    def __init__(self, nombre_bd=NOMBRE_BD):
        # Establece la conexion a la base de datos y configura el log
        self.conn = sqlite3.connect(nombre_bd)
        self.logging_conf()
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def logging_conf(self):
        # Configura el sistema de logging para escribir mensajes en un archivo
        logging.basicConfig(
            level=logging.DEBUG,
            filename=LOG_PATH,
            filemode="a"
        )
        
    def alta_contacto(self, contacto: Contacto):
        # Inserta un nuevo contacto en la base de datos
        with self.conn:
            try:
                self.logger.fatal("Entramos al metodo de guardado")
                cursor = self.conn.cursor()
                cursor.execute("""
                    INSERT INTO contact (nombre, primer_apellido, segundo_apellido, email)
                    VALUES(?, ?, ?, ?)                  
                """, (contacto.nombre, contacto.primer_apellido, contacto.segundo_apellido, contacto.email))
                
                self.conn.commit()

                # Devuelve el ID del nuevo registro insertado
                return cursor.lastrowid

            except IntegrityError:
                # Maneja errores de violacion de integridad
                raise Exception("Ocurrio un error en la integridad de los datos al insertar")
            except OperationalError:
                # Maneja errores operacionales
                self.logger.error("Ocurrio un error al guardar")
                raise Exception("Ocurrio un error en el proceso de insercion.")
            except Exception:
                # Maneja cualquier otro tipo de error
                raise Exception("Ocurrio un error desconocido")
                
    def baja_contacto(self, id_contacto):
        # Elimina un contacto de la base de datos segun su ID
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacto WHERE id = ?", (id_contacto,))
        contacto = cursor.fetchone()
        
        if contacto:
            cursor.execute("DELETE FROM contacto WHERE id = ?", (id_contacto,))
            self.conn.commit()
            return True

        # Si no se encuentra el contacto, devuelve False
        return False
    
    def actualiza_contacto(self, id_contacto, campo, nuevo_valor):
        # Actualiza un campo especifico de un contacto segun su ID
        with self.conn:
            self.conn.execute(f"""
                UPDATE contacto SET {campo} = ? WHERE id = ?               
            """, (nuevo_valor, id_contacto))

    def mostrar_todos(self):
        # Recupera todos los contactos ordenados por ID
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM contacto ORDER BY id")
        self.conn.commit()
        return cursor.fetchall()

    def buscar_por_nombre(self, nombre):
        # Busca contactos cuyo nombre contenga una cadena especifica
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM contacto WHERE nombre LIKE ? ORDER BY id', (f"%{nombre}%",))
        return cursor.fetchall()
    
    def cerrar_conexion(self):
        # Cierra la conexion con la base de datos (duplicada por error)
        self.conn.close()
        self.conn.close()
