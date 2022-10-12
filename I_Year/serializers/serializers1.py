from rest_framework.serializers import ModelSerializer, SerializerMethodField

# ------------- SEM 1 HEADER----------------

from ..models.models1 import Sem_1_Marks_IT, Sem_1_Marks_EIE, Sem_1_Marks_AIDS, Sem_1_Marks_AUTO, Sem_1_Marks_CIVIL, Sem_1_Marks_CSE, Sem_1_Marks_ECE, Sem_1_Marks_EEE, Sem_1_Marks_MECH, Sem_1_Results_AIDS, Sem_1_Results_AUTO, Sem_1_Results_CIVIL, Sem_1_Results_CSE, Sem_1_Results_ECE, Sem_1_Results_EEE, Sem_1_Results_EIE, Sem_1_Results_IT, Sem_1_Results_MECH

# ------------- END OF SEM 1----------------

# ------------- SEM 1 SERIAIZERS-------------


class Sem_1_IT_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_IT
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_CSE_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_CSE
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_ECE_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_ECE
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_EEE_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_EEE
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_AIDS_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_AIDS
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_MECH_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_MECH
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_CIVIL_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_CIVIL
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_EIE_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_EIE
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)


class Sem_1_AUTO_Serializer(ModelSerializer):
    P21MA101T = SerializerMethodField()
    P21CH101T = SerializerMethodField()
    P21EN101T = SerializerMethodField()
    P21ME101T = SerializerMethodField()
    P21CS101T = SerializerMethodField()
    P21CH102L = SerializerMethodField()
    P21CS102L = SerializerMethodField()
    P21EN102L = SerializerMethodField()
    GPA = SerializerMethodField()

    class Meta:
        model = Sem_1_Marks_AUTO
        fields = ['Register_No',
                  'P21MA101T', 'P21CH101T', 'P21EN101T', 'P21ME101T', 'P21CS101T', 'P21CH102L', 'P21CS102L', 'P21EN102L', 'GPA']

    dict = {'P21MA101T': 4, 'P21CH101T': 3, 'P21EN101T': 2, 'P21ME101T': 4,
            'P21CS101T': 3, 'P21CH102L': 1, 'P21CS102L': 2, 'P21EN102L': 1}
    dict1 = {'P21MA101T': 0, 'P21CH101T': 0, 'P21EN101T': 0, 'P21ME101T': 0,
             'P21CS101T': 0, 'P21CH102L': 0, 'P21CS102L': 0, 'P21EN102L': 0}

    def get_P21MA101T(self, obj):

        if ((obj.Internal_21MA101T or obj.External_21MA101T) == None):
            self.dict1.update({'P21MA101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 100 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 10*(self.dict['P21MA101T'])})
            return "O"
        elif 80 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 89 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 9*(self.dict['P21MA101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 79 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 8*(self.dict['P21MA101T'])})
            return "A"
        elif 60 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 69 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 7*(self.dict['P21MA101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 59 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 6*(self.dict['P21MA101T'])})
            return "B"
        elif 50 <= (obj.Internal_21MA101T+obj.External_21MA101T) <= 54 and (obj.External_21MA101T >= 25):
            self.dict1.update({'P21MA101T': 5*(self.dict['P21MA101T'])})
            return "C"
        else:
            self.dict1.update({'P21MA101T': 0})
            return "U"

    def get_P21CH101T(self, obj):
        if ((obj.Internal_21CH101T or obj.External_21CH101T) == None):
            self.dict1.update({'P21CH101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 100 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 10*(self.dict['P21CH101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 89 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 9*(self.dict['P21CH101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 79 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 8*(self.dict['P21CH101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 69 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 7*(self.dict['P21CH101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 59 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 6*(self.dict['P21CH101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CH101T+obj.External_21CH101T) <= 54 and (obj.External_21CH101T >= 25):
            self.dict1.update({'P21CH101T': 5*(self.dict['P21CH101T'])})
            return "C"
        else:
            self.dict1.update({'P21CH101T': 0})
            return "U"

    def get_P21EN101T(self, obj):
        if (obj.Internal_21EN101T or obj.External_21EN101T) == None:
            self.dict1.update({'P21EN101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 100 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 10*(self.dict['P21EN101T'])})
            return "O"
        elif 80 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 89 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 9*(self.dict['P21EN101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 79 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 8*(self.dict['P21EN101T'])})
            return "A"
        elif 60 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 69 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 7*(self.dict['P21EN101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 59 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 6*(self.dict['P21EN101T'])})
            return "B"
        elif 50 <= (obj.Internal_21EN101T+obj.External_21EN101T) <= 54 and (obj.External_21EN101T >= 25):
            self.dict1.update({'P21EN101T': 5*(self.dict['P21EN101T'])})
            return "C"
        else:
            self.dict1.update({'P21EN101T': 0})
            return "U"

    def get_P21ME101T(self, obj):
        if (obj.Internal_21ME101T or obj.External_21ME101T) == None:
            self.dict1.update({'P21ME101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 100 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 10*(self.dict['P21ME101T'])})
            return "O"
        elif 80 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 89 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 9*(self.dict['P21ME101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 79 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 8*(self.dict['P21ME101T'])})
            return "A"
        elif 60 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 69 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 7*(self.dict['P21ME101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 59 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 6*(self.dict['P21ME101T'])})
            return "B"
        elif 50 <= (obj.Internal_21ME101T+obj.External_21ME101T) <= 54 and (obj.External_21ME101T >= 25):
            self.dict1.update({'P21ME101T': 5*(self.dict['P21ME101T'])})
            return "C"
        else:
            self.dict1.update({'P21ME101T': 0})
            return "U"

    def get_P21CS101T(self, obj):
        if (obj.Internal_21CS101T or obj.External_21CS101T) == None:
            self.dict1.update({'P21CS101T': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 100 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 10*(self.dict['P21CS101T'])})
            return "O"
        elif 80 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 89 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 9*(self.dict['P21CS101T'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 79 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 8*(self.dict['P21CS101T'])})
            return "A"
        elif 60 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 69 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 7*(self.dict['P21CS101T'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 59 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 6*(self.dict['P21CS101T'])})
            return "B"
        elif 50 <= (obj.Internal_21CS101T+obj.External_21CS101T) <= 54 and (obj.External_21CS101T >= 25):
            self.dict1.update({'P21CS101T': 5*(self.dict['P21CS101T'])})
            return "C"
        else:
            self.dict1.update({'P21CS101T': 0})
            return "U"

    def get_P21EN102L(self, obj):
        if (obj.Internal_21EN102L or obj.External_21EN102L) == None:
            self.dict1.update({'P21EN102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 100 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 10*(self.dict['P21EN102L'])})
            return "O"
        elif 80 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 89 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 9*(self.dict['P21EN102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 79 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 8*(self.dict['P21EN102L'])})
            return "A"
        elif 60 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 69 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 7*(self.dict['P21EN102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 59 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 6*(self.dict['P21EN102L'])})
            return "B"
        elif 50 <= (obj.Internal_21EN102L+obj.External_21EN102L) <= 54 and (obj.External_21EN102L >= 25):
            self.dict1.update({'P21EN102L': 5*(self.dict['P21EN102L'])})
            return "C"
        else:
            self.dict1.update({'P21EN102L': 0})
            return "U"

    def get_P21CH102L(self, obj):
        if (obj.Internal_21CH102L or obj.External_21CH102L) == None:
            self.dict1.update({'P21CH102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 100 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 10*(self.dict['P21CH102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 89 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 9*(self.dict['P21CH102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 79 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 8*(self.dict['P21CH102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 69 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 7*(self.dict['P21CH102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 59 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 6*(self.dict['P21CH102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CH102L+obj.External_21CH102L) <= 54 and (obj.External_21CH102L >= 25):
            self.dict1.update({'P21CH102L': 5*(self.dict['P21CH102L'])})
            return "C"
        else:
            self.dict1.update({'P21CH102L': 0})
            return "U"

    def get_P21CS102L(self, obj):
        if (obj.Internal_21CS102L or obj.External_21CS102L) == None:
            self.dict1.update({'P21CS102L': 0})
            return "U"
        elif 90 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 100 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 10*(self.dict['P21CS102L'])})
            return "O"
        elif 80 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 89 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 9*(self.dict['P21CS102L'])})
            return "A+"
        elif 70 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 79 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 8*(self.dict['P21CS102L'])})
            return "A"
        elif 60 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 69 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 7*(self.dict['P21CS102L'])})
            return "B+"
        elif 55 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 59 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 6*(self.dict['P21CS102L'])})
            return "B"
        elif 50 <= (obj.Internal_21CS102L+obj.External_21CS102L) <= 54 and (obj.External_21CS102L >= 25):
            self.dict1.update({'P21CS102L': 5*(self.dict['P21CS102L'])})
            return "C"
        else:
            self.dict1.update({'P21CS102L': 0})
            return "U"

    def get_GPA(self, obj):
        base_credits = self.dict
        total_credits = self.dict1
        for i in total_credits:
            if total_credits[i] == 0:
                return None
        else:
            gpa = sum(total_credits.values()) / sum(base_credits.values())
            return round(gpa, 2)
# -------------END OF SEM 1 SERIALIZERS-----------
