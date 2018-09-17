import rsa

key = rsa.newkeys (3000)  # 生成随机秘钥
privateKey = key[1]  # 私钥
publicKey = key[0]  # 公钥
message = 'a12345'
print ('Before encrypted:', message)
message = message.encode ()
cryptedMessage = rsa.encrypt (message, publicKey)
print ('After encrypted:\n', cryptedMessage)
message = rsa.decrypt (cryptedMessage, privateKey)
message = message.decode ()
print ('After decrypted:', message)
