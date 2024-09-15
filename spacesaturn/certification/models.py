from django.db import models

class CandidateCertificate(models.Model):
    name = models.CharField(max_length=100)
    space_id = models.CharField(max_length=100)
    certificate_id = models.CharField(max_length=100, default="cert")
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    marks = models.CharField(max_length=100, default="0%")  # Change marks field to CharField to store the percentage symbol
    course = models.CharField(max_length=100, default="ADCA")
    cs_fundamental_window = models.IntegerField()
    ms_word = models.IntegerField()
    ms_excel = models.IntegerField()
    ms_powerpoint = models.IntegerField()
    ms_outlook_internet = models.IntegerField()
    ms_access = models.IntegerField()
    man_acc_tally_erp = models.Inpagemaker_photoshop_gst_coreldraw = models.IntegerField()
    pagemaker_photoshop_gst_coreldraw = models.IntegerField()
    image = models.TextField(null=True,blank=True)

    def save(self, *args, **kwargs):
        # Calculate total marks
        total_marks = self.ms_access + self.man_acc_tally_erp + self.pagemaker_photoshop_gst_coreldraw + self.cs_fundamental_window + self.ms_word + self.ms_excel + self.ms_powerpoint + self.ms_outlook_internet

        # Calculate percentage with respect to 500
        percentage = (total_marks / 800) * 100

        # Store the percentage in marks field with percentage symbol
        self.marks = f"{percentage:.2f}%"
        self.certificate_id = "cert"+self.space_id
        
        # Call the parent save method
        super(CandidateCertificate, self).save(*args, **kwargs)
