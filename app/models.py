from django.db import models

# Create your models here.

class Bolimlar(models.Model):
    nomi = models.CharField(max_length=200)
    def __str__(self):
        return self.nomi
    class Meta:
        verbose_name = 'Bolim'
        verbose_name_plural = 'Bolimlar'


class Hodimlar(models.Model):
    ism_sharifi = models.CharField(max_length=200)
    bolimi = models.ForeignKey(Bolimlar, on_delete=models.CASCADE)
    lavozimi = models.CharField(max_length=200, help_text='Lavozimingiz ')
    stavka = models.FloatField()
    
    def __str__(self):
        return f"{self.ism_sharifi}"
    
    class Meta:
        verbose_name = 'Hodim'
        verbose_name_plural = 'Hodimlar'


class Malumoti(models.Model):
    ism_sharifi = models.ForeignKey(Hodimlar, on_delete = models.CASCADE)
    tugilgan_yil = models.IntegerField()
    millati = models.CharField(max_length=500, help_text='Millati: ')
    tamomlagan = models.CharField(max_length=500, help_text='Bitirgan ')
    mutaxasis = models.CharField(max_length=500, help_text='Soxasi ')
    ilmiy_darajasi = models.CharField(max_length=500, help_text='Drajasi: ')
    biladigan_tillari = models.CharField(help_text='tillar: ', max_length=500)
    mukofotlari = models.CharField(max_length=500, help_text='muKofotlari ')
    mehnat_faoliyati = models.TextField()
    
    def __str__(self):
        return f'{self.ism_sharifi}'
    class Meta:
        verbose_name = 'Malumot'
        verbose_name_plural = 'Malumotlar'

        
class Qarindoshlar(models.Model):
    hodim = models.ForeignKey(Malumoti, on_delete=models.CASCADE)
    qarindoshligi = models.CharField(max_length=500, help_text="Kim ekanini kiriting.....")
    qarindosh_ismi = models.CharField(max_length=500, help_text="Qarindoshni kiriting.....")
    qarindosh_tug_yil = models.DateField()
    yashash_joyi = models.CharField(max_length=500, help_text="Yashash manzil...")
    ish_joyi = models.CharField(max_length=500, help_text="Ish manzil...")

    def __str__(self):
        return "hodim"

    class Meta:
            verbose_name = 'Qarindoshi'
            verbose_name_plural = 'Qarindoshlari'
    




