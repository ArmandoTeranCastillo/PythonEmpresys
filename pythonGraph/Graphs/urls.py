from rest_framework import routers
from .viewsets import *
#CONTROLADOR
#Esta clase nos permite definir las URLs 
#GET, PUT, POST, UPDATE, DELETE, etc
#Esto nos facilita interactuar con las APIs
router = routers.SimpleRouter()
router.register('graph', graphViewSet)
router.register('x_axis_labels', x_axis_label_ViewSet)
router.register('y_axis_labels', y_axis_label_ViewSet)
router.register('year', yearViewSet)
router.register('entity', entityViewSet)
router.register('census', censusViewSet)
urlpatterns = router.urls
