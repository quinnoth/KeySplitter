import os, binascii
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
	length = len(s)

	s = bytearray(s)
	x = bytearray(os.urandom(length))
	y = bytearray(os.urandom(length))
	z = bytearray(os.urandom(length))

	for i in range(length):
		z[i] = s[i] ^ x[i] ^ y[i]
	
	x = binascii.hexlify(x)
	y = binascii.hexlify(y)
	z = binascii.hexlify(z)

	pieces = [x, y, z]

	return pieces

	# arrays = []
	# for i in range(number_of_pieces):
	# 	arrays.append(bytearray(os.urandom(length)))
	# for k in range(arrays):
		#xor with previous piece

# for k in range(number_of_splits, pieces):
	# for i in range length



def open_and_read_files_and_decrypt(filename1, filename2, filename3):
	f = open(filename1, 'r')
	part1 = f.read()
	f.close()
	f = open(filename2, 'r')
	part2 = f.read()
	f.close()
	f = open(filename3, 'r')
	part3 = f.read()
	f.close()
	return decrypt(part1, part2, part3)


def decrypt(x, y, z):

	s = bytearray(os.urandom(len(x) / 2)) #this is just because we need an array
	# already instantiated of the correct length
	x = bytearray(binascii.unhexlify(x))
	y = bytearray(binascii.unhexlify(y))
	z = bytearray(binascii.unhexlify(z))

	for i in range(len(x)):
		s[i] = x[i] ^ y[i] ^ z[i]

	return s.decode('utf-8')


def open_and_read_file(filename):
	#TODO: Change to "while" to prevent locking from an exception
	f = open(filename, 'r')
	file_contents = f.read()
	f.close()
	return file_contents


def write_keys_to_file(x, y, z):
	#TODO: Change to "while" to prevent locking from an exception
	f = open('secret.part1', 'w')
	f.write(x)
	f.close()
	f = open('secret.part2', 'w')
	f.write(y)
	f.close()
	f = open('secret.part3', 'w')
	f.write(z)
	f.close()


test = "This is a test!"
test_file = "test.txt"


print(open_and_read_file(test_file))
test_file_pieces = encrypt(open_and_read_file(test_file))
write_keys_to_file(test_file_pieces[0], test_file_pieces[1], test_file_pieces[2])
print(test_file_pieces[0])
print(test_file_pieces[1])
print(test_file_pieces[2])
test_file_decryption = decrypt(test_file_pieces[0], test_file_pieces[1], test_file_pieces[2])

print(open_and_read_files_and_decrypt('secret.part1', 'secret.part2', 'secret.part3'))