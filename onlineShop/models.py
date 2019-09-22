from django.db import models
from django.urls import reverse
from datetime import datetime

from django.conf import settings
from django.db.models.signals import post_save

# import stripe

# stripe.api_key = settings.STRIPE_SECRET_KEY


class MainCategory(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'main_category'
        verbose_name_plural = 'main_categories'
    
    # def get_absolute_url(self):
    #    return reverse('onlineShop:product_list_by_category', args=[self.slug])


class Category(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    # def get_absolute_url(self):
    #    return reverse('onlineShop:product_detail', args=[self.id, self.slug])


class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #    return reverse('onlineShop:product_detail', args=[self.id, self.slug])


class Product(models.Model):
    main_category = models.ForeignKey(MainCategory, related_name='products', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150, unique=False)
    description = models.TextField()
    brand = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=15,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    # def get_absolute_url(self):
    #    return reverse('onlineShop:ProductDetailPage', args=[self.id, self.slug])
# def soft_delete(self):
#     self.is_deleted = True
#     self.deleted_at = datetime.now()
#     self.save()



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, blank=True)
    phoneNumber = models.PositiveIntegerField()
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    #eproducts = models.ManyToManyField(Product, blank=True)
    #stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        #return self.user.username
         return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    user_profile, created = Profile.objects.get_or_create(user=instance)
    user_profile.save()

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

#@receiver(post_save, sender=User)
#def post_save_profile_create(sender, instance, created, **kwargs):
     #if created:
       # Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()


# def post_save_profile_create(sender, instance, created, *args, **kwargs):
#     user_profile, created = Profile.objects.get_or_create(user=instance)

#     if user_profile.stripe_id is None or user_profile.stripe_id == '':
#         new_stripe_id = stripe.Customer.create(email=instance.email)
#         user_profile.stripe_id = new_stripe_id['id']
#         user_profile.save()


# post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)
