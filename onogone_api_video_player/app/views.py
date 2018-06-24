from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import Video
from .serializers import VideoSerializer


class VideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        video_serializer = VideoSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_all_video(request):
    data = []
    for video in Video.objects.all():
        data.append({
            'name': video.name,
            'file_watermark': video.file_watermark,
            'file_1080p': video.file_1080p,
            'file_720p': video.file_720p
        })
    return JsonResponse(data={"videos": data})
