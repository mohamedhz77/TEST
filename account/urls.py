from django.urls import path,include
from . import views

urlpatterns =[

   path('account/', include('django.contrib.auth.urls')),
   path('register/', views.register, name='register' ),
   path('account/update/', views.UpdateUser, name='update' ),
   path('users/',views.user_list, name='user_list'),
   path('users/<username>/',views.user_detail, name='user_detail'),
]
