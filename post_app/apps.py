from django.apps import AppConfig


class PostAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'
    name = 'post_app'
    icon = 'fas fa-blog'
