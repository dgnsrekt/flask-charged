from lnd_grpc import Client
from pathlib import Path
from models import Invoice

ROOT = Path(__file__).parent

macaroon = ROOT / "admin.macaroon"
tls = ROOT / "tls.cert"

assert macaroon.exists()
assert tls.exists()

c = Client(
    macaroon_path=str(macaroon),
    tls_cert_path=str(tls),
    network="testnet",
    grpc_host="127.0.0.1",
    grpc_port="10009",
)
MEMO = "THIS IS A MEMO"

print(c.get_info())
inv = c.add_invoice(memo=MEMO, value=100)
print(inv.r_hash, type(inv.r_hash))
print(inv.payment_request, type(inv.payment_request))
print(inv.add_index, type(inv.add_index))

decoded = c.decode_pay_req(pay_req=inv.payment_request)
print(decoded)
print(decoded.description)
print(decoded.timestamp, type(decoded.timestamp))
print(decoded.expiry, type(decoded.expiry))
print(decoded.cltv_expiry, type(decoded.cltv_expiry))

Invoice.drop_table()
Invoice.create_table()
Invoice.create(
    r_hash=b"hashy123",
    r_hash_string="hash2ys",
    payment_request="sdfyasxyfjlkjl",
    satoshi_amount=100,
    description="this isfdsk a pyament",
    add_index=20,
)
