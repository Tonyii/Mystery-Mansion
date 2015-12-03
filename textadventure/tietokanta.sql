

DROP database if exists MM;
create database MM;
use MM;

drop table if exists Room;
drop table if exists Player;
drop table if exists Item;
drop table if exists NPC;

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

create table Synocmd(
	Nimi varchar(20) not null,
	Synonyymi varchar(20) not null,
	primary key (Synonyymi));

create table SynoPerson(
	personID varchar(20) not null,
	Synonyymi varchar(20) not null,
	primary key (Synonyymi));

insert into Room values (1, "guestroom"), (2, "garage"), (3, "corridor"),
			(4, "maidroom"), (5, "office"), (6, "kitchen"), (7, "stairs"), (8, "ballroom"),
            (9, "bathroom"), (10, "master bedroom"), (11, "study"), (12, "attic"), (13, "inventory");

insert into Player values (1, 1);
insert into NPC values (1, "Groundskeeper Willy", 2, 1), (2, "Maid Penelope", 8, 1), (3, "Chef Gordon", 6, 1), (4, "Jeeves the Butler", 5, 1), (5, "Lady Sonya", 10, 1);
insert into Item values (1, "whiskey", null, 6), (2, "torn page", null, 4), (3, "safe", null, 11), (4, "combination", null, 10), (5, "dark spellbook", null, 12);

insert into Synocmd values ("go", "go"), ("go","move"), ("go","exit"),("go","walk"), ("go","travel"), ("go", "climb"), ("go", "crawl"), ("go", "run");
insert into Synocmd values ("talk", "talk"), ("talk", "ask"), ("talk", "interrogate"), ("talk", "interview"), ("talk", "speak"), ("talk", "tell");
insert into Synocmd values ("look", "look"),("look", "inspect"),("look","examine"),("look", "search"),("look", "investigate");
insert into Synocmd values ("take", "take"),("take","lift"), ("take","pick"), ("take","get"), ("take","grab");
insert into Synocmd values ("room","questroom"),("room","garage"),("room","corridor"),("room","maidroom"),("room","office"),("room","kitchen"),("room","stairs"),("room","ballroom"),("room","bathroom"),("room","bedroom"),("room","study"),("room","attic");
insert into Synocmd values ("person","butler"),("person","jeeves"),("person","jeeves the butler"),("person", "willy"),("person","groundskeeper"),("person","willie"),("person","maid"),("person","penelope"),("person","gordon"),("person","chef"),("person","sonya"),("person","lady"),("person","mistress");
insert into Synocmd values ("whiskey","whiskey"),("whiskey","bottle"),("whiskey","whisky"),("page","page"),("page","paper"),("book","book"),("book","spellbook"),("lord","chadwick"),("lord","corpse"),("bed","pillow"),("bookshelf","shelf"),("bookshelf","bookcase");

insert into SynoPerson values (4,"butler"),(4,"jeeves"),(4,"jeeves the butler"),(1, "willy"),(1,"groundskeeper"),(1,"willie"),(2,"maid"),(2,"penelope"),(3,"gordon"),(3,"chef"),(5,"sonya"),(5,"lady"),(5,"mistress");