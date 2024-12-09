from django.contrib import admin
from . models import Hero,Section,WhyUsSection, WhyUsFeature, Feature, ContactInfo, SocialLink, UsefulLink, Service, AboutTitle, AboutUs
from . models import Testimonial,SkillCategory,SkillFeature,UploadSkill
# Register your models here.
admin.site.register(Hero)
admin.site.register(Section)
admin.site.register(WhyUsSection)
admin.site.register(WhyUsFeature)
admin.site.register(Feature)
admin.site.register(ContactInfo)
admin.site.register(SocialLink)
admin.site.register(UsefulLink)
admin.site.register(Service)
admin.site.register(AboutTitle)
admin.site.register(AboutUs)
admin.site.register(Testimonial)
admin.site.register(SkillCategory)
admin.site.register(SkillFeature)
admin.site.register(UploadSkill)


