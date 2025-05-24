from django import template
import re

register = template.Library()

@register.filter(name='format_image_name')
def format_image_name(value):
    """将产品名称转换为图片文件名格式"""
    if not value:
        return ''
    # 转换为小写
    value = str(value).lower()
    # 替换空格为连字符
    value = re.sub(r'\s+', '-', value)
    # 移除特殊字符
    value = re.sub(r'[^a-z0-9-]', '', value)
    return value 