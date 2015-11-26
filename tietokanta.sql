
DROP database if exists MM;
create database MM;
use MM;

create table Room(
	RoomID int not null,
	Description varchar(1000),
	primary key(RoomID));

create table Player(
	PlayerID int not null,
	Location int,
	primary key (PlayerID),
	foreign key (location) references Room(RoomID));

create table Item(
	ItemID int not null,
	Description varchar(1000),
	Owner int,
	Location int,
	primary key (ItemID),
	foreign key (Owner) references Player(PlayerID),
	foreign key (Location) references Room(RoomID));

create table NPC(
	NPCID int not null,
	Description varchar(1000),
	Location int,
    Trust int,
	primary key (NPCID),
	foreign key (Location) references Room(RoomID));

insert into Room values (1, "Guestroom"), (2, "Garage"), (3, "Corridor"),
			(4, "Maidroom"), (5, "Office"), (6, "Kitchen"), (7, "Stairs"), (8, "Ballroom"),
            (9, "Bathroom"), (10, "Master bedroom"), (11, "Study"), (12, "Attic");

insert into Player values (1, 1);
insert into NPC values (1, "Groundskeeper Willy", 2, 1), (2, "Maid Penelope", 4, 1), (3, "Chef Gordon", 6, 1), (4, "Jeeves the Butler", 5, 1), (5, "Lady Sonya", 10, 1);
insert into Item values (1, "whiskey", null, 6), (2, "torn page", null, 1), (3, "safe", null, 11), (4, "combination", null, 10), (5, "dark spellbook", null, 11)

