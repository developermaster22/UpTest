<h1 style="color:white">🛠️ Inventario Web con Django + PostgreSQL 🐘</h1>

¡Bienvenido a tu sistema de gestión de productos con características personalizadas!  
Con este proyecto podrás agregar productos, asignarles características dinámicamente y gestionar todo desde una interfaz simple, funcional y atractiva. 🚀

<div align="center">
  <img src="https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif" width="400"/>
</div>

---

<h2 style="color:white">🧰 Tecnologías Utilizadas</h2>

- 🐍 Python 3.10+  
- 🌐 Django 4.x  
- 🐘 PostgreSQL  
- 🎨 HTML + CSS (Bootstrap)  
- ⚙️ JavaScript (para características dinámicas)  
- 🐳 Docker (opcional, recomendado)  

---

<h2 style="color:white">📦 Instalación Paso a Paso</h2>

> Si quieres correr este proyecto en tu máquina local, sigue estas instrucciones. ¡Es muy fácil!

<h3 style="color:white">1. 🔁 Clona el repositorio</h3>

```bash
git clone https://github.com/developermaster22/inventario-django.git
cd inventario-django

<h3 style="color:white">2. 🐍 Crea un entorno virtual</h3>
python -m venv env
source env/bin/activate  # En Linux/Mac
env\Scripts\activate     # En Windows

<h3 style="color:white">3. 🧪 Instala las dependencias</h3>
pip install -r requirements.txt

<h3 style="color:white">4. 🐘 Configura tu base de datos PostgreSQL</h3>
Crea una base de datos en PostgreSQL y actualiza tu archivo .env (o settings.py) con estos datos:
DB_NAME=nombre_de_tu_db
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432

<h3 style="color:white">5. 🔧 Realiza las migraciones</h3>
python manage.py makemigrations
python manage.py migrate

<h3 style="color:white">6. 👤 Crea un superusuario (opcional)</h3>
python manage.py createsuperuser

<h3 style="color:white">7. 🚀 Ejecuta el servidor</h3>
python manage.py runserver
Luego entra a 👉 http://127.0.0.1:8000

<h2 style="color:white">💡 Características</h2>
✅ Agregar productos
✅ Añadir múltiples características por producto
✅ Edición de productos y características
✅ Alerta animada al guardar cambios (¡desaparece en 4 segundos!)
✅ Interfaz responsive y funcional
✅ Soporte para PostgreSQL
✅ Listado de productos con botones y colores llamativos

🐳<h2 style="color:white">🐳 Docker (opcional pero recomendado)</h2> <h3 style="color:white">1. 🐳 Construye y levanta los contenedores</h3>
docker-compose up --build

<h3 style="color:white">2. 💾 Accede a la app</h3>
http://localhost:8000

🎯 Usa este comando si necesitas ejecutar migraciones dentro del contenedor:
docker-compose exec web python manage.py migrate

<h2 style="color:white">🖼️ Vista previa del proyecto</h2> <div align="center"> <img
¡Así se ve tu app!

<div align="center"> <img src="https://media.giphy.com/media/l0MYJzQWqF3TDsVWU/giphy.gif" width="600"/> </div>

<h2 style="color:white">🙌 Contribuciones</h2>
¿Quieres mejorar esta app? ¡Eres más que bienvenido!
Haz un fork, crea tu rama y envía un PR 💪
git checkout -b nueva-funcionalidad
git commit -m "Agrego nueva funcionalidad"
git push origin nueva-funcionalidad
<h2 style="color:white">📬 Contacto</h2>
📧 cesarlinares1522@gmail.com
🐙 GitHub: @developermaster22



