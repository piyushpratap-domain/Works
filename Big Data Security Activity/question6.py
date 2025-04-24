def encrypt(num, key=10):
    return num + key

def decrypt(encrypted, key=10):
    return encrypted - key

a = 5
b = 3
enc_a = encrypt(a)
enc_b = encrypt(b)

sum_result = decrypt(enc_sum)

print(f"Encrypted sum: {enc_sum}")
print(f"Decrypted sum result: {sum_result}")
