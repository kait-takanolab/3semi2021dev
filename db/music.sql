CREATE TABLE music (
	id int PRIMARY KEY,
	uid int,
	file varchar(256),
	spectrogram varchar(256),

	FOREIGN KEY(uid) REFERENCES user(id)
);