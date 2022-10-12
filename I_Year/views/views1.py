from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404


# --------------- SEM 1 HEADER -------------

from ..models.models1 import Sem_1_Marks_IT, Sem_1_Marks_EIE, Sem_1_Marks_AIDS, Sem_1_Marks_AUTO, Sem_1_Marks_CIVIL, Sem_1_Marks_CSE, Sem_1_Marks_ECE, Sem_1_Marks_EEE, Sem_1_Marks_MECH, Sem_1_Results_AIDS, Sem_1_Results_AUTO, Sem_1_Results_CIVIL, Sem_1_Results_CSE, Sem_1_Results_ECE, Sem_1_Results_EEE, Sem_1_Results_EIE, Sem_1_Results_IT, Sem_1_Results_MECH
from ..serializers.serializers1 import Sem_1_IT_Serializer, Sem_1_CSE_Serializer, Sem_1_CIVIL_Serializer, Sem_1_AIDS_Serializer, Sem_1_AUTO_Serializer, Sem_1_ECE_Serializer, Sem_1_EEE_Serializer, Sem_1_EIE_Serializer, Sem_1_MECH_Serializer

# -------------- END OF SEM 1 HEAD -----------------


# --------------- SEM 1 VIEWS--------------------


class ApiOverView(APIView):
    def get(self, request):
        api_urls = {
            'ResultsIT_Total': 'results/IT',
            'ResultIT': 'results/IT/<int:id>/',
            'ResultsCSE_Total': 'results/CSE',
            'ResultCSE': 'results/CSE/<int:id>/',
            'ResultsECE_Total': 'results/ECE',
            'ResultECE': 'results/ECE/<int:id>/',
            'ResultsEEE_Total': 'results/EEE',
            'ResultEEE': 'results/EEE/<int:id>/',
            'ResultsAIDS_Total': 'results/AIDS',
            'ResultAIDS': 'results/AIDS/<int:id>/',
            'ResultsMECH_Total': 'results/MECH',
            'ResultMECH': 'results/MECH/<int:id>/',
            'ResultsCIVIL_Total': 'results/CIVIL',
            'ResultCIVIL': 'results/CIVIL/<int:id>/',
            'ResultsEIE_Total': 'resultS/EIE',
            'ResultEIE': 'results/EIE/<int:id>/',
            'ResultsAUTO_Total': 'results/AUTO',
            'ResultAUTO': 'results/AUTO/<int:id>/',
        }
        return Response(api_urls)


class Sem_1_Results_List_View_IT(APIView):
    def get(self, request):
        result = Sem_1_Marks_IT.objects.all()
        serializer = Sem_1_IT_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_IT.objects.get_or_create(Register_No=i['Register_No'],
                                                   P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_IT_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_IT.objects.get(Register_No=pk)
        except Sem_1_Marks_IT.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_IT_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_CSE(APIView):
    def get(self, request):
        result = Sem_1_Marks_CSE.objects.all()
        serializer = Sem_1_CSE_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_CSE.objects.get_or_create(Register_No=i['Register_No'],
                                                    P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_CSE_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_CSE.objects.get(Register_No=pk)
        except Sem_1_Marks_CSE.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_CSE_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_ECE(APIView):
    def get(self, request):
        result = Sem_1_Marks_ECE.objects.all()
        serializer = Sem_1_ECE_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_ECE.objects.get_or_create(Register_No=i['Register_No'],
                                                    P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_ECE_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_ECE.objects.get(Register_No=pk)
        except Sem_1_Marks_ECE.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_ECE_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_AIDS(APIView):
    def get(self, request):
        result = Sem_1_Marks_AIDS.objects.all()
        serializer = Sem_1_AIDS_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_AIDS.objects.get_or_create(Register_No=i['Register_No'],
                                                     P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_AIDS_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_AIDS.objects.get(Register_No=pk)
        except Sem_1_Marks_AIDS.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_AIDS_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_EEE(APIView):
    def get(self, request):
        result = Sem_1_Marks_EEE.objects.all()
        serializer = Sem_1_EEE_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_EEE.objects.get_or_create(Register_No=i['Register_No'],
                                                    P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_EEE_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_EEE.objects.get(Register_No=pk)
        except Sem_1_Marks_EEE.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_EEE_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_CIVIL(APIView):
    def get(self, request):
        result = Sem_1_Marks_CIVIL.objects.all()
        serializer = Sem_1_CIVIL_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_CIVIL.objects.get_or_create(Register_No=i['Register_No'],
                                                      P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_CIVIL_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_CIVIL.objects.get(Register_No=pk)
        except Sem_1_Marks_CIVIL.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_CIVIL_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_MECH(APIView):
    def get(self, request):
        result = Sem_1_Marks_MECH.objects.all()
        serializer = Sem_1_MECH_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_MECH.objects.get_or_create(Register_No=i['Register_No'],
                                                     P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_MECH_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_MECH.objects.get(Register_No=pk)
        except Sem_1_Marks_MECH.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_MECH_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_EIE(APIView):
    def get(self, request):
        result = Sem_1_Marks_EIE.objects.all()
        serializer = Sem_1_EIE_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_EIE.objects.get_or_create(Register_No=i['Register_No'],
                                                    P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_EIE_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_EIE.objects.get(Register_No=pk)
        except Sem_1_Marks_EIE.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_EIE_Serializer(result, many=False)
        return Response(serializer.data)


class Sem_1_Results_List_View_AUTO(APIView):
    def get(self, request):
        result = Sem_1_Marks_AUTO.objects.all()
        serializer = Sem_1_AUTO_Serializer(result, many=True)
        data = serializer.data
        for i in data:
            Sem_1_Results_AUTO.objects.get_or_create(Register_No=i['Register_No'],
                                                     P21MA101T=i['P21MA101T'], P21CH101T=i['P21CH101T'], P21EN101T=i['P21EN101T'], P21ME101T=i['P21ME101T'], P21CS101T=i['P21CS101T'], P21CH102L=i['P21CH102L'], P21CS102L=i['P21CS102L'], P21EN102L=i['P21EN102L'], GPA=i['GPA'])
        return Response(serializer.data)


class Sem_1_Result_AUTO_View(APIView):
    def get_object(self, pk):
        try:
            return Sem_1_Marks_AUTO.objects.get(Register_No=pk)
        except Sem_1_Marks_AUTO.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        result = self.get_object(pk)
        serializer = Sem_1_AUTO_Serializer(result, many=False)
        return Response(serializer.data)


# --------------- END OF SEM 1 VIEWS-------------
