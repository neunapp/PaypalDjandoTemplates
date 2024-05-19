from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.views import View
from django import forms
#
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.f
from .functions import generateAccessToken, create_order, capture_order


class HomeView(TemplateView):
    template_name = 'index.html'


class PayForm(forms.Form):
    count = forms.IntegerField()
    
    
class PayView(FormView):
    template_name = 'pay.html'
    form_class = PayForm
    success_url = '/'
    
    def form_valid(self, form):
        print(form.cleaned_data['count'])
        #
        print('----')
        respuesta = generateAccessToken()
        print(respuesta)
        return super().form_valid(form)


class CrearOrden(APIView):
    
    def post(self, request):
        order = create_order('Productos')
        print('=====')
        print(order['id'])
        return Response(order, status=status.HTTP_200_OK)


class CapturarOdernPaypal(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            order_id = self.kwargs['order_id']
            response = capture_order(order_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            return Response({'error': 'error aqui'}, status=status.HTTP_400_BAD_REQUEST)
