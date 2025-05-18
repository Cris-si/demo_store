# Django电商平台

这是一个基于Django框架开发的现代电商平台。(大作业）

## 功能特点

- 用户认证和授权系统
- 商品管理和展示
- 购物车功能
- 订单管理系统
- 在线支付集成
- 商品分类和搜索
- 用户评价系统

## 安装说明

1. 克隆项目到本地
```bash
git clone [项目地址]
```

2. 创建并激活虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 执行数据库迁移
```bash
python manage.py migrate
```

5. 创建超级用户
```bash
python manage.py createsuperuser
```

6. 运行开发服务器
```bash
python manage.py runserver
```

## 技术栈

- Django 5.0.2
- Django REST Framework
- SQLite (开发) / PostgreSQL (生产)
- Bootstrap 5
- JavaScript/jQuery

## 环境要求

- Python 3.8+
- pip 
