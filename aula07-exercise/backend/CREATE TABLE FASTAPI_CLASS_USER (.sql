create table fastapi_class_user (
   username      varchar(30) not null,
   email         varchar(45) not null,
   password_hash varchar2(128) not null
)