select @@VERSION;

--Creamos la base de datos
create database Relevamiento;
--Seleccionamos la base de datos a usar	
use Relevamiento;

-- CREAR un esquema dentro de la base de datos
create schema computadoras;


--create table Terminal.Omnibus.controll(
--nroControl int primary key identity (1,1) not null,
--codES int NOT NULL,
--patente varchar  NOT NULL,
--fecha date NOT NULL, --date	YYYY-MM-DD
--hora varchar(4) NOT NULL,
--dniChofer int	NOT NULL,
--codLoc int NOT NULL,
--cantPasajeros int NOT NULL,
--);

create table Relevamiento.computadoras.pc_Farmacias(
	nombre varchar(255) NOT NULL,
	ip varchar(255) not null,
	arquitectura_so varchar(255) not null,
	tipo_maquina varchar(255) not null,
	procesador varchar(255) not null,
	cores_fisicos int,
	cores_totales int,
	ram_tot varchar(255) not null,
	ram_usada varchar(255) not null,
	ram_disponible varchar(255) not null,
	espacio_tot_C varchar(255) not null,
	espacio_usado_C varchar(255) not null,
	espacio_disponible_C varchar(255) not null,
	espacio_tot_D varchar(255) not null,
	espacio_usado_D varchar(255) not null,
	espacio_disponible_D varchar(255) not null,
	anydesk varchar(255) not null,
	id_anydesk varchar(255) not null,
	CONSTRAINT PK_nombre_ip primary key (nombre, ip)
	);


create table Relevamiento.computadoras.farmacia(
	idFarmacia varchar(255) primary key not null,
	nombreFcia varchar(255) not null,
	direccion varchar(255) not null

	);

create table Relevamiento.computadoras.pc_almacenamiento(
	nombre varchar(255) primary key not null,
	info_txt varchar(255) not null,
);
