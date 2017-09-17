from django.contrib import admin
from .models import Category, Product


# admin.site.empty_value_display = '空值'


# Register your models here.

# 1）定义模型管理类
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'desc_view')

    # empty_value_display = '<空>'

    def desc_view(self, obj):
        return obj.description

    desc_view.empty_value_display = '-未填写-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def custom_discontinued(self, obj):
        return '停产' if obj.discontinued else '在产'

    custom_discontinued.short_description = '生产状态'

    list_display = (
        'name', 'category', 'unit_price', 'quantity_per_unit', 'custom_discontinued', 'discontinued', 'posted_time')
    list_display_links = ('name', 'unit_price',)
    list_editable = ('quantity_per_unit',)
    list_filter = ('discontinued', 'category')
    list_per_page = 20
    list_select_related = ('category',)
    ordering = ('-unit_price', 'discontinued',)

    search_fields = ['name']

    # 针对编辑页选项
    # fields = (('name', 'category'), 'quantity_per_unit')
    # exclude = ('unit_in_stock',)
    # fieldsets = (
    #     ('主要信息', {
    #         'fields': ('name', 'category', 'unit_price')
    #     }),
    #     ('选项', {
    #         'fields': ('quantity_per_unit', 'units_in_stock', 'discontinued')
    #     })
    # )
    # readonly_fields = ('units_in_stock',)

    # 列表页自定义行为批量操作
    def make_continued(self, request, queryset):
        queryset.update(discontinued=False)

    make_continued.short_description = '设为在产'
    actions = [make_continued, ]


# 2）注册模型管理类到站点管理
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Product, ProductAdmin)
