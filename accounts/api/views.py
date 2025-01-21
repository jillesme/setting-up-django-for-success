from django.db.models.expressions import F
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUser


class IncrementCountView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        CustomUser.objects.filter(pk=request.user.pk).update(count=F("count") + 1)
        return Response(status=status.HTTP_204_NO_CONTENT)