from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets

from profiles_api import serializers

'''
APIviews vs Viewsets:

APIViews:
--API views are used when we need complex logic like (calling   other APIs or working with other files)
-- define fucntion for HTTPS (get,put,post,delete,patch)
-- full control over logic


ViewSets:
-- uses common api object oprations (list,create,retireve,update,partial update,deletobkect)
-- database intrface fastest
--for standard database oprations
--CRUD 
--simple API
'''


#APIView
class HelloApiView(APIView):
    '''TEST API VIEW'''
    
    #added seirializer class
    serializer_class = serializers.HelloSerializer
    
    
    
    def get(self,request,format=None):
        '''return a list of APIView Features'''
        an_apiview=[
        'Uses HTTP methods as fucntion(get,post,patch,put,delete)',
        'is similar to a traditional django view',
        'gives most control on logic',
        'is Mapped mannually to URLs',
        ]

        # can return list or dict in JSON
        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        """create hello messsge wih our name"""
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f"Hello {name}"
            return Response({"messsage":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                )
            
    def put(self,request,pk=None):
        """Handle update an object,it replaces the object"""
        
        return Response({"method":"PUT"})
    
    def patch(self,request,pk=None):
        """Handle partial update of object,it updates object"""
        
        return Response({"method":"PATCH"})
        
    def delete(self,request,pk=None):
        """Deletes the obejct"""
        return Response({"method":"DELETE"})
        
        
        
# Viewse
class HelloVeiwSet(viewsets.ViewSet):
    """TEST API VEIWSETS"""
    serializer_class=serializers.HelloSerializer
    
    def list(self,request):
        """return hello message"""
        
        a_viewset=[
            "uses common api object oprations (list,create,retireve,update,partial update,deletobkect)",
            "Automatically maps Urls, using Routers",
            "provides more functionality with less code",
        ]
        
        return Response({"message":"Hello","a_viewset":a_viewset})
    
    def create(self,request):
        """create new create message"""
        serializer=self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            message=f"hello {name} bhai"
            
            return Response({"message": message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
            
    def retrieve(self,request,pk=None):
        """Handle getting object by ID"""
        return Response({"http_veiwset_method":"get(retrieve)"})
    
    def update(self,request,pk=None):
        """Handle updating object by ID"""
        return Response({"http_veiwset_method":"put(update)"})
    
    def partial_update(self,request,pk=None):
        """Handle updating partially object by ID"""
        return Response({"http_veiwset_method":"patch(partial update)"})
    
    
    def destroy(self,request,pk=None):
        """Handle delete object by ID"""
        return Response({"http_veiwset_method":"delete(destroy)"})