from django.db import models
# slugify helps in removing any character which isn't alpha-numeric or underscores or hyphens
# Mainly, slugify converts spaces into '-' for making it a url
from django.utils.text import slugify
from django.urls import reverse

# pip install misaka
# misaka helps in marking down (link links) inside the posts.
import misaka

# get_user_model funtion returns the user modeel thats currently active in this project
# It basically helps in finding out which user is signed in or else no one is signed in.
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)
# Slugs are a “URL friendly” version of the product or category name. They are typically lowercase, contain no special characters and hyphens are used in place of spaces.
# Unicode provides a unique code value for every character, regardless of the platform, program, or language.
    slug = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField(blank = True, default = '')
    description_html = models.TextField(editable = False, default = '', blank = True)
    members = models.ManyToManyField(User, through = 'GroupMember')


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        # This super is same as of java. It is saving to the base class
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs = {'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name = "memberships",on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name = "user_groups",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        unique_together = ('group', 'user')
