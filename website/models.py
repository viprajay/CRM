from django.db import models
from django.utils.timezone import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Emp(models.Model):
    objects = models.Manager()

    employee_id = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    employee_pass = models.CharField(max_length=10, unique=True, blank=True, editable=False, default="password")

    def save(self, *args, **kwargs):
        if not self.employee_id:
            last_emp = Emp.objects.order_by('id').last()
            if last_emp and last_emp.employee_id:
                last_id = int(last_emp.employee_id.replace("EMP", ""))
                new_id = f"EMP{last_id + 1:04d}"
            else:
                new_id = "EMP0001"
            self.employee_id = new_id

        if not self.employee_pass or self.employee_pass == "password":
            last_emp = Emp.objects.order_by('id').last()
            if last_emp and last_emp.employee_pass:
                try:
                    last_pass_id = int(last_emp.employee_pass.replace("PASS", ""))
                except ValueError:
                    last_pass_id = 0
                new_pass = f"PASS{last_pass_id + 1:04d}"
            else:
                new_pass = "PASS0001"
            self.employee_pass = new_pass

        super().save(*args, **kwargs)

    name = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=200, default="")
    email = models.EmailField(unique=True, default="")
    address=models.TextField( default="")
    join_date = models.DateField(default=datetime.now)
    salary = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    img = models.ImageField(upload_to="employee/", default="")

    is_active = models.BooleanField(default=True, null=True, blank=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Employees"
        verbose_name = "Employee"

    def __str__(self):
        return self.name

class Service(models.Model):
    objects=models.Manager

    name=models.CharField(max_length=100, default='')
    photo = models.CharField(max_length=100,verbose_name="How many photos")
    video = models.CharField(max_length=100,verbose_name="How many videos")
    price = models.CharField(max_length=100)

    is_active=models.BooleanField(default=True, editable=False)
    created_on=models.DateField(default=datetime.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Services"
        verbose_name="Service"

class Client(models.Model):
    objects=models.Manager

    client_id = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.client_id:
            today = timezone.now().strftime('%d%m%Y')
            count_today = Client.objects.filter(client_id__startswith=today).count()
            sequence = f"{count_today + 1:03d}"  
            self.client_id = f"{today}{sequence}"
        super().save(*args, **kwargs)

    name=models.CharField(max_length=100)
    service=models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Service', null=True, blank=True,default='')
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    address=models.TextField()
    pincode=models.IntegerField()

    is_active=models.BooleanField(default=True, editable=False)
    created_on=models.DateField(default=datetime.now, editable=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Clients"
        verbose_name = "Client"

class Deposit(models.Model):
    objects=models.Manager

    client=models.CharField(max_length=100, verbose_name="Client ID")
    name=models.CharField(max_length=100, default='',verbose_name="Client Name")
    phone = models.CharField(max_length=100)
    pay = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    pending = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    total = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")

    is_active=models.BooleanField(default=True, editable=False)
    created_on=models.DateField(default=datetime.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Deposit"
        verbose_name="Deposit"

class Withdraw(models.Model):
    objects=models.Manager

    name=models.CharField(max_length=100, verbose_name="Who withdraw")
    purpose = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    created_on=models.DateField(default=datetime.now, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= "Withdraws"
        verbose_name="Withdraw"

class Project(models.Model):
    objects = models.Manager()

    project_id = models.CharField(max_length=10, unique=True, blank=True,editable=False)
    def save(self, *args, **kwargs):
        if not self.project_id:
            last_pro = Project.objects.order_by('id').last()
            if last_pro:
                last_id = int(last_pro.project_id.replace("PRO", ""))
                new_id = f"PRO{last_id + 1:04d}"
            else:
                new_id = "PRO0001"
            self.project_id = new_id
        super().save(*args, **kwargs)

    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]
    project_name = models.CharField(max_length=100, verbose_name="Project Name")
    client = models.ForeignKey(Client, on_delete=models.CASCADE,verbose_name="Client Name")
    work_on = models.ForeignKey(Emp, on_delete=models.CASCADE, verbose_name="Work On")
    start_date = models.DateField(default=datetime.now, verbose_name="Start Date")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started', verbose_name="Status")

    is_active = models.BooleanField(default=True, null=True, blank=True, editable=False)
    created_on = models.DateField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "Projects"
        verbose_name = "Project"

    def __str__(self):
        return self.project_name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(Emp, on_delete=models.CASCADE)
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_on = models.DateField(default=datetime.now, editable=False)


    def __str__(self):
        return self.title