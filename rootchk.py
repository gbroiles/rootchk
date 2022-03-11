#!/usr/bin/env python3
# REQUIRES Python 3.10, prior versions do not have required methods in ssl module
# thanks to Seth M. Larson for https://sethmlarson.dev/blog/experimental-python-3.10-apis-and-trust-stores
import ssl
import pprint
import socket
import sys

host = sys.argv[1]
timeout = 7

print(host, end=" ")

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
conn.settimeout(timeout)

try:
    conn.connect((host, 443))
    cert_chain = conn._sslobj.get_unverified_chain()
    print(cert_chain[-1])

except ValueError:
    print("parsing error")
    pprint.pprint(cert_chain)
except socket.gaierror:
    print("invalid hostname.")
except ssl.SSLError:
    print("SSL failed.")
except socket.timeout:
    print("timed out.")
except ConnectionRefusedError:
    print("connection refused.")
except ConnectionResetError:
    print("connection reset.")
except Exception:
    raise
