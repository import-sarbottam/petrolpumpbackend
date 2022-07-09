from django.urls import path
from api import views

urlpatterns = [
    path("entry/", views.GetEntry.as_view()),
    path("entryshift/", views.GetShiftEntry.as_view()),
    path("party/", views.GetParty.as_view()),
    path('postentry/', views.EntryPost.as_view()),
    path('postparty/', views.PartyPost.as_view()),
    path('price/', views.GetPrices.as_view()),
    path('postprice/', views.PostUpdatePrice.as_view()),
    path('deleteparty/<str:pk>', views.DeleteParty.as_view()),
]
