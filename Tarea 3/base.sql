drop table miapp_desafio;
drop table miapp_desafiosestudiantes;
drop table miapp_estudiante;
drop table miapp_grupo;
drop table miapp_proyecto;
drop table miapp_ramo;


create table miapp_categoria
(id int auto_increment primary key, nombre varchar(45) not null
 , descripcion varchar(450) 
 );


create table miapp_usuario
(id integer auto_increment  primary key, nombre varchar(55) not null
 , direccion varchar(100)
 , telefono varchar(15)
 , correo varchar(254) 
 );


create table miapp_producto
(id integer auto_increment  primary key, nombre varchar(45) not null
 , precio int, descripcion varchar(450), disponibilidad boolean, categoria_id INT
, CONSTRAINT fk_categoria
    FOREIGN KEY (categoria_id)
    REFERENCES miapp_categoria(id)
);
 

create table miapp_carrito
(id integer auto_increment  primary key, producto_id int not null
 , cantidad int default 1, monto int default 0, usuario_id INT
, CONSTRAINT fk_producto
    FOREIGN KEY (producto_id)
    REFERENCES miapp_producto(id)
, CONSTRAINT fk_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES miapp_usuario(id)
);

create table miapp_detalleCompra
(id integer auto_increment  primary key, carrito_id int not null
 , fecha datetime not null, comentario varchar(450), evaluacionNota tinyint
, CONSTRAINT fk_carrito
    FOREIGN KEY (carrito_id)
    REFERENCES miapp_carrito(id)
);

