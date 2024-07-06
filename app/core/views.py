# from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
# from app.core.forms import ProductForm, BrandForm, SupplierForm, CategoryForm
# from app.core.models import Product, Brand, Supplier, Category
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django .contrib.auth.models import User
# from django.contrib.auth import login, logout, authenticate
# from .forms import CustomUserCreationForm, CustomUserUpdateForm
# from django.contrib import messages
# from django.db.models import Q

# # PAGUINACION
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# # ----------------- Perfil -----------------
# def profile(request):
#     data = {"title1": "IC - Perfil",
#             "title2": "Perfil de Usuario"}
#     return render(request, 'core/profile.html', data)

# #  Actualizar perfil 
# def update_profile(request):
#     data = {"title1": "IC - Actualizar Perfil",
#             "title2": "Actualizar Perfil"}
#     if request.method == 'POST':
#         form = CustomUserUpdateForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '¡Tu perfil ha sido actualizado exitosamente!')
#             return redirect('profile')
#     else:
#         form = CustomUserUpdateForm(instance=request.user)
    
#     return render(request, 'core/update_profile.html', {'form': form, **data})

# # ----------------- Registro -----------------
# def signup(request):
#     data = {"title1": "IC - Registro",
#             "title2": "Registro de Usuarios"}

#     if request.method == "GET":
#         form = CustomUserCreationForm()
#         return render(request, "registration/signup.html", {"form": form, **data})
#     elif request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # login(request, user)
#             messages.success(
#                 request, '¡Registro exitoso! Por favor, inicia sesión.')
#             return redirect("signin")
#         else:
#             # Manejo de errores específicos
#             if form.errors:
#                 error_messages = []
#                 for field in form:
#                     for error in field.errors:
#                         error_messages.append(f"{field.label}: {error}")
#                 for error in form.non_field_errors():
#                     error_messages.append(error)
#                 data["errors"] = error_messages

#             return render(request, "registration/signup.html", {"form": form, **data})

# # ----------------- Cerrar Sesion -----------------
# def signout(request):
#     logout(request)
#     return redirect("core:home")

# # ----------------- Iniciar Sesion -----------------
# def signin(request):
#     data = {"title1": "IC - Inicio de Sesión",
#             "title2": "Inicio de Sesión"}

#     if request.method == "GET":
#         # Obtener mensajes de éxito de la cola de mensajes
#         success_messages = messages.get_messages(request)
#         return render(request, "registration/signin.html", {
#             "form": AuthenticationForm(),
#             "success_messages": success_messages,  # Pasar mensajes de éxito a la plantilla
#             **data
#         })
#     else:
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect("core:home")
#             else:
#                 return render(request, "registration/signin.html", {
#                     "form": form,
#                     "error": "El usuario o la contraseña son incorrectos",
#                     **data
#                 })
#         else:
#             return render(request, "registration/signin.html", {
#                 "form": form,
#                 **data
#             })

# # ----------------- Vistas de Home -----------------
# def home(request):
#     data = {"title1": "IC - Inicio",
#             "title2": "Iguanas Corporation"}
#     # Obtener el estado de autenticación del usuario
#     is_authenticated = request.user.is_authenticated
#     # Agregar el estado de autenticación al contexto
#     data["is_authenticated"] = is_authenticated
#     return render(request, 'core/home.html', data)

# # ----------------- Vistas de Productos -----------------
# def product_List(request):
#     data = {"title1": "IC - Productos", "title2": "Consulta de Productos"}
    
#     query = request.GET.get('q')
#     if query:
#         products_list = Product.objects.filter(Q(description__icontains=query) | Q(id__icontains=query))
#     else:
#         products_list = Product.objects.all()

#     paginator = Paginator(products_list, 5)  # Muestra 10 productos por página
#     page = request.GET.get('page')
#     try:
#         products = paginator.page(page)
#     except PageNotAnInteger:
#         products = paginator.page(1)
#     except EmptyPage:
#         products = paginator.page(paginator.num_pages)

#     data["products"] = products
#     return render(request, "core/products/list.html", data)

# def product_create(request):
#     data = {"title1": "IC - Crear Productos", "title2": "Ingreso De Productos"}

