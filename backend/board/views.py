from django.shortcuts import render
from board.serializers import BoardSerializer
from rest_framework.views import APIView
from icecream import ic
from rest_framework.response import Response


class Boards(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'post succes! Title:, {serializer.data.get("title")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)

    class Board(APIView):
        def get(self, request):
            pass


