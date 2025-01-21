from django.contrib.auth import get_user_model
from django.db.models.expressions import F
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class IncrementCountView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        get_user_model().objects.filter(pk=request.user.pk).update(count=F("count") + 1)
        request.user.refresh_from_db()
        return Response(data={'updatedCount': request.user.count}, status=status.HTTP_200_OK)
