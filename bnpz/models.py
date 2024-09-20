from django.core.mail import send_mail
from django.db import models
from rest_framework.exceptions import ValidationError
from django.contrib import messages

from bnpz.message import result, subject
from bnpz.send_code import send_code
from config import settings


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Til'


class CategoryNew(models.Model):
    title_uz = models.CharField(max_length=500, verbose_name="Kategoriya nomi (Uzbek)")
    uz = models.CharField(max_length=10, default="uz")
    title_ru = models.CharField(max_length=500, verbose_name="Kategoriya nomi (Русский)")
    ru = models.CharField(max_length=10, default="ru")
    title_en = models.CharField(max_length=500, verbose_name="Kategoriya nomi (English)")
    en = models.CharField(max_length=10, default="en")
    title_kr = models.CharField(max_length=500, verbose_name="Kategoriya nomi (Крилл)")
    kr = models.CharField(max_length=10, default="kr")

    def __str__(self):
        return f"{self.title_uz}"

    class Meta:
        verbose_name = 'CategoryNew'
        verbose_name_plural = '1. Yangiliklar kategoyasi'


class New(models.Model):
    number = models.IntegerField(verbose_name="Nomer: ")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    category = models.ForeignKey(CategoryNew, on_delete=models.CASCADE, verbose_name="Kategoriyani tanlang",
                                 related_name="new")
    title = models.CharField(max_length=400, verbose_name="Sarlavha")
    mainImage = models.ImageField(default="new.png", verbose_name="Asosiy rasm. 500x500 shart", null=True, blank=True)
    description_1 = models.TextField(verbose_name="Ta'rif 1", null=True, blank=True)
    description_2 = models.TextField(verbose_name="Ta'rif 2", null=True, blank=True)
    description_3 = models.TextField(verbose_name="Ta'rif 3", null=True, blank=True)
    description_4 = models.TextField(verbose_name="Ta'rif 4", null=True, blank=True)
    description_5 = models.TextField(verbose_name="Ta'rif 5", null=True, blank=True)
    img_1 = models.ImageField(verbose_name="Rasm 1", null=True, blank=True)
    img_2 = models.ImageField(verbose_name="Rasm 2", null=True, blank=True)
    img_3 = models.ImageField(verbose_name="Rasm 3", null=True, blank=True)
    img_4 = models.ImageField(verbose_name="Rasm 4", null=True, blank=True)
    img_5 = models.ImageField(verbose_name="Rasm 5", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name="Active:")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = '1.1 Yangiliklar'


class Video(models.Model):
    video_1 = models.CharField(max_length=250, verbose_name="1-video", null=True, blank=True)
    video_2 = models.CharField(max_length=250, verbose_name="2-video", null=True, blank=True)
    video_3 = models.CharField(max_length=250, verbose_name="3-video", null=True, blank=True)

    def __str__(self):
        return f"Asosiy sahifa videolari"

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = '2. Asosiy videolar'


