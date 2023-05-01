from rest_framework import routers
from infoApi.viewsets import InfoViewset

router = routers.DefaultRouter()
router.register('info', InfoViewset)
