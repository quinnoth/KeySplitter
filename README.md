KeySplitter
===========
This is sort of a Secret Sharing tool (https://en.wikipedia.org/wiki/Secret_sharing) written in Python 3.2

It takes some blob of text or data, generates 2 keys and XORs them in a sequence, such that:
Z = S ^ X ^ Y
with X, Y, and Z being the secrets to be shared.

To find the original value, just reverse the sequence:
S = X ^ Y ^ Z

X & Y are generated randomly each time the algorithm is run, providing a One-Time Pad for the encryption.

os.urandom is used for the RNG. Apparently on Windows it's using CryptGenRandom (https://en.wikipedia.org/wiki/CryptGenRandom) (http://docs.python.org/2/library/os.html#os.urandom)
