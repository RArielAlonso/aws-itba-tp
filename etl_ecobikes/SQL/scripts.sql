drop schema if exists eco_bikes CASCADE;

create schema eco_bikes;

drop table if exists eco_bikes.station_info;

CREATE TABLE eco_bikes."station_info" (
"station_id" INTEGER,
  "name" TEXT,
  "physical_configuration" TEXT,
  "lat" REAL,
  "lon" REAL,
  "altitude" REAL,
  "address" TEXT,
  "post_code" TEXT,
  "capacity" INTEGER,
  "is_charging_station" BOOLEAN,
  "rental_methods" TEXT,
  "groups" TEXT,
  "obcn" TEXT,
  "nearby_distance" REAL,
  "_ride_code_support" BOOLEAN,
  "cross_street" text,
  "reload_id" integer
 );


drop table if exists eco_bikes.station_status;

CREATE TABLE eco_bikes."station_status" (
"station_id" INTEGER not NULL,
  "num_bikes_available" INTEGER,
  "num_bikes_disabled" INTEGER,
  "num_docks_available" INTEGER,
  "num_docks_disabled" INTEGER,
  "last_reported" REAL,
  "is_charging_station" BOOLEAN,
  "status" TEXT,
  "is_installed" INTEGER,
  "is_renting" INTEGER,
  "is_returning" INTEGER,
  "traffic" TEXT,
  "num_bikes_available_types.mechanical" INTEGER,
  "num_bikes_available_types.ebike" INTEGER,
  "reload_id" integer  
 );

drop table if exists eco_bikes.general_info;

CREATE TABLE "eco_bikes"."general_info" (
  "system_id" TEXT,
  "language" TEXT,
  "name" TEXT,
  "timezone" TEXT,
  "build_version" TEXT,
  "build_label" TEXT,
  "build_hash" TEXT,
  "build_number" TEXT,
  "mobile_head_version" TEXT,
  "mobile_minimum_supported_version" TEXT,
  "_station_count" INTEGER,
  "_vehicle_count._mechanical_count" INTEGER,
  "_vehicle_count._ebike_count" INTEGER,
  "reload_id" integer
)


drop table if exists ecobikes.metadata_load;

create table eco_bikes.metadata_load 
(reload_id integer,
date_reload text
);


select * from eco_bikes.station_status ss 
where reload_id = (select max(reload_id) from eco_bikes.metadata_load )