from django.db import models

class CandidateCertificate(models.Model):
    name = models.CharField(max_length=100)
    space_id = models.CharField(max_length=100)
    certificate_id = models.CharField(max_length=100, default="cert")
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    marks = models.CharField(max_length=100, default="0%")  # Change marks field to CharField to store the percentage symbol
    course = models.CharField(max_length=100, default="ADCA")
    dca = models.IntegerField()
    dtp = models.IntegerField()
    tally = models.IntegerField()
    manual_accounting = models.IntegerField()
    gst = models.IntegerField()
    image = models.TextField(null=True,blank=True)

    def save(self, *args, **kwargs):
        # Calculate total marks
        total_marks = self.dca + self.dtp + self.tally + self.manual_accounting + self.gst

        # Calculate percentage with respect to 500
        percentage = (total_marks / 500) * 100

        # Store the percentage in marks field with percentage symbol
        self.marks = f"{percentage:.2f}%"
        self.certificate_id = "cert"+self.space_id
        
        # Call the parent save method
        super(CandidateCertificate, self).save(*args, **kwargs)
