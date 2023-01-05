from Crypto.Cipher import AES
import base64
import os
def decrypt(encrypt_file,out_file):
    #打开加密文件
    f_read = open(encrypt_file, 'rb')
    #读取前8位获取加密头
    atmp = f_read.read(8)
    #从atmp获取加密头大小
    enc_header_size = int.from_bytes(atmp, byteorder='little', signed=True)
    #读取加密头
    encrypted = f_read.read(enc_header_size)
    #AES密钥
    key = 'aanxinci2sh3en4g'
    #初始化aes加密
    aes = AES.new(key.encode(), AES.MODE_ECB)
    #先base64后aes再gbk编码并替换填充
    decrypted = str((aes.decrypt(base64.decodebytes(encrypted))), encoding='gbk').replace('\x00', '')
    #str转字节
    decrypted = eval(decrypted)
    #打开输出文件
    dec_write = open(out_file, 'wb')
    dec_write.write(decrypted)
    #移位到没加密的后面几位
    f_read.seek(enc_header_size + 8, 0)
    #读取并写入剩余部分
    uncrypted = f_read.read(os.path.getsize(encrypt_file) - enc_header_size - 8)
    dec_write.write(uncrypted)
    dec_write.close()
    f_read.close()

if __name__ == '__main__':
    decrypt("TWRP-enc.img","TWRP-dec.img")