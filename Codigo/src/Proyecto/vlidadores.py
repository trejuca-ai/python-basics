from pydantic import BaseModel, field_validator
from email_validator import EmailNotValidError, validate_email

class ContactoValidator(BaseModel):
    # Define el modelo de validacion para los datos de un contacto
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    email: str

    @field_validator("nombre", "primer_apellido", "segundo_apellido", "email")
    def min_length_valid(cls, value, field):
        # Valida que el campo no este vacio
        if len(value) <= 0:
            raise ValueError("El campo es obligatorio")
        return value

    @field_validator("email")
    def email_valid(cls, value, field):
        # Valida que el correo electronico tenga un formato correcto
        try:
            validate_email(value)
        except EmailNotValidError:
            raise ValueError(f"El campo {field.field_name} no valido")
