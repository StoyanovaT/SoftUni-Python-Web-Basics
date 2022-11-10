from django.contrib import admin

from models_demos.web.models import Employee, NullBlankDemo, Department, Project, Category


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level')
    list_filter = ('level', 'first_name')
    search_fields = ('first_name', 'last_name')

    # fieldsets = (
    #     (
    #         'Personal Info',
    #         {
    #             'fields': ('first_name', 'last_name', 'age'),
    #         }
    #     ),
    #     (
    #         'Professional Info',
    #         {
    #             'fields': ('level', 'years_of_experience'),
    #         }
    #     ),
    #     (
    #         'Company Info',
    #         {
    #             'fields': ('department', 'is_full_time', 'start_date')
    #         }
    #     ),
    # )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
