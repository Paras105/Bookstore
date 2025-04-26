# Bookstore Management System  

A full-featured Django bookstore with admin controls and user cart functionality.  

 Features  
- 📖 User registration/login  
- 🛒 Session-based shopping cart  
- 👩‍💼 Custom admin panel (no Django admin)  
- 📚 Book inventory management  
- 🐳 Docker-ready deployment  

 Setup  
```bash
# 1. Clone repository  
git clone https://github.com/Paras105/bookstore-system.git  

# 2. Install dependencies  
pip install -r requirements.txt  

# 3. Run migrations  
python manage.py migrate  

# 4. Create admin user  
python manage.py createsuperuser  

# 5. Start dev server  
python manage.py runserver  
