from django.contrib.auth import get_user_model
from django import template
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from blog.models import Post

user_model = get_user_model()
register = template.Library()

@register.filter(name="author_details")
def author_details(post_author, current_user=None):
  if not isinstance(post_author, user_model):
    return ""
    
  if post_author == current_user:
    return format_html("<strong>me</strong>")

  full_name = post_author.username
  first_name, last_name = post_author.first_name, post_author.last_name

  if first_name and last_name:
    full_name = f"{first_name} {last_name}"

  email = post_author.email

  if email:
    # email = escape(email)
    return format_html('<a href="mailto:{}">{}</a>', email, full_name)

    # return mark_safe(clickable_name)
  
  return full_name

@register.simple_tag(takes_context=True)
def author_details_tag(context):
  request = context['request']
  current_user = request.user
  post = context['post']
  author = post.author

  if author == current_user:
    return format_html("<strong>me</strong>")

  full_name = author.username
  first_name, last_name = author.first_name, author.last_name

  if first_name and last_name:
    full_name = f"{first_name} {last_name}"

  email = author.email

  if email:
    return format_html('<a href="mailto:{}">{}</a>', email, full_name)
    
  return full_name

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
  posts = Post.objects.exclude(pk=post.pk)[:5]
  return {"title": "Recent Posts", "posts": posts}

@register.simple_tag
def row(class_names=""):
    return format_html("""
      <div class="row {}">
    """, class_names)

@register.simple_tag
def endrow():
  return format_html("</div>")
  
@register.simple_tag
def col(class_names=""):
  return format_html("""<div class="col {}">""", class_names)

@register.simple_tag
def endcol():
  return format_html("</div>")


