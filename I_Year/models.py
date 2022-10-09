from django.db import models

# Create your models here.

# --------------------1ST YEAR--------------------


# --------------------SEMESTER -1 ----------------

# --------------INFORMATION TECHNOLOGY------------


class Sem_1_Marks_IT(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks IT"
        verbose_name_plural = "Sem 1 Marks IT"


class Sem_1_Results_IT(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results IT"
        verbose_name_plural = "Sem 1 Results IT"

# -------------------END OF IT SEM-1--------------


# --------------COMPUTER SCIENCE------------------

class Sem_1_Marks_CSE(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks CSE"
        verbose_name_plural = "Sem 1 Marks CSE"


class Sem_1_Results_CSE(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results CSE"
        verbose_name_plural = "Sem 1 Results CSE"
# -------------------END OF CSE SEM-1--------------


# --------------ELECTRONICS AND COMMUNICATION------------------


class Sem_1_Marks_ECE(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks ECE"
        verbose_name_plural = "Sem 1 Marks ECE"


class Sem_1_Results_ECE(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results ECE"
        verbose_name_plural = "Sem 1 Results ECE"


# -------------------END OF ECE SEM-1--------------


# --------------ELECTRICAL ELECTRONICS ENGINEERING------------------


class Sem_1_Marks_EEE(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks EEE"
        verbose_name_plural = "Sem 1 Marks EEE"


class Sem_1_Results_EEE(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results EEE"
        verbose_name_plural = "Sem 1 Results EEE"

# -------------------END OF EEE SEM-1--------------


# --------------ARTIFICIAL INTELLIGENCE AND DATA SCIENCE------------------


class Sem_1_Marks_AIDS(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks AIDS"
        verbose_name_plural = "Sem 1 Marks AIDS"


class Sem_1_Results_AIDS(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results AIDS"
        verbose_name_plural = "Sem 1 Results AIDS"

# -------------------END OF AIDS SEM-1--------------


# --------------MECHANICAL ENGINEERING------------------


class Sem_1_Marks_MECH(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks MECH"
        verbose_name_plural = "Sem 1 Marks MECH"


class Sem_1_Results_MECH(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results MECH"
        verbose_name_plural = "Sem 1 Results MECH"

# -------------------END OF MECH SEM-1--------------


# --------------     CIVIL     ------------------


class Sem_1_Marks_CIVIL(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks CIVIL"
        verbose_name_plural = "Sem 1 Marks CIVIL"


class Sem_1_Results_CIVIL(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results CIVIL"
        verbose_name_plural = "Sem 1 Results CIVIL"

# -------------------END OF CIVIL SEM-1--------------


# --------------ELECTRONICS AND INSTRUMENTATION------------------


class Sem_1_Marks_EIE(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks EIE"
        verbose_name_plural = "Sem 1 Marks EIE"


class Sem_1_Results_EIE(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results EIE"
        verbose_name_plural = "Sem 1 Results EIE"

# -------------------END OF EIE SEM-1--------------


# --------------AUTOMOBILE ENGINEERING------------------


class Sem_1_Marks_AUTO(models.Model):
    Register_No = models.BigIntegerField(unique=True, blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    Internal_21MA101T = models.IntegerField(blank=False, null=True)
    External_21MA101T = models.IntegerField(blank=False, null=True)
    Internal_21CH101T = models.IntegerField(blank=False, null=True)
    External_21CH101T = models.IntegerField(blank=False, null=True)
    Internal_21EN101T = models.IntegerField(blank=False, null=True)
    External_21EN101T = models.IntegerField(blank=False, null=True)
    Internal_21ME101T = models.IntegerField(blank=False, null=True)
    External_21ME101T = models.IntegerField(blank=False, null=True)
    Internal_21CS101T = models.IntegerField(blank=False, null=True)
    External_21CS101T = models.IntegerField(blank=False, null=True)
    Internal_21CH102L = models.IntegerField(blank=False, null=True)
    External_21CH102L = models.IntegerField(blank=False, null=True)
    Internal_21CS102L = models.IntegerField(blank=False, null=True)
    External_21CS102L = models.IntegerField(blank=False, null=True)
    Internal_21EN102L = models.IntegerField(blank=False, null=True)
    External_21EN102L = models.IntegerField(blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Marks AUTO"
        verbose_name_plural = "Sem 1 Marks AUTO"


class Sem_1_Results_AUTO(models.Model):
    Register_No = models.BigIntegerField(unique=True,
                                         blank=False, null=True)
    DOB = models.DateField(
        auto_now_add=False, auto_now=False, blank=False, null=True)
    Name = models.CharField(max_length=50, blank=False, null=True)
    P21MA101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH101T = models.CharField(max_length=2, blank=False, null=True)
    P21EN101T = models.CharField(max_length=2, blank=False, null=True)
    P21ME101T = models.CharField(max_length=2, blank=False, null=True)
    P21CS101T = models.CharField(max_length=2, blank=False, null=True)
    P21CH102L = models.CharField(max_length=2, blank=False, null=True)
    P21CS102L = models.CharField(max_length=2, blank=False, null=True)
    P21EN102L = models.CharField(max_length=2, blank=False, null=True)
    GPA = models.DecimalField(
        max_digits=4, decimal_places=2, blank=False, null=True)

    class Meta:
        verbose_name = "Sem 1 Results AUTO"
        verbose_name_plural = "Sem 1 Results AUTO"
# -------------------END OF AUTO SEM-1--------------

# --------------------END OF SEMESTER -1 ----------------

# -------------------- END OF 1ST YEAR--------------------
