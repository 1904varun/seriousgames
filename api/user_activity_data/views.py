import re
from django.forms import model_to_dict
from user_activity_data.models import UserActivityData
from rest_framework import generics
from rest_framework.response import Response
#user_activity_data


class UserActivity(generics.GenericAPIView):
   
    def post(self, request):
        try:
            model_class = UserActivityData(id=request.POST['id'], activity_type=request.POST['activity_type'], value=request.POST['value'],
                                        start_time=request.POST['start_time'], end_time=request.POST['end_time'], points=request.POST['points'])
            model_class.save()
            return Response({"data":{
                "status": "success"}})
        except:
            return Response({"data":{
                "status": "error"}})

        
        

