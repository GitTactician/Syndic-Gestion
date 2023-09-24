from django.urls import path
from .views import (
    HabitantLoginView,
    SyndicLoginView,
    UserLogoutView,
    HabitantListCreateView,
    HabitantDetailView,
    SyndicListCreateView,
    SyndicDetailView,
    ResidenceListCreateView,
    ResidenceDetailView,
    ReglementListCreateView,
    ReglementDetailView,
)

urlpatterns = [
    # Login views
    path('habitant/login/', HabitantLoginView.as_view(), name='habitant-login'),
    path('syndic/login/', SyndicLoginView.as_view(), name='syndic-login'),

    # Logout view
    path('logout/', UserLogoutView.as_view(), name='user-logout'),

    # Habitant views
    path('habitant/', HabitantListCreateView.as_view(), name='habitant-list-create'),
    path('habitant/<int:pk>/', HabitantDetailView.as_view(), name='habitant-detail'),

    # Syndic views
    path('syndic/', SyndicListCreateView.as_view(), name='syndic-list-create'),
    path('syndic/<int:pk>/', SyndicDetailView.as_view(), name='syndic-detail'),

    # Residence views
    path('residence/', ResidenceListCreateView.as_view(), name='residence-list-create'),
    path('residence/<int:pk>/', ResidenceDetailView.as_view(), name='residence-detail'),

    # Reglement views
    path('reglement/', ReglementListCreateView.as_view(), name='reglement-list-create'),
    path('reglement/<int:pk>/', ReglementDetailView.as_view(), name='reglement-detail'),
]
