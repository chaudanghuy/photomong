from django.shortcuts import render
import requests
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from time import time
from datetime import datetime
import json, hmac, hashlib, urllib.request, urllib, urllib.parse, random
from revenue.models import Transaction, Order
from device.models import Device


# Create your views here.
class ZaloPayAPI(APIView):

    def get(self, request, *args, **kwargs):
        config = {
            "app_id": 2553,
            "key1": "PcY4iZIKFCIdgZvA6ueMcMHHUbRLYjPL",
            "key2": "kLtgPl8HHhfvMuDHPwKfgfsY4Ydm9eIz",
            "endpoint": "https://sb-openapi.zalopay.vn/v2/create",
        }

        transID = random.randrange(1000000)

        order = {
            "app_id": config["app_id"],
            "app_trans_id": "{:%y%m%d}_{}".format(
                datetime.today(), transID
            ),  # mã giao dich có định dạng yyMMdd_xxxx
            "app_user": "user123",
            "app_time": int(round(time() * 1000)),  # miliseconds
            "embed_data": json.dumps({}),
            "item": json.dumps([{}]),
            "amount": request.GET.get("amount") or 100000,
            "description": "PhotoMong - Payment for the order #" + str(transID),
            "bank_code": "zalopayapp",
        }

        # app_id|app_trans_id|app_user|amount|apptime|embed_data|item
        data = "{}|{}|{}|{}|{}|{}|{}".format(
            order["app_id"],
            order["app_trans_id"],
            order["app_user"],
            order["amount"],
            order["app_time"],
            order["embed_data"],
            order["item"],
        )

        order["mac"] = hmac.new(
            config["key1"].encode(), data.encode(), hashlib.sha256
        ).hexdigest()

        response = urllib.request.urlopen(
            url=config["endpoint"], data=urllib.parse.urlencode(order).encode()
        )

        # Find device
        device_code = request.GET.get("device")
        if device_code:
            device = Device.objects.filter(code=device_code).first()
        else:
            device = None

        orderObject = Order.objects.create(
            order_code=order["app_trans_id"],
            device_id=device,
            product_price=order["amount"],
            base_price=0,
            tax=0,
            total_price=order["amount"],
            status="Pending",
        )

        result = json.loads(response.read())
        
        result_response = {
            "order_code": order["app_trans_id"],
            "return_message": result.get("return_message"),
            "qr_code": result.get("qr_code"),
            "order_url": result.get("order_url"),
            "return_code": result.get("return_code")
        }
        
        return Response(result_response, status=status.HTTP_200_OK)        


class ZaloPayUpdateAPI(APIView):
    def post(self, request, order_code, *args, **kwargs):                
        status = request.data.get("status")
        if order_code:
            order = Order.objects.filter(order_code=order_code).first()
            if order:
                order.status = status
                order.save()
        return Response(status=status.HTTP_200_OK)


class ZaloPayWebhookAPI(APIView):

    def get(self, request, *args, **kwargs):        
        # Get order code
        device_code = request.GET.get("device")
        if device_code:
            device = Device.objects.filter(code=device_code).first()
            if device:
                order = Order.objects.filter(device_id=device).first()
                result = {
                    "status": "Success",
                }
                return Response(result, status=status.HTTP_200_OK)        
        
        config = {
            "app_id": 2553,
            "key1": "PcY4iZIKFCIdgZvA6ueMcMHHUbRLYjPL",
            "key2": "kLtgPl8HHhfvMuDHPwKfgfsY4Ydm9eIz",
            "endpoint": "https://sb-openapi.zalopay.vn/v2/query",
        }

        params = {
            "app_id": config["app_id"],
            "app_trans_id": order.order_code,  # Input your app_trans_id"
        }

        data = "{}|{}|{}".format(
            config["app_id"], params["app_trans_id"], config["key1"]
        )  # app_id|app_trans_id|key1
        params["mac"] = hmac.new(
            config["key1"].encode(), data.encode(), hashlib.sha256
        ).hexdigest()

        response = urllib.request.urlopen(
            url=config["endpoint"], data=urllib.parse.urlencode(params).encode()
        )
        result = json.loads(response.read())
        
        
        if result.get("return_code") == 1:
            order.status = "Success"
        elif result.get("return_code") == 2:
            order.status = "Fail"
        elif result.get("return_code") == 3:
            order.status = "Processing"
        order.save()
        
        # Debug
        order.status = "Success"
        
        result_response = {
            "order_code": order.order_code,
            "return_message": result.get("return_message"),            
            "return_code": result.get("return_code"),
            "status": order.status
        }


        return Response(result_response, status=status.HTTP_200_OK)