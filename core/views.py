from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Profile, Skill, Project, Experience, Education, SocialLink, Testimonial, Contact
# Import custom template tags to ensure they're registered
from .templatetags import custom_filters

def home(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            subject = request.POST.get('subject', '').strip()
            message_text = request.POST.get('message', '').strip()
            
            if not name or not email or not message_text:
                messages.error(request, 'Please fill in all required fields.')
            else:
                Contact.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message_text
                )
                messages.success(request, 'Message sent successfully! We will get back to you soon.')
                return redirect('home')
        except Exception as e:
            messages.error(request, f'Error sending message: {str(e)}')
    
    # Get data for display
    skills_by_category = {}
    for skill in Skill.objects.all():
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    # Get featured projects first, then all projects
    featured_projects = Project.objects.filter(featured=True)
    all_projects = Project.objects.all()
    
    # Pagination for projects
    paginator = Paginator(all_projects, 6)  # 6 projects per page
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    # Get experience and education
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    
    # Get approved testimonials
    testimonials = Testimonial.objects.filter(approved=True)
    
    # Get social links
    social_links = SocialLink.objects.all()
    
    # Get profile
    profile = Profile.objects.first()
    
    context = {
        'profile': profile,
        'skills_by_category': skills_by_category,
        'featured_projects': featured_projects,
        'projects_page': projects_page,
        'paginator': paginator,
        'experiences': experiences,
        'educations': educations,
        'testimonials': testimonials,
        'social_links': social_links,
    }
    
    return render(request, 'home.html', context)

def project_detail(request, slug):
    """Display detailed view of a project"""
    project = get_object_or_404(Project, slug=slug)
    
    # Increment view count
    project.view_count += 1
    project.save(update_fields=['view_count'])
    
    # Get related projects (same technologies)
    related_projects = Project.objects.filter(
        technologies__icontains=project.technologies[0:50]
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    
    return render(request, 'project_detail.html', context)

def search_projects(request):
    """Search for projects by title, description, or technologies"""
    query = request.GET.get('q', '').strip()
    results = []
    
    if query:
        results = Project.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(technologies__icontains=query)
        )
    
    paginator = Paginator(results, 6)
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    context = {
        'query': query,
        'projects_page': projects_page,
        'paginator': paginator,
        'results_count': len(results),
    }
    
    return render(request, 'search_results.html', context)

def about(request):
    """About page with experience and education"""
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    social_links = SocialLink.objects.all()
    profile = Profile.objects.first()
    
    # Calculate total experience in years
    current_experiences = experiences.filter(is_current=True)
    total_years = sum([
        (e.end_date.year - e.start_date.year) if e.end_date 
        else ((datetime.now().year - e.start_date.year) if e.is_current else 0)
        for e in experiences
    ])
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'social_links': social_links,
        'total_years': total_years,
        'projects_count': Project.objects.count(),
        'skills_count': Skill.objects.count(),
    }
    
    return render(request, 'about.html', context)

from datetime import datetime

def download_resume(request):
    """Download the resume from profile"""
    profile = Profile.objects.first()
    
    if profile and profile.resume:
        from django.http import FileResponse
        from django.utils.text import slugify
        
        # Get the file
        file = profile.resume.open('rb')
        filename = f"{slugify(profile.name)}_resume.pdf"
        
        response = FileResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
    else:
        return redirect('home')