from rest_framework import routers
from .viewsets import graphViewSet, censusViewSet


#Esta clase nos permite definir las URLs 
#GET, PUT, POST, UPDATE, DELETE, etc
#Esto nos facilita crear APIs
router = routers.SimpleRouter()
router.register('graph', graphViewSet)
router.register('censuspoblation', censusViewSet)
urlpatterns = router.urls