#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.user = request.user  # Asignar el usuario actual
#             product.save()  # Guardar el producto principal

#             # Guardar las relaciones ManyToMany (categorías)
#             form.save_m2m()

#             messages.success(request, f"Éxito al crear el producto {product.description}.")
#             return redirect("core:product_list")
#     else:
#         form = ProductForm()

#     # Si el formulario no es válido o es una solicitud GET, mostrar el formulario con los datos actuales
#     data["form"] = form
#     return render(request, "core/products/form.html", data)


# # Editar un producto
# def product_update(request, id):
#     data = {"title1": "IC - Actualizar Productos", "title2": "Edicion De Productos"}
#     product = Product.objects.get(pk=id)
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"Éxito al actualizar el producto {product.description}.")
#             return redirect("core:product_list")
#     else:
#         form = ProductForm(instance=product)
#     data["form"] = form
#     return render(request, "core/products/form.html", data)

# # Eliminar un producto
# def product_delete(request, id):
#     product = Product.objects.get(pk=id)
#     data = {"title1": "IC - Eliminar Productos",
#             "title2": "Eliminar Un Producto", "product": product}
#     if request.method == "POST":
#         product.delete()
#         messages.success(request, f"Éxito al eliminar el producto.")
#         return redirect("core:product_list")
#     return render(request, "core/delete.html", data)

# # ----------------- Vistas de Marcas -----------------
# def brand_List(request):
#     data = {"title1": "IC - Marcas", "title2": "Consulta de Marcas"}
#     brands = Brand.objects.all()
#     data["brands"] = brands
#     # Pasar los mensajes al contexto de la plantilla
#     data["messages"] = messages.get_messages(request)
#     return render(request, "core/brands/list.html", data)

# # Crear una marca
# def brand_create(request):
#     data = {"title1": "IC - Crear Marcas", "title2": "Ingreso de Marca"}
#     if request.method == "POST":
#         form = BrandForm(request.POST)
#         if form.is_valid():
#             # Asignar el usuario actual al campo user de la marca
#             brand = form.save(commit=False)
#             brand.user = request.user
#             brand.save()
#             # Agregar mensaje de éxito
#             messages.success(request, f"Éxito al crear la marca {brand.description}.")
#             return redirect("core:brand_list")
#     else:
#         form = BrandForm()
#     data["form"] = form
#     return render(request, "core/brands/form.html", data)

# # Editar una marca
# def brand_update(request, id):
#     data = {"title1": "IC - Editar Marcas", "title2": "Edicion De Marcas"}
#     brand = Brand.objects.get(pk=id)
#     if request.method == "POST":
#         form = BrandForm(request.POST, request.FILES, instance=brand)
#         if form.is_valid():
#             form.save()
#             # Agregar mensaje de éxito
#             messages.success(request, f"Éxito al actualizar la marca {brand.description}.")
#             return redirect("core:brand_list")
#     else:
#         form = BrandForm(instance=brand)

#     data["form"] = form
#     return render(request, "core/brands/form.html", data)

# # Eliminar una marca
# def brand_delete(request, id):
#     brand = Brand.objects.get(pk=id)
#     data = {"title1": "IC - Eliminar Marcas", "title2": "Eliminar Una Marca", "brand": brand}
#     if request.method == "POST":
#         brand.delete()
#         messages.success(request, f"Éxito al eliminar la marca.")
#         return redirect("core:brand_list")
#     return render(request, "core/delete.html", data)

# # ----------------- Vistas de Proveedores -----------------
# def supplier_List(request):
#     data = {"title1": "IC - Proveedores", "title2": "Consulta de Proveedores"}

#     query = request.GET.get('q')
#     if query:
#         suppliers_list = Supplier.objects.filter(
#             Q(name__icontains=query) | Q(id__icontains=query) | Q(ruc__icontains=query) | Q(address__icontains=query) | Q(phone__icontains=query)
#         )
#     else:
#         suppliers_list = Supplier.objects.all()

#     # Implementar la paginación
#     paginator = Paginator(suppliers_list, 5)  # 5 registros por página
#     page = request.GET.get('page')

