# Storefront - Django E-commerce API

A Django REST API for an online store with products, shopping cart, and order management.

## Features

- Product catalog with images and reviews
- Shopping cart functionality
- User authentication with JWT
- Order management system
- Customer profiles
- Admin panel for store management

## Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API development
- **MySQL** - Database
- **JWT** - Authentication
- **Pillow** - Image handling
- **Celery** - Background tasks
- **Redis** - Caching

## Quick Start

1. **Clone the project**
   ```bash
   git clone <your-repo-url>
   cd storefront
   ```

2. **Install dependencies**
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Set up database**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

5. **Visit** `http://localhost:8000/admin` to access admin panel

## Main API Endpoints

### Authentication
- `POST /auth/users/` - Register new user
- `POST /auth/jwt/create/` - Login and get token

### Products
- `GET /store/products/` - List all products
- `GET /store/products/{id}/` - Get product details
- `POST /store/products/{id}/reviews/` - Add product review

### Shopping Cart
- `POST /store/carts/` - Create new cart
- `GET /store/carts/{id}/` - Get cart details
- `POST /store/carts/{id}/items/` - Add item to cart

### Orders
- `GET /store/orders/` - List your orders
- `POST /store/orders/` - Create order from cart

### Profile
- `GET /store/customers/me/` - Get your profile
- `PUT /store/customers/me/` - Update your profile

## Project Structure

```
storefront/
├── core/           # User management
├── store/          # Main store functionality
├── tags/           # Product tagging
├── playground/     # Testing area
└── manage.py       # Django management
```

## Models Overview

- **Product** - Store items with price, description, images
- **Collection** - Product categories
- **Cart & CartItem** - Shopping cart functionality
- **Order & OrderItem** - Purchase orders
- **Customer** - User profiles with membership levels
- **Review** - Product reviews

## Environment Setup

Create a `.env` file:
```
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=mysql://user:password@localhost/storefront
```

## Requirements

- Python 3.12+
- MySQL
- Redis (for caching)

## Testing

The project includes Django Silk for performance monitoring at `/silk/` and Locust for load testing.

## Notes

This is a learning project that demonstrates Django REST Framework concepts including:
- Custom user authentication
- API permissions and viewsets
- Database relationships
- Image upload handling
- Shopping cart logic

## License

MIT License