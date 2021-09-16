from django.contrib import admin

from .models import Info

# Register your models here.

admin.site.register(Info)

# @admin.register(info)
# class info(admin.ModelAdmin):
#     '''
#     问卷信息
#     '''
#     list_display = ('id', 'openid', 'dia', 'result', 'yzk', 'photoOD', 'photoOS', 'ctime', 'uptime')
#     list_display_links = ('id',)
#     # 设置过滤选项
#     list_filter = ('id',)
#     # 设置可编辑字段 如果设置了可以编辑字段，页面会自动增加保存按钮
#     # list_editable = ('dia',)
#     # 按id升序排序
#     ordering = ('id',)
#
#     save_as_continue = False # 修改完成之后跳转到元素列表页面
#     # 重写方法屏蔽按钮
#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         extra_context = extra_context or {}
#         extra_context['show_save_and_add_another'] = False
#         extra_context['show_save_and_continue'] = False
#         return super(Info, self).change_view(request, object_id,
#             form_url, extra_context=extra_context)