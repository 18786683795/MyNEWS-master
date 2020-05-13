#!/usr/bin/env python
# encoding: utf-8

import xadmin

from .models import *


# Register your models here.
class ArticleAdmin(object):
    # 列表显示字段
    list_display = ('title', 'item', 'status', 'author', 'publish_date',
                'expiration_date', 'is_active')

    list_filter = ('author', 'status', 'is_active', 'publish_date',
               'expiration_date')
    # 每页记录数
    list_per_page = 25
    # 查询字段
    search_fields = ('title', 'tags', 'slug', 'content')

    class Media:
        js = ('/static/ueditor/ueditor.config.js', '/static/ueditor/ueditor.all.min.js',)


class TagAdmin(object):
    list_display = ('name', 'article_count')

    def article_count(self, obj):
        return Article.objects.filter(tag=obj).count()


class CategoryAdmin(object):
    list_display = ('id', 'title', 'item_count')

    def item_count(self, obj):
        # return obj.item_set.count()
        return Item.objects.filter(categorys=obj).count()


class ItemAdmin(object):
    list_display = ('title', 'created_date', 'categorys', 'completed')


class AdAdmin(object):
    list_display = ('title', 'pic', 'adurl', 'adlocation', 'status')


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Item, ItemAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Ad, AdAdmin)