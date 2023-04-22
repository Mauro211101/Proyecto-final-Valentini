from django.contrib import admin
from miBlog.models import Post
from Account.models import Profile

admin.site.register(Post)
admin.site.register(Profile)
# Register your models here.
