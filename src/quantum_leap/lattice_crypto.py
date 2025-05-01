class LatticeCrypto:
    def encrypt(self, plaintext: str):
        return f"lattice_enc({plaintext})"

    def decrypt(self, ciphertext: str):
        return ciphertext.replace("lattice_enc(", "").rstrip(")")