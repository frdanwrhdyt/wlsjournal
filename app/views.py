from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class UserBusinessView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        userBusiness = UserBusiness.objects.filter(user_id = request.user.id)
        try:
            id = request.query_params['id']
            if id!=None:
                data = UserBusiness.object.get(pk=id)
                serializer = UserBusinessSerializer(data)
        except:
            serializer = UserBusinessSerializer(userBusiness, many=True)

        return Response({
            'data':serializer.data,
            'status':status.HTTP_200_OK,
            'message':'success'
        })

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserBusinessSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data,
            'status':status.HTTP_200_OK,
            'message':"success"
        })
    def put(self, request, *args, **kwargs):
        try:
            id=request.data['id']

            data_object = UserBusiness.objects.get(id=id)
            data = request.data

            data_object.name = data['name']
            data_object.location = data['location']
            data_object.tax = data['tax']

            data_object.save()
            serializer = UserBusinessSerializer(data_object)

            return Response({
                'data':serializer.data, 
                'status':status.HTTP_200_OK,
                'message':'success'    
            })
        except:
            return Response({
                'message':'Data not found',
                'status':status.HTTP_204_NO_CONTENT
            })

class SellingProductView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return SellingProduct.objects.get(pk=pk)
        except :
            raise Http404

    def get (self, request, *args, **kwargs):
        ub = UserBusiness.objects.filter(name=request.data['business_name'])
        ubSerializer = UserBusinessSerializer(ub, many=True).data

        data = []
        for i in ubSerializer:
            sP = SellingProduct.objects.filter(user_business_id = i['id'])
            serializer = SellingProductSerializer(sP, many=True).data
            if serializer != []:
                data = data+serializer

        return Response({
            'data':data,
            'status':status.HTTP_200_OK,
            'message':'success'    
        })
    
    def post (self, request):
        serializer = SellingProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data,
            'status':status.HTTP_200_OK,
            'message':"success"
        })
    
    def put(self, request):
        try:
            id = request.data['id']
            data_object = self.get_object(id)
            data = request.data

            data_object.name = data['name']
            data_object.hpp = data['hpp']
            data_object.price = data['price']

            data_object.save()
            serializer = SellingProductSerializer(data_object)
            return Response({
                'data':serializer.data,
                'status':status.HTTP_200_OK,
                'message':'success'    
            })

        except :
            return Response({'message':'Data not found'})
    
    def delete(self, request):
        data_object = self.get_object(request.data['id'])
        data_object.delete()
        return Response({'message':'success',"status":status.HTTP_204_NO_CONTENT})


class CustomerView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try: 
            return Customer.objects.get(pk=pk)
        except:
            raise Http404
    def get(self, request):
        getUBi = UserBusinessView().get(request)
        data = []

        for i in getUBi.data:
            ub = UserBusiness.objects.filter(name=i['name'])
            ubSerializer = UserBusinessSerializer(ub, many=True).data
            for j in ubSerializer:
                sP = Customer.objects.filter(user_business_id = j['id'])
                serializer = CustomerSerializer(sP, many=True).data
        #     if serializer != []:
                data = data+serializer

        return Response({
            'data':data,
            'status':status.HTTP_200_OK,
            'message':'success'        
        })

    def post(self, request):
        serializer = CustomerSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def put(self, request):
        try:
            id = request.data['id']
            data_object = self.get_object(id)
            data = request.data

            data_object.name = data['name']
            
            data_object.save()
            serializer = CustomerSerializer(data_object)
            return Response({
                'status':status.HTTP_200_OK,
                'message':'success',
                'data':serializer.data
            })
        except:
            return Response({'status':status.HTTP_204_NO_CONTENT, 'message':'Data not found'})

    def delete(self, request):
        data_object = self.get_object(request.data['id'])
        data_object.delete()
        return Response({'message':'success', 'status':status.HTTP_204_NO_CONTENT})

class PaymentTypeView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return PaymentType.objects.get(pk)
        except:
            return Http404
    
    def get(self, request):
        ub = UserBusiness.objects.filter(name=request.data['name'])
        ubSerializer = UserBusinessSerializer(ub, many=True).data
        data = []

        for i in ubSerializer:
            sP = PaymentType.objects.filter(user_business_id = i['id'])
            serializer = PaymentTypeSerializer(sP, many=True).data
            if serializer != []:
                data = data+serializer

        return Response({
            'data':data, 
            'status':status.HTTP_200_OK,
            'message':'success'    
        })

    def post(self, request):
        serializer = PaymentTypeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data':serializer.data,
            'status':status.HTTP_200_OK,
            'message':'success'
        })
    
    def put(self, request):
        try:
            id = request.data['id']
            data_object = self.get_object(id)
            data = request.data

            data_object.name = data['name']
            
            data_object.save()
            serializer = CustomerSerializer(data_object)
            return Response({
                'data':serializer.data,
                'status':status.HTTP_200_OK,
                'message':'success',
            })
        except:
            return Response({'status':status.HTTP_204_NO_CONTENT, 'message':'Data not found'})
        
    def delete(self, request):
        data_object = self.get_object(request.data['id'])
        data_object.delete()
        return Response({'message':'success', 'status':status.HTTP_204_NO_CONTENT})

class InvoiceView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Invoice.objects.get(pk)
        except:
            return Http404

    def get(self, request):
        # for i in request.user:
        #     print(i)
        return Response(request.user.name)

class OrderView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Order.objects.get(pk)
        except:
            return Http404
    def get(self, request):
        getCus = CustomerView().get(request)
        data = []
        for i in getCus.data:
            OrderData = Order.objects.filter(customer_id = i['id'])
            serializer = OrderSerializer(OrderData, many=True).data
            data = data+serializer
        return Response(data)
    def post(self, request):
        data = request.data
        if data['customer_id'] is "":
            for i in UserBusinessView().get(request).data:
                # print(i['id'])
                req = {
                    'name':'Walk-in Customer',
                    'user_business_id':i['id']
                }
                response = Response(req)
            idCus = CustomerView().post(response)
            idCus.accepted_renderer = JSONRenderer()
            idCus.accepted_media_type = "application/json"
            idCus.renderer_context = {}
            idCus.render()           
            # for j in idCus:
            data._mutable = True
            data['customer_id'] = idCus.data['id']
                # print(j)
        serializer = OrderSerializer(data = data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    def put(self, request):
        try: 
            id = request.data['id']
            data_object = self.data_object(id)
            data = request.data

            data_object.status = data['status']
            data_object.selling_product_id = data['selling_product_id']
            data_object.amount = data['amount']
            
            data_object.save()
            serializer = CustomerSerializer(data_object)
            return Response({
                'status':status.HTTP_200_OK,
                'message':'success',
                'data':serializer.data
            })
        except:
            return Response({'status':status.HTTP_204_NO_CONTENT, 'message':'Data not found'})

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated,]
    def get_object(self, pk):
        try:
            return Order.objects.get(pk)
        except:
            raise Http404
    
    def get(self, request):
        # all = request.query_params['all']
        # # return Response(all)
        # if all is '0':
        #     cid = request.data['customer_id']
        #     status = request.data['status']
        #     data = Order.objects.filter(customer_id = cid, status= status)
        # else:
        #     pass
        # return Response(data)
        pass