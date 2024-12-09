from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hero(models.Model):
    hero_desc = models.TextField()
    hero_title = models.CharField(max_length = 100)
    hero_btn = models.CharField(max_length=50)
    hero_image = models.ImageField(upload_to='hero/')

    def __str__(self):
        return self.hero_title

class Section(models.Model):
    desc = models.TextField()
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='sections/')
    feature_1 = models.TextField()
    feature_2 = models.CharField(max_length=100, default='default_value')
    feature_3 = models.CharField(max_length=100, default='default_value')

    def __str__(self):
        return self.title




class WhyUsSection(models.Model):
    main_title = models.CharField(max_length=255)
    main_description = models.TextField()
    more_button_link = models.CharField(max_length=50)

    def __str__(self):
        return self.main_title

class WhyUsFeature(models.Model):
    section = models.ForeignKey(WhyUsSection, related_name='features', on_delete=models.CASCADE)
    icon = models.CharField(max_length=255)  # Store the icon class name (e.g., bi-clipboard-data)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Feature(models.Model):
    icon = models.CharField(max_length=100)  # Store the icon class (e.g., 'bi bi-eye')
    title = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=15)  # Color of the icon, stored as hex code (e.g., '#ffbb2c')
    order = models.IntegerField(default=0)  # Optional: Helps control the order in which features are displayed

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Contact Info for {self.city}"

class SocialLink(models.Model):
    platform = models.CharField(max_length=50)  
    url = models.URLField()  
    icon_class = models.CharField(max_length=50)  

    def __str__(self):
        return self.platform

class UsefulLink(models.Model):
    name = models.CharField(max_length=100)  
    url = models.CharField(max_length=255)  

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)  
    url = models.CharField(max_length=255, blank=True, null=True)  

    def __str__(self):
        return self.name


class AboutTitle(models.Model):
    about_title = models.CharField(max_length=100)
    about_desc = models.TextField()
    background_image = models.ImageField(upload_to='about/', blank=True, null=True, default=None)

    def __str__(self):
        return self.about_title
    

class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='about/')
    feature1 = models.CharField(max_length=250)
    feature2 = models.CharField(max_length=250)
    feature3 = models.CharField(max_length=250)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='testimonial/')

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title



class SkillCategory(models.Model):
    skill_title = models.CharField(max_length=100)
    skill_desc = models.TextField()
    skill_btn = models.CharField(max_length=100)
    skill_image = models.ImageField(upload_to='skills/')

    def __str__(self):
        return self.skill_title


class SkillFeature(models.Model):
    feature_title = models.CharField(max_length=100)
    feature_desc = models.TextField()
    feature_img = models.ImageField(upload_to='features/',default='default_image.jpg')
    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='features',default=1)

    def __str__(self):
        return self.feature_title



class UploadSkill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    file = models.FileField(upload_to='skills/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'learn_skill' 

    def __str__(self):
        return self.name


class SkillRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who requested the skill
    skill_name = models.CharField(max_length=255)
    skill_description = models.TextField()
    status = models.CharField(max_length=50, default="Pending")  # E.g., "Pending", "Fulfilled"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.skill_name} by {self.user.username}"


class Feedback(models.Model):
    skill_request = models.ForeignKey(SkillRequest, related_name='feedbacks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User giving the feedback
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.skill_request.skill_name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default.jpg')

    def __str__(self):
        return self.user.username













