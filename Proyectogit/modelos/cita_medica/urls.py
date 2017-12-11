from django.conf.urls import url, include
from modelos.cita_medica.views import solicitud, CitaCreate

# #CRUD por funciones 
# urlpatterns = [ 
#     url(r'^inicio$', index, name='inicio'),
#     url(r'^nuevo$', usuario_view, name='crear_usuario'),
#     url(r'^listar$', usuario_list, name='listar_usuario'),
#     url(r'^editar/(?P<id_usuario>\d+)/$', usuario_edit, name='editar_usuario'),
#     url(r'^eliminar/(?P<id_usuario>\d+)/$', usuario_delete, name='eliminar_usuario'),
# ]

#CRUD por clases
# urlpatterns = [ 
#     url(r'^inicio$', index, name='inicio'),
#     url(r'^nuevo$', UsuarioCreate.as_view(), name='crear_usuario'),
#     url(r'^listar$', UsuarioList.as_view(), name='listar_usuario'),
#     url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='editar_usuario'),
#     url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='eliminar_usuario'),


urlpatterns = [ 
     url(r'^solicitud$', solicitud, name='solicitud'),
     url(r'^nuevo$', CitaCreate.as_view(), name='crearcita'),
#     url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='editar_usuario'),
#     url(r'^listar$', UsuarioList.as_view(), name='listar_usuario'),
#     url(r'^nuevo_usuario$', UsuarioCreate.as_view(), name='crear_usuario'),
#     url(r'^validar/(?P<id_usuario>\d+)/$', validar, name='validarform'),
]