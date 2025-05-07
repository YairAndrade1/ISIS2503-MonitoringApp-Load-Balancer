from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64


def cargar_llave_privada():
    with open('monitoring/keys/private_key.pem', 'rb') as key_file: 
        return serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())


def cargar_llave_publica():
    with open('monitoring/keys/public_key.pem', 'rb') as key_file:
        return serialization.load_pem_public_key(key_file.read(), backend=default_backend())

def firmar_contenido(contenido: str) -> str:
    private_key = cargar_llave_privada()
    firma = private_key.sign(
        contenido.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return base64.b64encode(firma).decode()

def verificar_firma(contenido: str, firma_base64: str) -> bool:
    public_key = cargar_llave_publica()
    try:
        public_key.verify(
            base64.b64decode(firma_base64),
            contenido.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False
