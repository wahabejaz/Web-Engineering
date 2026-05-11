from django.db import models
from django.utils.text import slugify

class Profile(models.Model):
    name = models.CharField(max_length=200, default="Wahab Ejaz")
    title = models.CharField(max_length=200, default="Full Stack Developer")
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True, help_text="Upload your resume PDF")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    category = models.CharField(
        max_length=50, 
        choices=[
            ('frontend', 'Frontend'),
            ('backend', 'Backend'),
            ('tools', 'Tools & Platforms'),
            ('other', 'Other'),
        ],
        default='other'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=250, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    technologies = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Projects'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']
        verbose_name_plural = 'Experience'

    def __str__(self):
        return f"{self.position} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_year']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} in {self.field_of_study}"


class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('twitter', 'Twitter'),
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('email', 'Email'),
        ('youtube', 'YouTube'),
        ('portfolio', 'Portfolio'),
    ]
    
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, unique=True)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, blank=True, help_text="e.g., fab fa-github")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['platform']
        verbose_name_plural = 'Social Links'

    def __str__(self):
        return self.platform


class Testimonial(models.Model):
    author_name = models.CharField(max_length=200)
    author_title = models.CharField(max_length=200, blank=True)
    author_image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    content = models.TextField()
    rating = models.IntegerField(
        choices=[(i, f'{i} Star{"s" if i != 1 else ""}') for i in range(1, 6)],
        default=5
    )
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"Review from {self.author_name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name