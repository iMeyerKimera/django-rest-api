from rest_framework import generics


from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

#  Implementation of Rest capability  with Pure Django Rest Framework


#  Using generic vies to simplify code
class PollList(generics.ListCreateAPIView):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


#  Using APIView
# from rest_framework.views import APIView
#
#
# from .models import Poll, Choice
# from .serializers import PollSerializer
#
#
# #  Using generic vies to simplify code
# class PollList(APIView):
#
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
#
#
# class PollDetail(APIView):
#
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer


#  Using methods
# from rest_framework.response import  Response
# from django.shortcuts import render, get_object_or_404
#
# from .models import Poll, Choice
# from .serializers import PollSerializer
#
# class PollList(APIView):
#
#     def get(self, request):
#         polls = Poll.objects.all()[:5]
#         data = PollSerializer(polls, many=True).data
#         return Response(data)
#
#
#
# class PollDetail(APIView):
#
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)

