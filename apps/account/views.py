from rest_framework import  generics
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import UserProfile
from .serializers import UserProfileSerializer

# class GetUserProfileView(APIView):
#     def get(self, request, format=None):
#         try:
#             user = self.request.user
#             user_profile = UserProfile.objects.get(user=user)
#             user_profile = UserProfileSerializer(user_profile)

#             return Response(
#                 {'profile': user_profile.data},
#                 status=status.HTTP_200_OK
#             )
#         except:
#             return Response(
#                 {'error': 'Something went wrong when retrieving profile'},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )


class GetUserProfileView(generics.GenericAPIView):
    serializer_class = UserProfileSerializer

    def get(self, request, format=None):
        user = UserProfile.objects.get(user=self.request.user)

        if user:
            return Response(self.serializer_class(user).data)
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)


class UpdateUserProfileView(generics.UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, format=None):
        user = self.request.user
        data = self.request.data

        address_line_1 = data['address_line_1']
        address_line_2 = data['address_line_2']
        city = data['city']
        state_province_region = data['state_province_region']
        phone = data['phone']
        dni = data['dni']

        UserProfile.objects.filter(user=user).update(
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
            state_province_region=state_province_region,
            phone=phone,
            dni=dni
        )
        user_profile = UserProfile.objects.get(user=user)

        if user_profile:
            return Response(self.serializer_class(user_profile).data)
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)
        

       