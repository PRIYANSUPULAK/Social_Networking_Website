from django.contrib import admin
from . import models

# Register your models here.
# This Inline Class helps us to edit the group members from our Admin page directly.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)


# Register your models here.
