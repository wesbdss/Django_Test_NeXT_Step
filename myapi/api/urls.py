from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'person',views.PersonList)
router.register(r'person_media',views.Person_mediaList)
router.register(r'person_type',views.Person_typeList)
router.register(r'person_media_type',views.Person_media_typeList)
router.register(r'person_audit',views.Person_auditList)

urlpatterns =[
    path('',include(router.urls))
]