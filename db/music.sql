CREATE TABLE music{
	id int,
	uid int,
	file varchar(256),
	spectrogram varchar(256),

	FOREIGN KEY(uid)
}