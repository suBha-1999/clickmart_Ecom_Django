from django.urls import path
# here we'll going to separate views based on apps
from users import views as UserViews
from products import views as ProductViews
from carts import views as CartViews
#  ------------------- for token / login----------------
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
# ----------------for Order ----------------------------
from orders import views as OrderViews


urlpatterns = [
    path('register/', UserViews.RegisterView.as_view(), name='Register'),

    # for login we'll use token (access token/ refresh token) ------> for that neeed to install #simplejwt
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #-----access tokens-------
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #----refresh tokens------


    path('profile/', UserViews.ProfileView.as_view()),

    # ---------------------Category API-----------------
    path('categories/', ProductViews.CategoryListViews.as_view(), name='CategoryList'),

    # ---------------------Product API------------------
    path('products/', ProductViews.ProductListViews.as_view(), name='ProductList'),
    path('products/<int:pk>/', ProductViews.ProductDetailsView.as_view(), name='ProductDetails'),

    # --------------------Cart API -------------------------
    path('carts/', CartViews.CartListView.as_view(), name='CartListViews'),

    # --------------------- Add to Cart --------------------
    path('cart/add/', CartViews.AddToCart.as_view(), name='AddToCart'),

    # --------------------- Manage -----------------------
    path('cart/items/<int:item_id>', CartViews.ManageCartItemView.as_view(), name='ManageCartItem'),


    # -------------------- Order --------------------------
    path('order/place/',OrderViews.PlaceOrderViews.as_view(), name='OrderViews'),

    # -------------------- Orders History -----------------
    path('orders/', OrderViews.myOrdersView.as_view(), name='myOrdersview'),
    path('orders/<int:pk>/', OrderViews.OrderDetailView.as_view(), name='OrderDetailView')

]