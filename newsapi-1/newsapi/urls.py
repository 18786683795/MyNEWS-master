"""newsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from . import settings
import article.views as view
from django.conf.urls import include,url
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='新闻系统 API')
# 建立一个路由对象
router = DefaultRouter()
# 将我们的路由注册到url里
router.register(r'category', view.CategoryViewset, basename='category')
router.register(r'categoryitems', view.CategoryitemsViewset, basename='categoryitems')
router.register(r'categoryStringitems', view.CategoryStringitemsViewset, basename='categoryStringitems')
router.register(r'categoryPrimaryKeyitems', view.CategoryPrimaryKeyitemsViewset, basename='categoryPrimaryKeyitems')
router.register(r'categorySlugitems', view.CategorySlugitemsViewset, basename='categorySlugitems')
router.register(r'item', view.ItemViewset, basename='item')
router.register(r'tag', view.TagViewset, basename='tag')
router.register(r'ad', view.AdViewset, basename='ad')
router.register(r'articleList', view.ArticleListViewSet, basename="articleList")
router.register(r'hot_articleList', view.Hot_articleListViewSet, basename="hot_articleList")
router.register(r'user', view.UserViewset, basename="user")
router.register(r'userLogin', view.UserLoginViewset, basename="userLogin")
router.register(r'setPassword', view.UserSetPasswordViewset, basename="setPassword")
router.register(r'userFav', view.UserFavViewset, basename="userFav")

urlpatterns = [
    #re_path('', schema_view),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('docs/', include_docs_urls(title="后台接口文档")),
    re_path('login/', view.UserLogin.as_view(), name="login"),
	path('', include(router.urls)),

]
#urlpatterns += router.urls
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
