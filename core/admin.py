from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Skill, Project, Experience, Education, SocialLink, Testimonial, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'image_preview', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio')
        }),
        ('Media', {
            'fields': ('image', 'image_preview', 'resume')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="150" height="150" style="border-radius: 10px;" />',
                obj.image.url
            )
        return 'No image'
    image_preview.short_description = 'Preview'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage', 'category', 'created_at')
    search_fields = ('name',)
    list_filter = ('percentage', 'category', 'created_at')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Skill Information', {
            'fields': ('name', 'percentage', 'category')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured_badge', 'view_count', 'created_at')
    search_fields = ('title', 'technologies', 'description')
    list_filter = ('featured', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'view_count', 'slug')
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'description', 'image')
        }),
        ('Links & Details', {
            'fields': ('github_link', 'live_link', 'technologies')
        }),
        ('Status', {
            'fields': ('featured', 'view_count')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    
    def featured_badge(self, obj):
        if obj.featured:
            return '⭐ Featured'
        return '—'
    featured_badge.short_description = 'Status'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'start_date', 'end_date', 'current_badge')
    search_fields = ('position', 'company', 'description')
    list_filter = ('is_current', 'start_date')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Job Information', {
            'fields': ('company', 'position', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
    
    def current_badge(self, obj):
        if obj.is_current:
            return '✓ Currently Working'
        return '—'
    current_badge.short_description = 'Status'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'field_of_study', 'start_year', 'end_year')
    search_fields = ('degree', 'institution', 'field_of_study')
    list_filter = ('start_year', 'institution')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Education Details', {
            'fields': ('institution', 'degree', 'field_of_study', 'description')
        }),
        ('Duration', {
            'fields': ('start_year', 'end_year')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'icon_class')
    search_fields = ('platform', 'url')
    list_filter = ('platform',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Social Media', {
            'fields': ('platform', 'url', 'icon_class')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_title', 'rating_stars', 'approved_badge', 'created_at')
    search_fields = ('author_name', 'content')
    list_filter = ('approved', 'rating', 'created_at')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Author Information', {
            'fields': ('author_name', 'author_title', 'author_image')
        }),
        ('Review', {
            'fields': ('content', 'rating')
        }),
        ('Status', {
            'fields': ('approved',)
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
    
    def rating_stars(self, obj):
        return '⭐' * obj.rating
    rating_stars.short_description = 'Rating'
    
    def approved_badge(self, obj):
        if obj.approved:
            return '✓ Approved'
        return '⏳ Pending'
    approved_badge.short_description = 'Status'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'read_badge', 'created_at')
    search_fields = ('name', 'email', 'message', 'subject')
    list_filter = ('is_read', 'replied', 'created_at')
    readonly_fields = ('created_at', 'name', 'email', 'message', 'subject')
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'replied')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
    
    def has_add_permission(self, request):
        return False
    
    def read_badge(self, obj):
        if obj.is_read:
            return '✓ Read'
        return '📬 Unread'
    read_badge.short_description = 'Status'