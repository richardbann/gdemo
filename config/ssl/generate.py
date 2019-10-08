#!.venv/bin/python

import random
import os

from OpenSSL import crypto, SSL


CERT_NOT_AFTER = 3 * 365 * 24 * 60 * 60


def consistent(key, cert):
    keypub = key.to_cryptography_key().public_key().public_numbers()
    certpub = cert.get_pubkey().to_cryptography_key().public_numbers()
    if keypub != certpub:
        return False
    return True


def make_cert(certname):
    cert = crypto.X509()
    cert.set_serial_number(random.randint(0, 2 ** 64 - 1))
    cert.get_subject().CN = certname

    cert.set_version(2)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(CERT_NOT_AFTER)
    return cert


def generate(names, ips=None, cakeyfile=None, cacertfile=None, dest=""):
    ips = ips or []
    if cakeyfile is None and cacertfile:
        raise Exception("cacertfile wihtout cakeyfile")

    cn = names[0]
    base = os.path.join(dest, "ssl")

    if cakeyfile:
        with open(cakeyfile, "rb") as f:
            buf = f.read()
            cakey = crypto.load_privatekey(SSL.FILETYPE_PEM, buf)
    else:
        cakey = crypto.PKey()
        cakey.generate_key(crypto.TYPE_RSA, 2048)
        with open(f"{base}_CA.key", "wb") as f:
            f.write(crypto.dump_privatekey(SSL.FILETYPE_PEM, cakey))

    if cacertfile:
        with open(cacertfile, "rb") as f:
            buf = f.read()
            cacert = crypto.load_certificate(SSL.FILETYPE_PEM, buf)
    else:
        cacert = make_cert(f"{cn}")
        cacert.set_issuer(cacert.get_subject())
        cacert.set_pubkey(cakey)
        cacert.add_extensions([
            crypto.X509Extension(b"basicConstraints", True, b"CA:TRUE, pathlen:0"),
            crypto.X509Extension(b"keyUsage", True, b"keyCertSign, cRLSign"),
            crypto.X509Extension(
                b"subjectKeyIdentifier", False, b"hash", subject=cacert
            ),
        ])
        cacert.sign(cakey, "sha256")
        with open(f"{base}_CA.crt", "wb") as f:
            f.write(crypto.dump_certificate(SSL.FILETYPE_PEM, cacert))

    if not consistent(cakey, cacert):
        raise Exception("the CA private key and the certificate are not consistent")

    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)
    with open(f"{base}.key", "wb") as f:
        f.write(crypto.dump_privatekey(SSL.FILETYPE_PEM, key))

    req = crypto.X509Req()
    req.get_subject().CN = cn
    req.set_pubkey(key)
    req.sign(key, "sha256")

    cert = make_cert(cn)
    cert.set_issuer(cacert.get_subject())
    cert.set_pubkey(req.get_pubkey())

    altnames = [f"DNS:{n}" for n in names] + [f"IP:{i}" for i in ips]
    altnames = ",".join(altnames)
    cert.add_extensions([
        crypto.X509Extension(b'subjectAltName', False, altnames.encode()),
        crypto.X509Extension(b'extendedKeyUsage', False, b"serverAuth,clientAuth"),
    ])
    cert.sign(cakey, "sha256")
    with open(f"{base}.crt", "wb") as f:
        f.write(crypto.dump_certificate(SSL.FILETYPE_PEM, cert))


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    generate(
        [x.strip() for x in os.environ.get("HOST_NAMES").split(",")],
        ips=["127.0.0.1"],
        dest="config/ssl"
    )
