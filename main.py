import hashlib

password = input("Enter password to be hashed: ")
hash_object = hashlib.sha256(password.encode("utf-8"))
hex_dig = hash_object.hexdigest()
print (hex_dig)