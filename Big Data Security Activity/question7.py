def encrypt(value, key=100):
    return value + key

def decrypt(encrypted_value, key=100):
    return encrypted_value - key

salary = 50000
tax_rate = 0.10
enc_salary = encrypt(salary)
enc_tax = int(enc_salary * tax_rate)

tax_amount = decrypt(enc_tax)

print(f"Encrypted Tax Value: {enc_tax}")
print(f"Decrypted Tax Amount: ₹{tax_amount}")
