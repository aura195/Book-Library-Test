"""
URL configuration for Library Management System.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.http import HttpResponse

def home_view(request):
    """Simple home view that provides links to the admin and API."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Library Management System</title>
        <style>
            body { 
                font-family: 'Inter', Arial, sans-serif; 
                margin: 40px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                min-height: 100vh;
            }
            .container { 
                max-width: 800px; 
                margin: 0 auto; 
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 20px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            .card { 
                border: 1px solid rgba(255, 255, 255, 0.2); 
                padding: 20px; 
                margin: 20px 0; 
                border-radius: 12px;
                background: rgba(255, 255, 255, 0.05);
            }
            .btn { 
                display: inline-block; 
                padding: 12px 24px; 
                background: rgba(255, 255, 255, 0.2); 
                color: white; 
                text-decoration: none; 
                border-radius: 8px; 
                margin: 8px; 
                transition: all 0.3s ease;
                border: 1px solid rgba(255, 255, 255, 0.3);
            }
            .btn:hover { 
                background: rgba(255, 255, 255, 0.3); 
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            }
            .api-info { 
                background: rgba(255, 255, 255, 0.1); 
                padding: 15px; 
                border-radius: 8px; 
                margin: 10px 0;
            }
            h1 { text-align: center; margin-bottom: 30px; font-size: 2.5em; }
            h2 { color: #fbbf24; margin-bottom: 15px; }
            code { 
                background: rgba(0, 0, 0, 0.3); 
                padding: 4px 8px; 
                border-radius: 4px; 
                font-family: 'Monaco', monospace;
            }
            a { color: #fbbf24; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📚 Library Management System</h1>
            <p style="text-align: center; font-size: 1.2em; margin-bottom: 30px;">
                Welcome to the Django admin to DRF + Vue.js migration project!
            </p>
            
            <div class="card">
                <h2>🔗 Quick Links</h2>
                <div style="text-align: center;">
                    <a href="/admin/" class="btn">Django Admin</a>
                    <a href="/api/" class="btn">API Root</a>
                    <a href="http://localhost:3000" class="btn">Vue.js Frontend</a>
                </div>
            </div>
            
            <div class="card">
                <h2>📊 API Endpoints</h2>
                <div class="api-info">
                    <p><strong>Book Loans:</strong> <a href="/api/book-loans/">/api/book-loans/</a></p>
                    <p><strong>Students:</strong> <a href="/api/students/">/api/students/</a></p>
                    <p><strong>Books:</strong> <a href="/api/books/">/api/books/</a></p>
                    <p><strong>Statistics:</strong> <a href="/api/book-loans/statistics/">/api/book-loans/statistics/</a></p>
                    <p><strong>Overdue Loans:</strong> <a href="/api/book-loans/overdue_loans/">/api/book-loans/overdue_loans/</a></p>
                </div>
            </div>
            
            <div class="card">
                <h2>🧪 Testing</h2>
                <p>To test the API without authentication, use the test settings:</p>
                <code>DJANGO_SETTINGS_MODULE=config.settings.test python3 manage.py runserver 8001</code>
                <br><br>
                <p>Then access: <a href="http://localhost:8001/api/book-loans/">http://localhost:8001/api/book-loans/</a></p>
            </div>
            
            <div class="card">
                <h2>🚀 Development</h2>
                <p>This project uses a professional structure with:</p>
                <ul>
                    <li>✅ Python virtual environment</li>
                    <li>✅ Modular Django apps</li>
                    <li>✅ Environment-specific settings</li>
                    <li>✅ Comprehensive testing</li>
                    <li>✅ Beautiful Vue.js frontend with Tailwind CSS</li>
                    <li>✅ Docker support</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
    path('api/', include('apps.library.urls')),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug toolbar URLs
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
