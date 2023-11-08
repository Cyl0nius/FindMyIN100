#python2
#extened by in100 payload
import sys,base64,hashlib,random
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

in100_pl = bytearray(31)
in100_mac = bytearray(6)
dummy = bytearray(1)

def int_to_bytes(n, length, endianess='big'):
    h = '%x' % n
    s = ('0'*(len(h) % 2) + h).zfill(length*2).decode('hex')
    return s if endianess == 'big' else s[::-1]

def sha256(data):
    digest = hashlib.new("sha256")
    digest.update(data)
    return digest.digest()

priv = random.getrandbits(224)
adv = ec.derive_private_key(priv, ec.SECP224R1(), default_backend()).public_key().public_numbers().x

priv_bytes = int_to_bytes(priv, 28)
adv_bytes = int_to_bytes(adv, 28)

priv_b64 = base64.b64encode(priv_bytes).decode("ascii")
adv_b64 = base64.b64encode(adv_bytes).decode("ascii")
s256_b64 = base64.b64encode(sha256(adv_bytes)).decode("ascii")

if '/' in s256_b64[:7]:
    print('invalid key file generated, try again')
    exit()
else:
    fname = '%s.keys' % s256_b64[:7]
    
in100_pl[0:] = "\x1e\xff\x4c\x00\x12\x19\x00"
in100_mac[0:] = adv_bytes[0:6]
print("*raw device address:"),
print(''.join(format(x, '02x') for x in in100_mac)) 
val = (in100_mac[0] | 0b11000000)
in100_mac[0] = val
in100_pl[7:22] = adv_bytes[6:29] 
dummy[0] = adv_bytes[0]
val = (dummy[0] >> 6)
in100_pl.append(val)
in100_pl.append("\x00")

#in100_pl[0:] = in100_pl[0:31]
    
print('file_name: %s' % fname)
print('private_key: %s' % priv_b64)
print('advertisement_key: %s' % adv_b64)
print('hashed_adv_key: %s' % s256_b64)
print('*in100_mac:'),
print(''.join(format(x, '02x') for x in in100_mac))
print('*in100_payload:'),
print(''.join(format(x, '02x') for x in in100_pl)) 
print('*lenght of payload:'),
print(len(in100_pl))   

with open(fname, 'w') as f:
    f.write('private_key: %s\n' % priv_b64)
    f.write('advertisement_key: %s\n' % adv_b64)
    f.write('hashed_adv_key: %s\n' % s256_b64)
    f.write('in100_mac: ')
    f.write(''.join(format(x, '02x') for x in in100_mac))
    f.write('\nin100_payload: ')
    f.write(''.join(format(x, '02x') for x in in100_pl)) 