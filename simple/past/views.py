from django.shortcuts import render
from .models import Message, UnMessage
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime


class decode(APIView):
    def get(self, request):
        mes = request.GET.get('message')
        rot = int(request.GET.get('rot'))
        m = UnMessage()
        m.zac = mes
        m.rot = rot
        m.ish = ''
        for i in m.zac:
            if 65 + m.rot <= ord(i) <= 90:
                m.ish += chr(ord(i) - m.rot)
            elif 64 < ord(i) <= 64+m.rot:
                m.ish += chr(ord(i) - m.rot + 36)
            elif 97 + m.rot <= ord(i) <= 122:
                m.ish += chr(ord(i) - m.rot)
            elif 96 < ord(i) <= 96+m.rot:
                m.ish += chr(ord(i) - m.rot + 36)
        return Response({"message": m.ish})



class encode(APIView):
    def post(self, request):
        mes = Message()
        mes.ish = request.data.get("message")
        mes.rot = int(request.data.get('rot'))
        mes.zac = ''
        for i in mes.ish:
            if 65 <= ord(i) <= 90 - mes.rot:
                mes.zac += chr(ord(i) + mes.rot)
            elif 90 - mes.rot < ord(i) <= 90:
                mes.zac += chr(ord(i) + mes.rot - 36)
            elif 97 <= ord(i) <= 122 - mes.rot:
                mes.zac += chr(ord(i) + mes.rot)
            elif 122 - mes.rot < ord(i) <= 122:
                mes.zac += chr(ord(i) + mes.rot - 36)
        mes.save()
        return Response({'message': mes.zac})


class stats(APIView):
    def get(self, request):
        a = []
        b = Message.objects.filter(date=str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day))
        c = [0]*27
        for i in b:
            c[i.rot]+=1
        for i in range(1, 27):
            if c[i]!=0:
                a.append({
                    "rot": i,
                    "usages": c[i]
                })
        return Response(a)
