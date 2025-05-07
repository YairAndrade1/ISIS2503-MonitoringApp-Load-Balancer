# generar_llaves.py
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import os

os.makedirs("monitoring/keys", exist_ok=True)

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

with open('monitoring/keys/private_key.pem', 'wb') as private_pem:
    private_pem.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

public_key = private_key.public_key()
with open('monitoring/keys/public_key.pem', 'wb') as public_pem:
    public_pem.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

print("Llaves generadas correctamente.")
