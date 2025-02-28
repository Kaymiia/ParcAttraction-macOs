DROP TABLE IF EXISTS attraction;

CREATE TABLE attraction (
    attraction_id integer PRIMARY KEY ASC ,
    nom text not null,
    description text not null,
    difficulte integer,
    visible bool default true
);

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    users_id integer primary key ASC,
    name text not null,
    password text not null
);


DROP TABLE IF EXISTS critique;

CREATE TABLE critique (
    critique_id INTEGER PRIMARY KEY ASC,
    nom TEXT,
    prenom TEXT,
    crit TEXT NOT NULL,
    note INTEGER NOT NULL CHECK (note >= 1 AND note <= 5),
    attraction_id INTEGER NOT NULL,
    FOREIGN KEY (attraction_id) REFERENCES attraction(attraction_id) ON DELETE CASCADE
);

