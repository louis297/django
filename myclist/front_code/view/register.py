import hashlib
import binascii
import base64
import os
from ..param import global_setting
from django.shortcuts import render
from django.http import HttpResponse

dk_len = global_setting['password_hash_length']
salt_len = global_setting['password_salt_length']
password_encrypt_version = global_setting['password_encrypt_version']
iterations = global_setting['password_iteration']


def pbkdf2(salt, password):
    dk = hashlib.pbkdf2_hmac(hashlib.sha512().name, password.encode('utf8'),
                             base64.b16decode(salt.upper()), iterations, dk_len)
    return binascii.hexlify(dk)


def encrypt_pass(password):
    salt = binascii.hexlify(os.urandom(salt_len))
    encrypted_pass = pbkdf2(salt, password)
    return password_encrypt_version, iterations, salt, encrypted_pass


def register(request):
    if request.method == 'POST':
        return register_user(request)
    elif request.method == 'GET':
        # return HttpResponse('test test')
        return register_page()


# POST method, will save user info to DB
def register_user(request):
    # get all info
    # POST dict key is "name" attribute of form items
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    password_encrypt_version, iterations, salt, encrypted_pass = encrypt_pass(password)


    # return register status to frontend
    # redirect will be done by client-side JS script
    return


# GET method, will return the html page
def register_page():
    pass
