
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
    Trust int,
	primary key (NPCID));

insert into Room values (1, "guestbed"), (2, "groundskeeperslair"), (3, "corridor"),
			(4, "maidchamber"), (5, "butler"), (6, "kitchen"), (7, "stairs"), (8, "ballroom"),
            (9, "bathroom"), (10, "masterbedroom"), (11, "study"), (12, "attic");

insert into Player values (1, 1);
insert into NPC values (1, "groudskeeper", 1), (2, "maid", 1), (3, "chef", 1), (4, "jeeves", 1), (5, "mistress", 1);
insert into Item values (1, "whiskey", null, 6), (2, "torn page", null, 1), (3, "safe", null, 11), (4, "combination", null, 10), (5, "dark spellbook", null, 11)

