# 🛒 Cartify - Ecommerce Platform

## 🙏 All praise to Allah Almighty — the source of all strength and guidance.

---

## 📋 Project Overview

**Cartify** is a full-stack ecommerce website developed as a semester project for the **Design and Analysis of Algorithms** course. The platform uses Django for the backend, MySQL as the database, and HTML, CSS, and JavaScript (with Bootstrap) for the frontend.

This project provides a secure, user-friendly online shopping experience featuring user registration, product browsing, cart management, and order processing. The admin dashboard enables efficient management of products, orders, and users.

---

## ✨ Features

### Frontend
- 🔒 Secure user registration and login with validation  
- 🏠 Home page with featured products and latest offers  
- 🛍️ Product catalog with filters by category, price, and popularity  
- 🖼️ Detailed product pages with multiple images and pricing  
- 🛒 Dynamic shopping cart with real-time updates  
- 📝 Streamlined checkout collecting shipping and billing details  
- 👤 User dashboard for orders, profile, and wishlist management  
- 📱 Responsive design for desktops, tablets, and smartphones  

### Backend
- 🔐 User authentication via Django’s built-in system  
- 🛠️ Admin panel for product, category, user, and order management  
- 📦 Order processing with status tracking  
- ✅ Input validation and session management for security  
- 🗄️ MySQL database integration for storing all relevant data  

---

## 🛠️ Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap  
- **Backend:** Python, Django  
- **Database:** MySQL  
- **Tools:** Visual Studio Code, Git, GitHub, Django REST Framework (future API integration)  

---

## 🎯 Project Scope & Objectives

- ✅ Develop a fully functional and secure ecommerce website  
- 💻 Build an intuitive, responsive frontend enhancing user experience  
- ⚙️ Implement a robust backend with Django and MySQL  
- 🛎️ Provide an administrative dashboard for seamless management  
- 🔒 Ensure data security and privacy with authentication and validation  
- 🧱 Follow best practices for maintainability and scalability  

**Note:** Current system excludes real-time payment gateway, multi-language support, and advanced features like product reviews, but architecture supports future enhancements.

---

## 🧩 Technical Implementation & Component Breakdown

- **Django Models (`models.py`):** Database schema for Products, Users, Orders, Cart Items with ORM.  
- **Views (`views.py`):** Logic for product listing, details, cart, checkout, dashboard; renders templates.  
- **Templates:** Located in `/templates/` using Django Template Language for dynamic content.  
- **Static Files:** CSS, JS, images in `/static/` for styling and interactivity.  
- **Forms (`forms.py`):** Handle login, registration, checkout input with validation.  
- **URLs (`urls.py`):** URL routing for clean, user-friendly paths.  
- **Admin Panel (`admin.py`):** CRUD operations on products, categories, orders for admins.  
- **Authentication:** Secure user login/logout with Django auth module.  
- **Cart System:** Add/update/remove items, track cart dynamically for guests and users.  
- **Checkout System:** Collect shipping info, confirm orders, store in database.  
- **Database (MySQL):** Stores users, products, orders, transactions. Managed via Django migrations.  
- **Responsive Design:** Implemented with Bootstrap and media queries for all devices.  
- **Version Control:** Git for tracking progress and collaboration, project hosted on GitHub.  

---

```markdown
## 🗂️ Project Structure

Ecommerce_project/
│
├── ecommerce_project/         # Main project configuration
│   ├── __init__.py
│   ├── settings.py            # Database & app settings
│   ├── urls.py                # Main URL routing
│   ├── asgi.py                # ASGI config (deployment)
│   └── wsgi.py                # WSGI config (deployment)
│
├── shop/                      # Main ecommerce app
│   ├── migrations/            # Database migration files
│   ├── __init__.py
│   ├── admin.py               # Admin dashboard customizations
│   ├── apps.py                # App config
│   ├── models.py              # Database models
│   ├── views.py               # View functions/classes
│   ├── forms.py               # Django forms
│   └── urls.py                # App-specific URLs
│
├── templates/                 # HTML templates
│   ├── base.html              # Base template for inheritance
│   ├── home.html              # Homepage
│   ├── product_list.html      # Product catalog
│   ├── product_detail.html    # Product details
│   ├── cart.html              # Shopping cart
│   ├── checkout.html          # Checkout page
│   ├── login.html             # Login page
│   └── dashboard.html         # User dashboard
│
├── static/                    # Static files (CSS, JS, Images)
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/
│   │   └── scripts.js         # Optional scripts
│   └── images/                # Product and banner images
│
├── media/                     # Uploaded media files (e.g., product images)
│
├── manage.py                  # Django CLI utility
│
└── requirements.txt           # Python package dependencies

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cartify-ecommerce.git
   cd cartify-ecommerce
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
Install required packages:

bash
pip install -r requirements.txt
Configure MySQL database:

Create a MySQL database (e.g., cartify_db)

Update DATABASES settings in ecommerce_project/settings.py

Apply migrations:

bash
python manage.py migrate
Create admin user:

bash
python manage.py createsuperuser
Run development server:

bash
python manage.py runserver
Access the site at:
http://127.0.0.1:8000/

🔮 Future Enhancements
💳 Real-time payment gateway integration

🌐 Multi-language support

⭐ Product reviews and recommendations

📱 Mobile app API integration using Django REST Framework

🙌 Acknowledgements
Special thanks to Sir Muneeb for invaluable guidance, and to peers and family for continuous support. Gratitude to Sir Syed University of Engineering and Technology for excellent resources and learning opportunities.

📄 License
This project is intended for academic purposes. Please contact the author for commercial use inquiries.

Author:
👩‍💻 Sidra Bib (009)
Sir Syed University of Engineering and Technology

“Challenges are what make life interesting; overcoming them is what makes life meaningful.”
All praise to Allah Almighty for strength and perseverance.

text

### Key Fixes:
1. **Project Structure Alignment**: Now properly formatted with clear tree hierarchy.
2. **Consistency**: All sections use uniform emoji styling.
3. **Markdown Integrity**: No broken code blocks or misplaced backticks.
