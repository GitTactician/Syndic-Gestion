from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics
from rest_framework.mixins import (
    ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
)
from .models import Habitant, Syndic, Residence, Reglement
from .serializers import (
    HabitantSerializer, SyndicSerializer, ResidenceSerializer, ReglementSerializer, UserLoginSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import logout
from rest_framework.authentication import TokenAuthentication
import requests
from rest_framework import permissions
import os


class HabitantLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        # Add your custom logic here for Habitant login

        return Response(response_data, status=status.HTTP_200_OK)


class SyndicLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        # Add your custom logic here for Syndic login

        return Response(response_data, status=status.HTTP_200_OK)


class UserLogoutView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)

    def create(self, request, *args, **kwargs):
        try:
            request.auth.delete()
            logout(request)
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class HabitantListCreateView(generics.ListCreateAPIView):
    queryset = Habitant.objects.all()
    serializer_class = HabitantSerializer


class HabitantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitant.objects.all()
    serializer_class = HabitantSerializer


class SyndicListCreateView(generics.ListCreateAPIView):
    queryset = Syndic.objects.all()
    serializer_class = SyndicSerializer


class SyndicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Syndic.objects.all()
    serializer_class = SyndicSerializer


class ResidenceListCreateView(generics.ListCreateAPIView):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer


class ResidenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer


class ReglementListCreateView(generics.ListCreateAPIView):
    queryset = Reglement.objects.all()
    serializer_class = ReglementSerializer


class ReglementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reglement.objects.all()
    serializer_class = ReglementSerializer
