from django.shortcuts import render

from django.urls import path
from . import views_cbv
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from member.serializers import MemberSerializer
from rest_framework.views import APIView
from icecream import ic
from rest_framework.response import Response
from member.models import MemberVO



# CBV(Class Based View) 형식

class Members(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)


class Member(APIView):
    def get_object(self, pk):
        try:
            return MemberVO.objects.get(pk=pk)
        except MemberVO.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)



'''
@csrf_exempt
def member_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Member.objects.all()
        serializer = MemberSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # 저장
            return JsonResponse(serializer.data, status=201)  # Json으로 변경
        return JsonResponse(serializer.errors, status=400)
'''