from django.db import models
from django.urls import reverse
from django.conf import settings

class Ministry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    MinistryName = models.CharField(max_length=100)
    HonorableMinisterName = models.CharField(max_length=100)
    Address = models.TextField()
    Phone = models.CharField(max_length=15,null=True)
    Email = models.EmailField()
    class Meta:
        db_table = "ministry"

    def __str__(self):
        return self.MinistryName

    def get_absolute_url(self):
        return reverse('Crud:ministry_edit', kwargs={'pk': self.pk})

class GovernmentEmployee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    GovernmentEmployeeName = models.CharField(max_length=100)
    GovernmentEmployeeAddress = models.TextField()
    GovernmentEmployeePhnNumber = models.CharField(max_length=15)
    GovernmentEmployeeGmail = models.EmailField()
    GovernmentEmployeeDesignation = models.CharField(max_length=100)

    class Meta:
        db_table = "govermentemployee"

    def __str__(self):
        return self.GovernmentEmployeeName

    def get_absolute_url(self):
        return reverse('Crud:governmentEmployee_edit', kwargs={'pk': self.pk})