from django.urls import path
from MarketPlace import views

urlpatterns = [
    path("", views.inicio,name='Inicio'),
    path('vehiculos/', views.vehiculos,name='Vehiculos'),
    path('vehiculosApi/', views.vehiculosapi),
    path('categorias/', views.categorias,name='Categorias'),
    path('categoriasApi/', views.categoriasapi),
    path('vendedores/', views.vendedores,name='Vendedores'),
    path('vendedoresApi/', views.vendedoresapi),
    path('busquedaVehiculos/', views.buscarvehiculo,name='BuscarVehiculo'),
    path('busquedaCategorias/', views.buscarcategoria,name='BuscarCategoria'),
    path('busquedaVendedores/', views.buscarvendedor,name='BuscarVendedor'),
    path('buscar/', views.buscar),
    path('buscarc/', views.buscarc),
    path('buscarv/', views.buscarv),
    path('leerVehiculos/', views.leer_vehiculos), #CRUD de vehiculos
    path('crearVehiculo/', views.crear_vehiculo), #CRUD de vehiculos
    path('editarVehiculo/', views.editar_vehiculo), #CRUD de vehiculos
    path('eliminarVehiculo/', views.eliminar_vehiculo), #CRUD de vehiculos
    path('vehiculo/list/', views.VehiculoList.as_view(),name='List'),
    path('vehiculo/create/', views.VehiculoCreate.as_view(),name='New'),
    path('vehiculo/edit/<pk>', views.VehiculoEdit.as_view(),name='Edit'),
    path('vehiculo/detail/<pk>', views.VehiculoDetail.as_view(),name='Detail'),
    path('vehiculo/delete/<pk>', views.VehiculoDelete.as_view(),name='Delete'),
    path('leerCategorias/', views.leer_categorias), #CRUD de categorias
    path('crearCategoria/', views.crear_categoria), #CRUD de categorias
    path('editarCategoria/', views.editar_categoria), #CRUD de categorias
    path('eliminarCategoria/', views.eliminar_categoria), #CRUD de categorias
    path('categoria/listC/', views.CategoriaList.as_view(),name='ListC'),
    path('categoria/create/', views.CategoriaCreate.as_view(),name='NewC'),
    path('categoria/edit/<pk>', views.CategoriaEdit.as_view(),name='EditC'),
    path('categoria/detail/<pk>', views.CategoriaDetail.as_view(),name='DetailC'),
    path('categoria/delete/<pk>', views.CategoriaDelete.as_view(),name='DeleteC'),
    path('leerVendedores/', views.leer_vendedores), #CRUD de vendedores
    path('crearVendedor/', views.crear_vendedor), #CRUD de vendedores
    path('editarVendedor/', views.editar_vendedor), #CRUD de vendedores
    path('eliminarVendedor/', views.eliminar_vendedor), #CRUD de vendedores
    path('vendedor/listV/', views.VendedorList.as_view(),name='ListV'),
    path('vendedor/create/', views.VendedorCreate.as_view(),name='NewV'),
    path('vendedor/edit/<pk>', views.VendedorEdit.as_view(),name='EditV'),
    path('vendedor/detail/<pk>', views.VendedorDetail.as_view(),name='DetailV'),
    path('vendedor/delete/<pk>', views.VendedorDelete.as_view(),name='DeleteV')

]