from django.contrib import admin
from django.urls import path
from Programa import views
from django.conf.urls.static import static
from Sistema import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Página principal
    path('login/', views.login_view, name='login'),  # Pestaña de iniciar sesión
    path('logout/', views.logout_view, name='logout'),
    
    #ADMINISTRADOR
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('datos_productos_por_categoria/', views.datos_productos_por_categoria, name='datos_productos_por_categoria'),
    path('datos_inventario_por_almacen/', views.datos_inventario_por_almacen, name='datos_inventario_por_almacen'),
    path('obtener_ventas/', views.obtener_ventas, name='obtener_ventas'),
    
    #INVENTARIO
    path('registrar_inventario/', views.registrar_inventario, name='registrar_inventario'),
    path('administrador/producto/<str:serie>/', views.producto_detalle, name='producto_detalle'),
    
    #VENTA
    path('registrar/', views.registrar_venta, name='registrar_venta'),
    path('ventas/', views.listar_ventas, name='ventas'),
    path('actualizar/<int:venta_id>/', views.actualizar_venta, name='actualizar_venta'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    path('administrador/ventas/', views.ventas_grafico, name='ventas_grafico'),

    
    #CATEGORIA
    path('categorias/', views.listar_categorias, name='categorias'),
    path('categoria/nueva/', views.registrar_categoria, name='registrar_categoria'),
    path('categoria/editar/<int:categoria_id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('categoria/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    
    #PRODUCTOS
    path('productos/', views.listar_productos, name='productos'),
    path('producto/nuevo/', views.registrar_producto, name='registrar_producto'),
    path('producto/editar/<str:serie>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/eliminar/<str:serie>/', views.eliminar_producto, name='eliminar_producto'),
    
    #CLIENTE
    path('clientes/', views.listar_clientes, name='clientes'),
    path('clientes/nuevo/', views.registrar_cliente, name='registrar_cliente'),
    path('clientes/actualizar/<str:dni>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/eliminar/<str:dni>/', views.eliminar_cliente, name='eliminar_cliente'),
    
    #PROVEEDOR
    path('proveedores/', views.listar_proveedores, name='proveedores'),
    path('proveedores/eliminar/<str:ruc>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/actualizar/<str:ruc>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/nuevo/', views.registrar_proveedor, name='registrar_proveedor'),
    
    #USUARIOS
    path('usuarios/', views.listar_usuarios, name='usuarios'),
    path('usuarios/registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('usuarios/actualizar/<str:dni>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('usuarios/eliminar/<str:dni>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/detalle/<str:dni>/', views.detalles_usuario, name='usuario_detalle'),
    
    
    #VENDEDOR
    path('vendedor-dashboard/', views.vendedor_dashboard, name='vendedor_dashboard'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)