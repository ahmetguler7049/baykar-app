from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AircraftInventorySerializer, PartInventorySerializer
from .models import AircraftInventory, PartInventory
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def team_dashboard(request):
    user_team = request.user.team
    return render(request, 'team_dashboard.html', {'team': user_team})


class AircraftInventoryCreateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_team = request.user.team

        if user_team.name != "Montaj":
            return Response({"message": "Bu işlem sadece Montaj takımı için geçerlidir."},
                            status=status.HTTP_403_FORBIDDEN)

        aircraft_inventory = AircraftInventory.objects.all()
        serializer = AircraftInventorySerializer(aircraft_inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_team = request.user.team

        if user_team.name != "Montaj":
            return Response({"message": "Bu işlem sadece Montaj takımı için geçerlidir."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = AircraftInventorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartInventoryCreateListDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_team = request.user.team

        if user_team.name == "Montaj":
            return Response({"message": "Bu işlem sadece Montaj dışındaki takımlar için geçerlidir."},
                            status=status.HTTP_403_FORBIDDEN)

        part_inventory = PartInventory.objects.filter(team=user_team)
        serializer = PartInventorySerializer(part_inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_team = request.user.team

        if user_team.name == "Montaj":
            return Response({"message": "Bu işlem sadece Montaj dışındaki takımlar için geçerlidir."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = PartInventorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, part_id):
        user_team = request.user.team

        if user_team.name == "Montaj":
            return Response({"message": "Bu işlem sadece Montaj dışındaki takımlar için geçerlidir."},
                            status=status.HTTP_403_FORBIDDEN)

        try:
            part_inventory = PartInventory.objects.get(id=part_id, team=user_team)
        except PartInventory.DoesNotExist:
            return Response({"message": "PartInventory bulunamadı."}, status=status.HTTP_404_NOT_FOUND)

        # PartInventory'de "is_used" True ise silme işlemi yapılmasın
        if part_inventory.is_used:
            return Response({"message": "Bu parça kullanılıyor ve silinemez."},
                            status=status.HTTP_400_BAD_REQUEST)

        # PartInventory'yi sil
        part_inventory.delete()
        return Response({"message": "Parça başarıyla silindi."}, status=status.HTTP_204_NO_CONTENT)
