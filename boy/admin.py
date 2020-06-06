from django.contrib import admin
#import home_page

# Register your models here.
from .models import Grades,Students,Plans,Schools
class Studentinfo(admin.TabularInline):
    model = Students
    extra = 2
@admin.register(Students)#装饰器注册
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.xgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"

    list_display = ["xname",gender,"xgrade","isDelete","xage",'pk']
    list_filter = ["xgrade"]
    search_fields = ["xname"]
    list_per_page = 5
    #fields = ["xname","xid","xage","xgender","xgrade","isDelete"]
#admin.site.register(Students,StudentsAdmin)
class GradesAdmin(admin.ModelAdmin):
    inlines = [Studentinfo]
    list_display = ["gyear","ggirlnum","gboynum","gschool","isDelete",'pk']
    list_filter = ["gschool","gyear"]
    search_fields = ["gyear","gid","gschool"]
    list_per_page = 5
    #fields = ["gyear","gid","ggirlnum","gboynum","gschool","isDelete"]

admin.site.register(Grades,GradesAdmin)
class SchoolsAdmin(admin.ModelAdmin):
    list_display = ["sname","sdate","scity","isDelete",'pk']
    list_filter = ["scity"]
    search_fields = ["sname","sid"]
    list_per_page = 5
    #fields = ["sname","sid","sdate","scity","isDelete"]
admin.site.register(Schools,SchoolsAdmin)
class PlansAdmin(admin.ModelAdmin):
    list_display = ["pname","plong","pp_long","pp_start_time","pstart_time","pscore","pstudent",'pk']
    list_filter = ["pstudent"]
    search_fields = ["pname","pstudent"]
    list_per_page = 5
    #fields = ["pname","plong","pp_long","pp_start_time","pstart_time","pscore","pstudent","pover_time"]
admin.site.register(Plans,PlansAdmin)
