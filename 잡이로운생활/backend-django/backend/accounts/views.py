from django.shortcuts import render, get_object_or_404
from .models import User, Transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, ItemListSerializer, TransListSerializer
from rest_framework.response import Response
from django.core.mail import EmailMessage
from articles.models import Article
from django.db.models import Q

import random
import json
import sys
import time
import os

from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from solc import compile_source


blockchain_address = 'http://127.0.0.1:8545'
web3 = Web3(HTTPProvider(blockchain_address))
# Path to the compiled contract JSON file
compiled_contract_cash_path = './dev/truffle/build/contracts/Cash.json'
compiled_contract_purchaserecord_path = './dev/truffle/build/contracts/PurchaseRecord.json'
# Deployed contract address (see `migrate` command output: `contract address`)
CASH_CONTRACT_ADDRESS  = '0xc3F21414ACa813075c205306cb566D175cE1213F'
PURCHASE_RECORD_CONTRACT_ADDRESS  = '0xedEdC142D938fc2c09f0CA35c388b0b14BA26781'

with open(compiled_contract_cash_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
# fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']
# Create your views here.
# Fetch deployed contract reference
contract_cash = web3.eth.contract(address=CASH_CONTRACT_ADDRESS,
                             abi=contract_abi, bytecode=contract_json['bytecode'])

with open(compiled_contract_purchaserecord_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
# fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']
# Create your views here.
# Fetch deployed contract reference
contract_purchaserecord = web3.eth.contract(address=PURCHASE_RECORD_CONTRACT_ADDRESS,
                             abi=contract_abi, bytecode=contract_json['bytecode'])

# 회원가입


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_flag(request, flag):
    request.user.flag = flag
    request.user.save()
    return Response({'message': '성공적으로 제출되었습니다.'})

@api_view(['POST'])
def email(request, email):
    number = random.randint(100000, 1000000)
    subject_text = 'JOB!이로운생활 회원가입 인증입니다 확인해 주세요.'
    body_text = f'''회원가입를 위한 이메일인증 절차입니다 하단의 번호를 JOB!이로운생활 화면에 입력해 주세요
                인증번호: {number}\
                인증번호를 다른사람이 보지 않게 주의해 주세요.'''

    email = EmailMessage(subject_text, body_text, to=[email])
    result = email.send()

    if result == 1:
        return Response({"result": number, "1": result})
    else:
        return Response({"result": mqwmenjkcjxzkjqwnebmnsdbhqwbhqkbbxjcbkqjkcxzcq})

# 지갑정보


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wallet_create(request, password):
    user = request.user
    # truffle development blockchain address

    # Client instance to interact with the blockchain

    # Set the default account (so we don't need to set the "from" for every transaction call)
    web3.geth.personal.unlockAccount(web3.eth.accounts[0], "asd", 0)
    addr = web3.geth.personal.newAccount(password)

    path = "./dev/keystore"
    file_list = os.listdir(path)
    for i in range(len(file_list)):
        file_name = file_list[i]
        if addr[2:].lower() in file_name:
            with open('./dev/keystore/'+file_name) as keyfile:
                encrypted_key = keyfile.read()
                private_key = web3.eth.account.decrypt(
                    encrypted_key, password)  # '123'은 개인 password

    web3.eth.sendTransaction(
        {'to': addr, 'from': web3.eth.coinbase, 'value': web3.toWei(5, "ether")})

    tx_hash = web3.eth.getBlock(
        block_identifier='pending', full_transactions=True)
    pending_transactions = tx_hash['transactions']

    web3.geth.miner.start(4)
    time.sleep(3)
    web3.geth.miner.stop()

    web3.geth.miner.start(4)
    time.sleep(3)
    web3.geth.miner.stop()

    transact = web3.eth.getTransactionReceipt(
        pending_transactions[0]['hash'].hex())
    user.wallet_addr = addr
    user.balance = web3.fromWei(web3.eth.getBalance(addr), "microether")
    user.save()

    Transaction.objects.create(
        tx_hash=pending_transactions[0]['hash'].hex(),
        blockHash=transact['blockHash'].hex(),
        blockNumber=pending_transactions[0]['blockNumber'],
        from_adrr=pending_transactions[0]['from'],
        to_addr=pending_transactions[0]['to'],
        from_pk=0,
        to_pk=user.id,
        gas=pending_transactions[0]['gas'],
        gasPrice=pending_transactions[0]['gasPrice'],
        nonce=pending_transactions[0]['nonce'],
        r=pending_transactions[0]['r'].hex(),
        s=pending_transactions[0]['s'].hex(),
        v=pending_transactions[0]['v'],
        value=web3.fromWei(pending_transactions[0]['value'], "microether")
    )

    return Response({"result": private_key.hex()})


@api_view(['GET'])
def wallet_read(request, id):
    user = get_object_or_404(User, pk=id)
    serializer = UserSerializer(user)
    return Response({"result": serializer.data})


# 아이템 구매

# 자격증 등록
@api_view(['POST'])
def register(request, id):
    user = request.user
    # truffle development blockchain address
    web3.geth.personal.unlockAccount(web3.eth.accounts[0], "asd", 0)
    with open('./dev/keystore/UTC--2020-10-06T14-09-06.079950600Z--565afde033d6d2df643b5fa6d02d17f5efb2a3bb') as keyfile:
        encrypted_key = keyfile.read()
        private_key = web3.eth.account.decrypt(
            encrypted_key, 'asd')  # '123'은 개인 password

    addr = user.wallet_addr
    web3.eth.sendTransaction(
        {'to': addr, 'from': web3.eth.coinbase, 'value': web3.toWei(1, "ether")})

    tx_hash = web3.eth.getBlock(
        block_identifier='pending', full_transactions=True)
    pending_transactions = tx_hash['transactions']

    web3.geth.miner.start(4)
    time.sleep(3)
    web3.geth.miner.stop()

    web3.geth.miner.start(4)
    time.sleep(3)
    web3.geth.miner.stop()
    transact = web3.eth.getTransactionReceipt(
        pending_transactions[0]['hash'].hex())

    Transaction.objects.create(
        tx_hash=pending_transactions[0]['hash'].hex(),
        blockHash=transact['blockHash'].hex(),
        blockNumber=pending_transactions[0]['blockNumber'],
        from_adrr=pending_transactions[0]['from'],
        to_addr=pending_transactions[0]['to'],
        from_pk=0,
        to_pk=user.id,
        gas=pending_transactions[0]['gas'],
        gasPrice=pending_transactions[0]['gasPrice'],
        nonce=pending_transactions[0]['nonce'],
        r=pending_transactions[0]['r'].hex(),
        s=pending_transactions[0]['s'].hex(),
        v=pending_transactions[0]['v'],
        value=web3.fromWei(pending_transactions[0]['value'], "microether")
    )

    # user.balance = web3.fromWei(web3.eth.getBalance(addr), "ether")
    user.balance = web3.fromWei(web3.eth.getBalance(addr), "microether")
    user.save()

    return Response({"result": "sucess"})


# 아이템 조회
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def item_read(request):
    user = request.user
    articles = Article.objects.filter(buyer=user).order_by('-pk')
    serializer = ItemListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def item_read_ather(request, id):
    user = request.user
    article = get_object_or_404(Article, pk=id)
    if article.buyer.filter(id=request.user.pk).exists():
        return Response({ "result": 1})
    else:
        return Response({ "result": 0})

# 아이템 구매


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def item_purchase(request, id):
    pwd = request.data['password']
    key = request.data['private_key']
    article = get_object_or_404(Article, pk=id)
    another = get_object_or_404(User, pk=article.user_id)
    print(pwd, 1)
    print(key, 2)
    if article.buyer.filter(id=request.user.pk).exists():
        pass
    else:
        user = request.user
        try:
            web3.geth.personal.unlockAccount(user.wallet_addr, pwd, 0)
        except Exception:
            return Response({'result': 'fail'})
        # Path to the compiled contract JSON file
        path = "./dev/keystore"
        file_list = os.listdir(path)
        for i in range(len(file_list)):
            file_name = file_list[i]
            if user.wallet_addr[2:].lower() in file_name:
                with open('./dev/keystore/'+file_name) as keyfile:
                    encrypted_key = keyfile.read()
                    private_key = web3.eth.account.decrypt(
                        encrypted_key, pwd)
                if private_key.hex() == key:
                    print("sucess")
                    web3.eth.sendTransaction(
                        {'to': another.wallet_addr, 'from': user.wallet_addr, 'value': web3.toWei(1, "ether")})
                else: 
                    return Response({'result': 'fail'})
        tx_hash = web3.eth.getBlock(
            block_identifier='pending', full_transactions=True)
        pending_transactions = tx_hash['transactions']

        web3.geth.miner.start(4)
        time.sleep(3)
        web3.geth.miner.stop()

        web3.geth.miner.start(4)
        time.sleep(3)
        web3.geth.miner.stop()

        transact = web3.eth.getTransactionReceipt(
            pending_transactions[0]['hash'].hex())
        # user.balance = web3.fromWei(web3.eth.getBalance(user.wallet_addr), "ether")
        user.balance = web3.fromWei(
            web3.eth.getBalance(user.wallet_addr), "microether")

        # another.balance = web3.fromWei(web3.eth.getBalance(another.wallet_addr), "ether")
        another.balance = web3.fromWei(
            web3.eth.getBalance(another.wallet_addr), "microether")
        article.buyer.add(request.user)
        user.save()
        another.save()

        Transaction.objects.create(
            tx_hash=pending_transactions[0]['hash'].hex(),
            blockHash=transact['blockHash'].hex(),
            blockNumber=pending_transactions[0]['blockNumber'],
            from_adrr=pending_transactions[0]['from'],
            to_addr=pending_transactions[0]['to'],
            from_pk=user.id,
            to_pk=another.id,
            gas=pending_transactions[0]['gas'],
            gasPrice=pending_transactions[0]['gasPrice'],
            nonce=pending_transactions[0]['nonce'],
            r=pending_transactions[0]['r'].hex(),
            s=pending_transactions[0]['s'].hex(),
            v=pending_transactions[0]['v'],
            value=web3.fromWei(pending_transactions[0]['value'], "microether")
        )

    serializer = ItemListSerializer(article)

    return Response(serializer.data)

## 영상 구매
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def video_purchase(request, id):
    pwd = request.data['password']
    key = request.data['private_key']
    print(pwd, 1)
    print(key, 2)

    user = request.user
    try:
        web3.geth.personal.unlockAccount(user.wallet_addr, pwd, 0)
    except Exception:
        return Response({'result': 'fail'})
    # Path to the compiled contract JSON file
    path = "./dev/keystore"
    file_list = os.listdir(path)
    for i in range(len(file_list)):
        file_name = file_list[i]
        if user.wallet_addr[2:].lower() in file_name:
            with open('./dev/keystore/'+file_name) as keyfile:
                encrypted_key = keyfile.read()
                private_key = web3.eth.account.decrypt(
                    encrypted_key, pwd)
            if private_key.hex() == key:
                print("sucess")
                web3.eth.sendTransaction(
                    {'to': web3.eth.accounts[0], 'from': user.wallet_addr, 'value': web3.toWei(1, "ether")})
            else: 
                return Response({'result': 'fail'})

    tx_hash = web3.eth.getBlock(
        block_identifier='pending', full_transactions=True)
    pending_transactions = tx_hash['transactions']

    web3.geth.miner.start(4)
    time.sleep(3)
    web3.geth.miner.stop()

    web3.geth.miner.start(4)
    time.sleep(3)
    web3.geth.miner.stop()

    transact = web3.eth.getTransactionReceipt(
        pending_transactions[0]['hash'].hex())
    # user.balance = web3.fromWei(web3.eth.getBalance(user.wallet_addr), "ether")
    user.balance = web3.fromWei(
        web3.eth.getBalance(user.wallet_addr), "microether")

    # another.balance = web3.fromWei(web3.eth.getBalance(another.wallet_addr), "ether")
    if request.data['video'] == 'IT':
        user.it = 1
    elif request.data['video'] == '전자':
        user.electric = 1
    elif request.data['video'] == '반도체':
        user.semiconductor = 1
    elif request.data['video'] == '디자인':
        user.design = 1
    else:
        user.eng = 1
    user.save()

    Transaction.objects.create(
        tx_hash=pending_transactions[0]['hash'].hex(),
        blockHash=transact['blockHash'].hex(),
        blockNumber=pending_transactions[0]['blockNumber'],
        from_adrr=pending_transactions[0]['from'],
        to_addr=pending_transactions[0]['to'],
        from_pk=user.id,
        to_pk=0,
        gas=pending_transactions[0]['gas'],
        gasPrice=pending_transactions[0]['gasPrice'],
        nonce=pending_transactions[0]['nonce'],
        r=pending_transactions[0]['r'].hex(),
        s=pending_transactions[0]['s'].hex(),
        v=pending_transactions[0]['v'],
        value=web3.fromWei(pending_transactions[0]['value'], "microether")
    )


    return Response({"result": "sucess"})

## 내역 조회

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def trans(request):
    user = request.user
    print(user)
    trans = Transaction.objects.filter(Q(from_pk=user.id) | Q(to_pk=user.id)).order_by('-pk')
    serializer = TransListSerializer(trans, many=True)

    return Response(serializer.data)