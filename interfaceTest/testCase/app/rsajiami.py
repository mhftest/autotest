import rsa

# rsa加密
def rsaEncrypt(str):
    # 生成公钥、私钥
    (pubkey, privkey) = rsa.newkeys(1024)
    print(pubkey, privkey)
    # 明文编码格式
    # content = str.encode('utf-8')
    content = str.encode ('gbk')
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return (crypto, privkey)

# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con
str, pk = rsaEncrypt("a12345")
print('加密后密文：')
#print(str)
#print(pk)
content = rsaDecrypt(str, pk)
print('解密后明文：')
print(content)

p='MD9680KzfSP2FwvHIdHs5EsjGCimsJVmZ0r2oNpitRMOldTDyoPkLNpr2DonPkf64uQRc7iayzYGMmk1SR6Cyvm2lqluLLhIcnZi8Y8+aYp4mtZwJjGhoc20yCdWlcmhAfWB/WnxHVoyYeNReeJUkUprnfR8K0MZ5Hmwik4lm/w='
p2='FVZEDUzZPgwdBzSweBkoFTQd0nAr0SOFVaKEWO4HafnamyHWRMQwvntRS1zMfbUSTCCL1idBNcz7F32ecjQAdqu5+aKpPzDiiBG5BHnvkMIxJZ8cCY/I71kKYXa5pEuUQRe8ygnB2Vnbk0EtbqZ7Up3t33O0g1+Lv6vGt8SFilA='
p3='XiKhUDLPpgSYJYw9wIkjlsnEBgOTNfBmFt3M08e3qM7cpjGdgDo94XigDlzGSaZkAPifuNDSeN1SPIV93KMC+CB0R8SdSLsngStZW+swlnjiDXIG6MMoSt28Fxg/eZyXbI6hxL89Y/gJ+taqmgJRR9sTs57/OlDKp7qso3QaJEg='
# print(len(p))
# print(len(p2))