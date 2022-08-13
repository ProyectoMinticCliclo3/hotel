# Proyecto CICLO 3 NRC1872 - Grupo 05

## Plataforma de Reserva de Habitaciones de Hotel

Rose Rayhaan by Rotana requiere un sistema de reserva de habitaciones disponibles para sus clientes, en el cual los `usuarios` puedan ver las **_habitaciones disponibles_** y así poder **escoger** la que mejor se adapte a sus necesidades. Cabe destacar que **_todas las habitaciones son iguales y tienen las mismas características_**.

Los tipos de usuarios que debe manejar el sistema son `superadministrador`, `administrador`, y `usuario final`.

Un `usuario final`
de la plataforma debe estar en la capacidad de poder:

-[x] **registrarse**, -[x] **buscar** una habitación, -[x] **calificar** una habitación, -[ ] **realizar la reserva** por una _cantidad fija de días_ y -[ ] **gestionar sus comentarios** sobre las habitaciones.

Un `administrador` se encarga de:

-[x] **gestionar los usuarios finales** y de -[ ] **agregar habitaciones al sistema** para que el usuario final las pueda visualizar.

Un `superadministrador` ejerce el:

-[x] **control total de la plataforma (`usuarios` & `habitaciones`)**.

**_Los datos suministrados por los `usuarios` deben cumplir la _**política de privacidad de datos vigente**_._**

**_La plataforma debe ser desarrollada con el framework `Flask`._**

## Rúbricas Proyecto _Hotel_

| **PESO**     | **COMPONENTE A EVALUAR**                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Sprint 1** | **Planificación y diseño de la aplicación**                                                                         |
| 10.0%        | Definición de roles                                                                                                 |
| _10.0%_      | _Documento con la descripción de cada rol_                                                                          |
|              |                                                                                                                     |
| 45.0%        | Definición de artefactos                                                                                            |
| _20.0%_      | _Backlog del producto_                                                                                              |
| _20.0%_      | _Backlog por sprint_                                                                                                |
| _5.0%_       | _Asignación de backlogs a cada rol definido_                                                                        |
|              |                                                                                                                     |
| 25.0%        | Diagrama de clases                                                                                                  |
| 25.0%        | _Documento descriptivo de las clases más importantes_                                                               |
|              |                                                                                                                     |
| 20.0%        | Definición del cronograma                                                                                           |
| _20.0%_      | _Definir fechas para cada una de las actividades definidas_                                                         |
|              |                                                                                                                     |
| **Sprint 2** | **Desarrollo Front-End de la aplicación**                                                                           |
| 20.0%        | Mapa de navegabilidad                                                                                               |
| _20.0%_      | _Documento descriptivo del mapa de navegabilidad_                                                                   |
|              |                                                                                                                     |
| 40.0%        | Vistas de la aplicación                                                                                             |
| _35.0%_      | _Diseño e implementación preliminar de las vistas_                                                                  |
| _5.0%_       | _Documento con las imágenes de las vistas preliminares_                                                             |
|              |                                                                                                                     |
| 20.0%        | Estilos para las vistas                                                                                             |
| _20.0%_      | _Selección e implementación de los estilos para las vistas_                                                         |
|              |                                                                                                                     |
| 20.0%        | Creación del proyecto en GIT                                                                                        |
|              |                                                                                                                     |
| **Sprint 3** | **Desarrollo Back-End de la aplicación**                                                                            |
| 25.0%        | Diseño e implementación de los controladores para formularios y otras funcionalidades                               |
| _5.0%_       | _Especificación de ruta_                                                                                            |
| _5.0%_       | _Definición de métodos HTTP permitidos_                                                                             |
| _10.0%_      | _Lógica algorítmica_                                                                                                |
| _5.0%_       | _Documento descriptivo del diseño y la especificación de los controladores definidos_                               |
|              |                                                                                                                     |
| 25.0%        | Diseño e implementación de base de datos                                                                            |
| _10.0%_      | _Diseño de diagrama relacional_                                                                                     |
| _10.0%_      | _Diseño e implementación de las tablas de las bases de datos con SQLite_                                            |
| _5.0%_       | _Documento descriptivo de las tablas y las relaciones más importantes_                                              |
|              |                                                                                                                     |
| 30.0%        | Desarrollo de integración de controladores y bases de datos                                                         |
| _5.0%_       | _Validación de los datos de entrada_                                                                                |
| _10.0%_      | _Uso de librerías seguras (o prepared statements) para consultar/actualizar las bases de datos_                     |
| _10.0%_      | _Diseño de queries para consultar/actualizar las bases de datos_                                                    |
| _5.0%_       | _Documento descriptivo de las buenas prácticas de programación segura para fortalecer su aplicación_                |
|              |                                                                                                                     |
| 20.0%        | Diseño e implementación de portal de acceso usando método de autenticación basado en usuario y contraseña           |
| _10.0%_      | _Creación de sesiones_                                                                                              |
| _10.0%_      | _Uso de funciones hash criptográficas para almacenar contraseñas usando salts_                                      |
|              |                                                                                                                     |
| **Sprint 4** | **Despliegue de la aplicación**                                                                                     |
| 20.0%        | Definición de requerimientos para el despliegue de la aplicación                                                    |
| _20.0%_      | _Documento descriptivo de los requerimientos y el proceso de despliegue de la aplicación_                           |
|              |                                                                                                                     |
| 80.0%        | Configuración, despliegue y verificación del funcionamiento de la aplicación en una plataforma como servicio (PaaS) |
| _40.0%_      | _Despliegue de la aplicación en una PaaS (PythonAnywhere o Heroku)_                                                 |
| _10.0%_      | _Verificación de la conectividad al dominio web https://mi_dominio_                                                 |
| _30.0%_      | _Verificación del correcto funcionamiento de la aplicación_                                                         |