class Product(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    name = models.CharField(max_length=200, verbose_name="Nomi")
    image = models.ImageField(verbose_name="Asosiy rasm, 500x500 shart")
    advantage = models.TextField(null=True, blank=True, verbose_name="Afzalligi")
    field = models.TextField(null=True, blank=True, verbose_name="Qo'llash sohasi")
    marka = models.CharField(max_length=250, null=True, blank=True, verbose_name="Marka")
    document = models.CharField(max_length=250, null=True, blank=True, verbose_name="Normativ hujjat")
    world_standart = models.CharField(max_length=250, null=True, blank=True, verbose_name="jahon me'yorlariga mosligi")
    used = models.CharField(max_length=350, null=True, blank=True, verbose_name="Istemolchi")
    date = models.CharField(max_length=150, null=True, blank=True, verbose_name="O'zlashtirish sanasi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = '3. Maxsulotlar'


class FAQ(models.Model):
    number = models.IntegerField(verbose_name="Nomer")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    question = models.TextField(verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")
    file = models.FileField(verbose_name="Qo`llanma", null=True, blank=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = '5. Savol&Javob'


class Gallery(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    title = models.CharField(max_length=500, verbose_name="Sarlavha")
    date = models.DateTimeField(auto_now_add=True)
    img_1 = models.ImageField(verbose_name="Rasm 1", null=True, blank=True)
    img_2 = models.ImageField(verbose_name="Rasm 2", null=True, blank=True)
    img_3 = models.ImageField(verbose_name="Rasm 3", null=True, blank=True)
    img_4 = models.ImageField(verbose_name="Rasm 4", null=True, blank=True)
    img_5 = models.ImageField(verbose_name="Rasm 5", null=True, blank=True)
    img_6 = models.ImageField(verbose_name="Rasm 6", null=True, blank=True)
    img_7 = models.ImageField(verbose_name="Rasm 7", null=True, blank=True)
    img_8 = models.ImageField(verbose_name="Rasm 8", null=True, blank=True)
    img_9 = models.ImageField(verbose_name="Rasm 9", null=True, blank=True)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = '6. Galereya'


class CategoryTender(models.Model):
    title_uz = models.CharField(max_length=500, verbose_name="Kategoriya nomi (Uzbek)")
    uz = models.CharField(max_length=10, default="uz")
    title_ru = models.CharField(max_length=500, verbose_name="Kategoriya nomi (Русский)")
    ru = models.CharField(max_length=10, default="ru")
    title_en = models.CharField(max_length=500, verbose_name="Kategoriya nomi (English)")
    en = models.CharField(max_length=10, default="en")
    title_kr = models.CharField(max_length=500, verbose_name="Kategoriya nomi (Крилл)")
    kr = models.CharField(max_length=10, default="kr")

    def __str__(self):
        return f"{self.title_uz}"

    class Meta:
        verbose_name = 'CategoryTender'
        verbose_name_plural = '4. Tanlov kategoyasi'


class Selection(models.Model):
    number = models.IntegerField(verbose_name="Nomer: ")
    category = models.ForeignKey(CategoryTender, on_delete=models.CASCADE, verbose_name="Tanlov kategoriyasi")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    service = models.CharField(max_length=500, verbose_name="Sarlavha")
    condition = models.TextField(verbose_name="Maxsus shart", null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    term = models.DateField(verbose_name="Ohirgi muddat")
    phone = models.CharField(max_length=250, null=True, blank=True, verbose_name="Telefon raqam")
    view = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.service}-{self.language}"

    class Meta:
        verbose_name = 'Selection'
        verbose_name_plural = '4.1 Tanlovlar'


class SelectionProduct(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE, verbose_name="Tanlovning nomi")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    title = models.CharField(max_length=500, verbose_name="Maxsulot nomi")
    count = models.IntegerField(null=True, blank=True, verbose_name="Miqdori")
    file = models.FileField(verbose_name="Техническая задача (.pdf)", null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Aktiv")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'SelectionProduct'
        verbose_name_plural = '4.2 Tanlov maxsuloti'


class Message(models.Model):
    firstName = models.CharField(max_length=50, verbose_name="Ism")
    lastName = models.CharField(max_length=50, verbose_name="Familiya")
    address = models.TextField(verbose_name="Manzil")
    bthDate = models.CharField(max_length=50, verbose_name="Tug'ilgan yili")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqam")
    email = models.CharField(max_length=150, verbose_name="Email")
    theme = models.TextField(verbose_name="Murojaat mavzu")
    text = models.TextField(verbose_name="Murojaat matni")
    date = models.DateField(auto_now_add=True, )
    cause = models.TextField(null=True, blank=True, verbose_name="Murojaatga javob")
    file = models.FileField(verbose_name="Murojaat natijasi fayl shaklida", null=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name="Ko'rib chiqildi")

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def save(self, *args, **kwargs):
        if self.is_active and self.cause:
            send_code(f"998{self.phone[7:].replace(' ', '')}", f'"Buxoro neftni qayta ishlash zavodi" MCHJ. {result}')
            send_mail(subject, result, settings.EMAIL_HOST_USER, [self.email],
                      fail_silently=False)
            super().save()
            return {"is_active": True}
        elif self.is_active and not self.cause:
            return
        elif not self.is_active and self.cause:
            return
        super().save()

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = '7. Murojaatlar'


class SmsCode(models.Model):
    phone = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    code = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return self.phone

    class Meta:
        db_table = 'main_sms_code'


class Eskiz(models.Model):
    token = models.TextField(null=True, blank=True)


class Statistic(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    title = models.CharField(max_length=200, verbose_name="Hajm")
    titleAdd = models.CharField(max_length=200, verbose_name="Hajm birligi")
    subtitle = models.TextField(verbose_name="Nomi")
    img = models.ImageField(verbose_name="Rasm")

    def __str__(self):
        return f"{self.title} {self.titleAdd} {self.subtitle}"

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = '8. Statistika'


class Site(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    title = models.CharField(max_length=200, verbose_name="Sayt nomi")
    img = models.ImageField(verbose_name="Sayt logosi (.png shart)")
    link = models.TextField(verbose_name="Veb sayt linki")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = '9. Foydali saytlar'


class Certificate(models.Model):
    number = models.IntegerField(verbose_name="Nomer")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    title = models.CharField(max_length=200, verbose_name="Nomi")
    subtitle = models.TextField(verbose_name="Ta'rif")
    description_1 = models.TextField(null=True, blank=True, verbose_name="Matn 1")
    description_2 = models.TextField(null=True, blank=True, verbose_name="Matn 2")
    description_3 = models.TextField(null=True, blank=True, verbose_name="Matn 3")
    img = models.ImageField(verbose_name="Rasm")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = '9.1. Sertifikat'


class LocalDocs(models.Model):
    title = models.TextField(verbose_name="Hujjat nomi")
    file = models.FileField(verbose_name="Fayl")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'LocalDocs'
        verbose_name_plural = "9.2. Lokal me'yoriy hujjatlar"


class Lider(models.Model):
    number = models.IntegerField(verbose_name="Nomer")
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Tilni tanlang")
    position = models.CharField(max_length=500, verbose_name="Lavozimi")
    firstName = models.CharField(max_length=500, verbose_name="Ism")
    lastName = models.CharField(max_length=500, verbose_name="Familiya")
    sureName = models.CharField(max_length=500, verbose_name="Otasining ismi")
    phone = models.CharField(max_length=500, verbose_name="Telefon raqami")
    acceptance = models.TextField(verbose_name="Qabul kunlari")
    img = models.ImageField(verbose_name="Rasm")
    experience_1 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 1")
    experience_2 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 2")
    experience_3 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 3")
    experience_4 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 4")
    experience_5 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 5")
    experience_6 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 6")
    experience_7 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 7")
    experience_8 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 8")
    experience_9 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 9")
    experience_10 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 10")
    experience_11 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 11")
    experience_12 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 12")
    experience_13 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 13")
    experience_14 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 14")
    experience_15 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Mehnat faoliyati 15")
    functional_1 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 1")
    functional_2 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 2")
    functional_3 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 3")
    functional_4 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 4")
    functional_5 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 5")
    functional_6 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 6")
    functional_7 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 7")
    functional_8 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 8")
    functional_9 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 9")
    functional_10 = models.CharField(max_length=500, null=True, blank=True, verbose_name="Funksional majburiyati 10")

    def __str__(self):
        return f"{self.number}. {self.language} - {self.lastName} {self.firstName}"

    class Meta:
        verbose_name = 'Lider'
        verbose_name_plural = "9.3. Rahbariyat"


class Captcha(models.Model):
    code = models.CharField(max_length=50, verbose_name="Code", null=True, blank=True)
    shifr = models.CharField(max_length=50, verbose_name="Shifr", null=True, blank=True)

    def __str__(self):
        return self.code
