import base64
import os
"""
AES-128 = 16 bytes
AES-192 = 24 bytes
AES-256 = 32 bytes
1DES = 7 bytes
2DES = 14 bytes 
3DES = 21 bytes (assuming three-key triple DES)
"""
def encrypt_asymmetric_key(length):
	#generate RSA key pair
	#encode as a base64 blob together
	#send to encrypt(s)
	return False


def encrypt_symmetric_key(length):
	return encrypt(str(os.urandom(length)))


def encrypt(s):
	length = len(s) #if we try to take the length of s for the RNGs after it's been b64 encoded, they'll increase in size by 4/3rds

	s = str.encode(s) #encode in utf-8
	x = os.urandom(length)
	y = os.urandom(length)
	z = bytearray(os.urandom(length)) #cast as a bytearray, otherwise it's immutable
	for i in range(len(s)):
		z[i] = (s[i] ^ x[i]) ^ y[i]
	
	pieces = [base64.b64encode(x), base64.b64encode(y), base64.b64encode(z)]

	return pieces


def decrypt(x, y, z):
	s = bytearray(os.urandom(len(base64.b64decode(x)))) #the real length needs to be 4/3rds. I also need to figure out how to instantiate mutable byte arrays.
	
	x = base64.b64decode(x)
	y = base64.b64decode(y)
	z = base64.b64decode(z)
	
	for i in range(len(x)):
		s[i] = (x[i] ^ y[i]) ^ z[i]
	
	return s.decode()


def open_and_read_file(filename):
	f = open(filename, 'r')
	text = f.read()
	f.close()
	return text


def write_keys_to_file(x, y, z):
	f = open('secret.part1', 'w')
	f.write(str(x)) #still writes the b'' into the file, so i'll need to resolve that.
	f.close()
	f = open('secret.part2', 'w')
	f.write(str(y))
	f.close()
	f = open('secret.part3', 'w')
	f.write(str(z))
	f.close()

test = "This is a test!"
test_file = "test.txt"

#test with just providing a string
print(test)
test_pieces = encrypt(test)
#test_pieces = encrypt_symmetric_key(10)
print(test_pieces[0])
print(test_pieces[1])
print(test_pieces[2])
test_decryption = decrypt(test_pieces[0], test_pieces[1], test_pieces[2])
print(test_decryption)


print(open_and_read_file(test_file))
test_file_pieces = encrypt(open_and_read_file(test_file))
write_keys_to_file(test_file_pieces[0], test_file_pieces[1], test_file_pieces[2])
print(test_file_pieces[0])
print(test_file_pieces[1])
print(test_file_pieces[2])
test_file_decryption = decrypt(test_file_pieces[0], test_file_pieces[1], test_file_pieces[2])
print(test_file_decryption)