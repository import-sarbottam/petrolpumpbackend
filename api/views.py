from django.shortcuts import render
from .models import Entry, Partyname, Prices
from .serializers import EntrySerializer, PartySerializer, PriceSerializer
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
# Create your views here.


class EntryPost(GenericAPIView):

    serializer_class = EntrySerializer
    # authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartyPost(GenericAPIView):

    serializer_class = PartySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if(request.user.shift == 'zero'):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetEntry(APIView):  # only admin

    def get(self, request, format=None):

        query_set = Entry.objects.filter(company=request.user.company).values()
        if(query_set):
            return Response(query_set, status=status.HTTP_200_OK)
        else:
            return Response('The Entry does not exist', status=status.HTTP_404_NOT_FOUND)


class GetShiftEntry(APIView):

    def get(self, request, format=None):

        query_set = Entry.objects.filter(owner=request.user.username).values()
        if(query_set):
            return Response(query_set, status=status.HTTP_200_OK)
        else:
            return Response('The Entry does not exist', status=status.HTTP_404_NOT_FOUND)


class GetParty(APIView):

    def get(self, request, format=None):

        query_set = Partyname.objects.filter(
            company=request.user.company).values()

        if(query_set):
            return Response(query_set, status=status.HTTP_200_OK)
        else:
            return Response('The Entry does not exist', status=status.HTTP_404_NOT_FOUND)


class GetPrices(APIView):

    def get(self, request, format=None):

        try:
            query_set = Prices.objects.get(company=request.user.company)
            serializer = PriceSerializer(query_set)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Prices.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostUpdatePrice(GenericAPIView):

    serializer_class = PriceSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if(request.user.shift == 'zero'):
                try:
                    Prices.objects.get(company=request.user.company).delete()
                except Prices.DoesNotExist:
                    pass
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteParty(GenericAPIView):

    def get_object(self, request, pk):
        try:
            return Partyname.objects.get(id=pk)
        except Prices.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        if(request.user.shift == 'zero'):
            snippet = self.get_object(request, pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
