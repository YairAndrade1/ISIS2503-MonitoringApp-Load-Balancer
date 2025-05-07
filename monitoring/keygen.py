
from cryptography.hazmat.primitives import serialization
import rsa

# Generación de llaves con cryptography
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Guardado de las llaves en archivos PEM
with open('private_key.pem', 'wb') as private_pem:
    private_pem.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

public_key = private_key.public_key()
with open('public_key.pem', 'wb') as public_pem:
    public_pem.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )
