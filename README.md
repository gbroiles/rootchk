# rootchk
Python script to identify root CA for TLS certificate used by a website

usage:

    python3 rootchk.py www.google.com
    
Thanks to Seth Michael Larson for writing up https://sethmlarson.dev/blog/experimental-python-3.10-apis-and-trust-stores

This code *requires* Python 3.10 (or later) because that version introduced additional certificate functions in the ssl module. 
