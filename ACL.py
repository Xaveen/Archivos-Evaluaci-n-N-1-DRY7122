aclnum = int(input("Cual es el numero IPV4 ACL?"))
if aclnum >= 1 and aclnum <= 99:
    print("Esta es una ACL IPV4 Estandar")
elif aclnum >= 100 and aclnum <= 199:
    print("Esta es una ACL IPV4 Extendida")
else:
    print("No es una ACl Estandar o Extendida")