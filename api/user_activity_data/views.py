from logging import exception
import json
from django.forms import model_to_dict
from django.http import JsonResponse
from user_activity_data.models import UserActivityData, UserPoints, Rewards
from rest_framework import generics
from rest_framework.response import Response
from collections import defaultdict
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

        
        

class UserPointsData(generics.GenericAPIView):

    def get(self, request, user_id):
        try:
            user_points_model = UserPoints.objects.filter(id=user_id)
            user_total_points = user_points_model[0].total_points
            return Response({"data":{
                "value": user_total_points}})
        except:
            return Response({"data":{
                "value": "error"}})



class RewardsTable(generics.GenericAPIView):

    
    def get(self, request):

        try:
            data = {}
            rewards_model = Rewards.objects.all()
            data = list(rewards_model.values())
            return JsonResponse({'data':data}, safe=False)
        except:
            return Response({"data":{
                "value": "error"}})
        
