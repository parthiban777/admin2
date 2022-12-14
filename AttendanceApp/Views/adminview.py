from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import jwt, datetime
from AttendanceApp.models import Employee,Admin
from AttendanceApp.serializers import EmployeeSerializer,AdminSerializer
from PIL import Image
import io


#django file storage




"""
class EmployeeView(APIView):
    @csrf_exempt
    def post(self, request):
        #image=open(request.data['img'],'rb')
        #im = Image.open(request.data['img'])
        #image_bytes = io.BytesIO()
        #im.save(image_bytes, format='JPEG')

        #request.data['img']=image_bytes.getvalue()
        
        serializer = EmployeeSerializer(data=request.data)
        #print(serializer)
        #serializer.img.replace(image,filename=serializer.id)
        serializer.is_valid(raise_exception=True)
        serializer.save() #saving User profile
        return Response(serializer.data)
"""
"""
class EmployeeView(APIView):
    @csrf_exempt
    def post(self, request):
        im = Image.open(request.data['img'])
        image_bytes = io.BytesIO()
        im.save(image_bytes, format='JPEG')
        request.data['img']=image_bytes.getvalue()
        serializer = EmployeeSerializer(data=request.data)
        print(request.data['img'])
        serializer.is_valid(raise_exception=True)
        serializer.save() #saving User profile
        return Response(serializer.data)

"""
import os, os.path

'''
#Compreface

from tkinter import Y
from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.collections.face_collections import Subjects
from django.http import JsonResponse


DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '54cc82e7-9a68-4676-bb75-a3315748598c'

#API_KEY: str = 'da1647cc-856c-4c77-9aa2-0b221cea2754'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

subjects: Subjects = recognition.get_subjects()
'''
from rest_framework.exceptions import AuthenticationFailed

class EmployeeView(APIView):
    @csrf_exempt
    def post(self, request):
       token = request.COOKIES.get('jwt')
       if token:
            serializer = EmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save() #saving User profile
            return Response("New Employee Has Been Added Successfully")


<<<<<<< HEAD
        imp="D:\\User_G\\Applications\\Attendance_management\\Images\\"
        end=".jpg"
        data=request.data        
        # face_collection.add(image_path=imp+data["subject"]+end, subject=data["name"])
        serializer = EmployeeSerializer(data=request.data)
=======
class AdminLogin(APIView): 
    @csrf_exempt
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = Admin.objects.filter(email=email).first()
            
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class AdminReg(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
>>>>>>> 138653ae049ee7ca18b7ccbdd4be31df6c6ecfc7
        serializer.is_valid(raise_exception=True)
        serializer.save() #saving User profile
        return Response(serializer.data)


