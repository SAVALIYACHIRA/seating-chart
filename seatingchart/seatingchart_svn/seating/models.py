#Author Michael Lee Harrison

from django.db import models

# Create your models here.
RANK_CHOICES = (
                ('Gen','General'),
                ('LtGen','Lieutenant General'),
                ('MajGen','Major General'),
                ('BGen','Brigadier General'),
                ('Col','Colonel'),
                ('LtCol','Lieutenant Colonel'),
                ('Maj','Major'),
                ('Capt','Captain'),
                ('1stLt','First Lieutenant'),
                ('2ndLt','Second Lieutenant'),
                ('COW5','Chief Warrent Officer-5'),
                ('COW4','Chief Warrent Officer-4'),
                ('COW3','Chief Warrent Officer-3'),
                ('COW2','Chief Warrent Officer-2'),
                ('OW','Warrent Officer'),
                ('SgtMaj','Sergeant Major'),
                ('MGySgt','Master Gunnery Sergeant'),
                ('1stSgt','First Sergeant'),
                ('MSgt','Master Sergeant'),
                ('GySgt','Gunnery Sergeant'),
                ('SSgt','Staff Sergeant'),
                ('Sgt','Sergeant'),
                ('Cpl','Corporal'),
                ('LCpl','Lance corporal'),
                ('Pfc','Private First Class'),
                ('Pvt','Private'),                
                )

class Table(models.Model):
    tNumber = models.CharField(max_length=1,primary_key=True)
    seatsFilled = models.CharField(max_length=1)
    def __unicode__(self):
        return u'Table %s' % (self.tNumber)
    
class Sponsor(models.Model):
    rank = models.CharField(max_length=1,choices=RANK_CHOICES,null=True, blank=True)
    LName = models.CharField(max_length=30)
    mName = models.CharField(max_length=30)
    fName = models.CharField(max_length=30)
    cellNumber = models.CharField(max_length=10)
    deskNumber = models.CharField(max_length=10)
    email = models.EmailField()
    def __unicode__(self):
        return u'%s %s, %s %s.' % (self.rank,self.LName,self.fName,self.mName)
    
class Occupant(models.Model):
    LName = models.CharField(max_length=30)
    mName = models.CharField(max_length=30)
    fName = models.CharField(max_length=30)
    def __unicode__(self):
        return u'%s %s %s' % (self.fName,self.mName,self.LName)  
        
class Seat(models.Model):
    sNumber = models.CharField(max_length=1,primary_key=True)
    table = models.ForeignKey(Table)
    sponsor = models.ForeignKey(Sponsor)
    occupant = models.ForeignKey(Occupant)
    def __unicode__(self):
        return u'%s - %s, %s %s' % (self.alpha,self.LName,self.fName,self.mName)