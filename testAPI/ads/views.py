from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)


class AdvertisementDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, ad_id):
        advertisement = get_object_or_404(Advertisement, ad_id=ad_id)
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)
