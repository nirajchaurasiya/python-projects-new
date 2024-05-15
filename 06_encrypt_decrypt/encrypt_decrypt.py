import cryptocode

encoded = cryptocode.encrypt("mystring", "mypassword")
print(f"encoded: {encoded}")
## And then to decode it:
decoded = cryptocode.decrypt(encoded, "mypassword")
print(f"decoded: {decoded}")