#     try:
#         suppliers = paginator.page(page)
#     except PageNotAnInteger:
#         # Si la página no es un número entero, mostrar la primera página
#         suppliers = paginator.page(1)
#     except EmptyPage:
#         # Si la página está fuera del rango (por ejemplo, página 9999), mostrar la última página
#         suppliers = paginator.page(paginator.num_pages)

#     data["suppliers"] = suppliers
#     return render(request, "core/suppliers/list.html", data)

# # Crear un proveedor
# def supplier_create(request):
#     data = {"title1": "IC - Crear Proveedores", "title2": "Ingreso De Proveedores"}
#     if request.method == "POST":
#         form = SupplierForm(request.POST, request.FILES)  # Añadir request.FILES para manejar archivos
#         if form.is_valid():
#             supplier = form.save(commit=False)
#             supplier.user = request.user  # Asignar el usuario actual al proveedor
#             supplier.save()
#             messages.success(request, f"Éxito al crear al proveedor {supplier.name}.")
#             return redirect("core:supplier_list")
#     else:
#         form = SupplierForm()  # Mover esto aquí para que el formulario se cree en ambos casos

#     # Pasar el formulario al contexto de la plantilla en ambos casos
#     data["form"] = form
#     return render(request, "core/suppliers/form.html", data)

# # Editar un proveedor
# def supplier_update(request, id):
#     data = {"title1": "IC - Editar Proveedores", "title2": "Edicion De Proveedores"}
#     supplier = Supplier.objects.get(pk=id)
#     if request.method == "POST":
#         form = SupplierForm(request.POST, request.FILES, instance=supplier)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"Éxito al actualizar al proveedor {supplier.name}.")
#             return redirect("core:supplier_list")
#     else:
#         form = SupplierForm(instance=supplier)
#     data["form"] = form
#     return render(request, "core/suppliers/form.html", data)

# # Eliminar un proveedor
# def supplier_delete(request, id):
#     supplier = Supplier.objects.get(pk=id)
#     data = {"title1": "IC - Eliminar Proveedores",
#             "title2": "Eliminar Proveedor", "supplier": supplier}
#     if request.method == "POST":
#         supplier.delete()
#         messages.success(request, f"Éxito al eliminar al proveedor.")
#         return redirect("core:supplier_list")
#     return render(request, "core/delete.html", data)

# # ----------------- Vistas de Categorias -----------------
# def category_List(request):
#     data = {"title1": "IC - Categorías",
#             "title2": "Consulta de Categorías"}
#     categories = Category.objects.all()
#     data["categories"] = categories
#     return render(request, "core/categories/list.html", data)

# # Crear una categoria
# def category_create(request):
#     data = {"title1": "IC - Crear Categorías", "title2": "Ingreso De Categorías"}
#     if request.method == "POST":
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             category = form.save(commit=False)
#             category.user = request.user
#             category.save()
#             messages.success(request, f"Éxito al crear la categoría {category.description}.")
#             return redirect("core:category_list")  # Redirigir si el formulario es válido
#     else:
#         form = CategoryForm()  # Aquí el formulario se instancia sin errores personalizados
    
#     # Pasar el formulario al contexto de la plantilla en ambos casos
#     data["form"] = form
#     return render(request, "core/categories/form.html", data)

# # Editar una categoria
# def category_update(request, id):
#     data = {"title1": "IC - Actualizar Categorías", "title2": "Edicion De Categorias"}
#     category = Category.objects.get(pk=id)
#     if request.method == "POST":
#         form = CategoryForm(request.POST, request.FILES, instance=category)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f"Éxito al actualizar la categoría {category.description}.")
#             return redirect("core:category_list")
#     else:
#         form = CategoryForm(instance=category)
#     # Pasar el formulario al contexto de la plantilla en ambos casos
#     data["form"] = form
#     return render(request, "core/categories/form.html", data)

# # Eliminar una categoria
# def category_delete(request, id):
#     category = Category.objects.get(pk=id)
#     data = {"title1": "IC - Eliminar Categorías",
#             "title2": "Eliminar Una Categoría", "category": category}
#     if request.method == "POST":
#         category.delete()
#         messages.success(request, f"Éxito al eliminar la categoría.")
#         return redirect("core:category_list")
#     return render(request, "core/delete.html", data)
