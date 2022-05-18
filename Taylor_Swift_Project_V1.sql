
CREATE DATABASE taylor_swift_project;

USE taylor_swift_project;

CREATE TABLE master_song_list (
	PK_SongID VARCHAR(10) NOT NULL,
    Title VARCHAR(100) NOT NULL,
    Album VARCHAR(30) NOT NULL,
    Spotify_ID VARCHAR (200) NOT NULL,
    CONSTRAINT UNIQUE (Spotify_ID),
    PRIMARY KEY (PK_SongID)
    );
    
INSERT INTO master_song_list (Spotify_ID, Title, Album, PK_SongID) VALUES
	("spotify:track:6lzc0Al0zfZOIFsFvBS1ki", "State of Grace (Taylor's Version)", "Red (Taylor's Version)", "r1"),
	("spotify:track:4OAuvHryIVv4kMDNSLuPt6", "Red (Taylor's Version)", "Red (Taylor's Version)", "r2"),
	("spotify:track:3S7HNKPakdwNEBFIVTL6dZ", "Treacherous (Taylor's Version)", "Red (Taylor's Version)", "r3"),
    ("spotify:track:6AtZLIzUINvExIUy4QhdjP", "I Knew You Were Trouble (Taylor's Version)", "Red (Taylor's Version)", "r4"),
    ("spotify:track:3nsfB1vus2qaloUdcBZvDu", "All Too Well (Taylor's Version)", "Red (Taylor's Version)", "r5"),
    ("spotify:track:3yII7UwgLF6K5zW3xad3MP", "22 (Taylor's Version)", "Red (Taylor's Version)", "r6"),
    ("spotify:track:2r9CbjYgFhtAmcFv1cSquB", "I Almost Do (Taylor's Version)", "Red (Taylor's Version)", "r7"),
    ("spotify:track:5YqltLsjdqFtvqE7Nrysvs", "We Are Never Ever Getting Back Together (Taylor's Version)", "Red (Taylor's Version)", "r8"),
    ("spotify:track:7eQj6r5PIdYKEIZjucBMcq", "Stay Stay Stay (Taylor's Version)", "Red (Taylor's Version)", "r9"),
    ("spotify:track:0y6kdSRCVQhSsHSpWvTUm7", "The Last Time (feat. Gary Lightbody of Snow Patrol) (Taylor's Version)", "Red (Taylor's Version)", "r10"),
    ("spotify:track:7J4b3LVCIGO4CMBDFLPoP6", "Holy Ground (Taylor's Version)", "Red (Taylor's Version)", "r11"), 
    ("spotify:track:73qMN9bXy7MSPwwGfH3wQr", "Sad Beautiful Tragic (Taylor's Version)", "Red (Taylor's Version)", "r12"),
    ("spotify:track:4e5ayHsOLJNLTGfjau2mEw", "The Lucky One (Taylor's Version)", "Red (Taylor's Version)", "r13"),
    ("spotify:track:7qEUFOVcxRI19tbT68JcYK", "Everything Has Changed (feat. Ed Sheeran) (Taylor's Version)", "Red (Taylor's Version)", "r14"),
    ("spotify:track:7A2cNLRT0YJc1yjxHlKihs", "Starlight (Taylor's Version)", "Red (Taylor's Version)", "r15"), 
    ("spotify:track:05GsNucq8Bngd9fnd4fRa0", "Begin Again (Taylor's Version)", "Red (Taylor's Version)", "r16"),
    ("spotify:track:0NRHj8hDwwmSPaA41o379r", "The Moment I Knew (Taylor's Version)", "Red (Taylor's Version)", "r17"),
    ("spotify:track:4pNApnaUWAL2J4KO2eqokq", "Come Back...Be Here (Taylor's Version)", "Red (Taylor's Version)", "r18"),
    ("spotify:track:0DMVrlMUn01M0IcpDbwgu7", "Girl At Home (Taylor's Version)", "Red (Taylor's Version)", "r19"),
    ("spotify:track:5jAIouBES8LWMiriuNq170", "State of Grace (Acoustic Version) (Taylor's Version)", "Red (Taylor's Version)", "r20"),
    ("spotify:track:7nWui6jiMM2m9qFmET1Mtj", "Ronan (Taylor's Version)", "Red (Taylor's Version)", "r21"),
    ("spotify:track:4OmFmE0fzcMG6g0Y8p4eSD", "Better Man (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r22"),
    ("spotify:track:01K4zKU104LyJ8gMb7227B", "Nothing New (feat. Phoebe Bridgers) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r23"),
    ("spotify:track:0v4z1tuZvn6LGknom9Qx7d", "Babe (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r24"),
    ("spotify:track:3z6XUommYDWPHeFhmhhT6j", "Message In A Bottle (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r25"),
    ("spotify:track:4CkgMiMqZ5JzW9iYXSTMTL", "I Bet You Think About Me (feat. Chris Stapleton) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r26"),
    ("spotify:track:3oGVx9RBmiYGv5ZCecWLkx", "Forever Winter (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r27"),
    ("spotify:track:4IQkfUsrwXol38VV3U7t7T", "Run (feat. Ed Sheeran) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r28"),
    ("spotify:track:6pYNq0ZwpPVazKzsqpf0G8", "The Very First Night (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r29"),
    ("spotify:track:5enxwA8aAbwZbf5qCHORXi", "All Too Well (10 Minute Version) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r30"),
    ("spotify:track:77sMIMlNaSURUAXq5coCxE", "Fearless (Taylor's Version)", "Fearless (Taylor's Version)", "f1"),
    ("spotify:track:2nqio0SfWg6gh2eCtfuMa5", "Fifteen (Taylor's Version)", "Fearless (Taylor's Version)", "f2"), 
    ("spotify:track:6YvqWjhGD8mB5QXcbcUKtx", "Love Story (Taylor's Version)", "Fearless (Taylor's Version)", "f3"),
    ("spotify:track:550erGcdD9n6PnwxrvYqZT", "Hey Stephen (Taylor's Version)", "Fearless (Taylor's Version)", "f4"), 
    ("spotify:track:5YL553x8sHderRBDlm3NM3", "White Horse (Taylor's Version)", "Fearless (Taylor's Version)", "f5"), 
    ("spotify:track:1qrpoAMXodY6895hGKoUpA", "You Belong With Me (Taylor's Version)", "Fearless (Taylor's Version)", "f6"),
    ("spotify:track:7HC7R2D8WjXVcUHJyEGjRs", "Breath (feat. Colbie Caillate) (Taylor's Version)", "Fearless (Taylor's Version)", "f7"),
    ("spotify:track:0k0vFacOHNuArLWMiH60p7", "Tell Me Why (Taylor's Version)", "Fearless (Taylor's Version)", "f8"), 
    ("spotify:track:6iiAfo4wTA2CVC3Uwx9uh8", "You're Not Sorry (Taylor's Version)", "Fearless (Taylor's Version)", "f9"), 
    ("spotify:track:22bPsP2jCgbLUvh82U0Z3M", "They Way I Loved You (Taylor's Version)", "Fearless (Taylor's Version)", "f10"),
    ("spotify:track:1msEuwSBneBKpVCZQcFTsU", "Forever & Always (Taylor's Version)", "Fearless (Taylor's Version)", "f11"),
    ("spotify:track:6ON9UuIq49xXY9GPmHIYRp", "The Best Day (Taylor's Version)", "Fearless (Taylor's Version)", "f12"),
    ("spotify:track:3ExweHKZF9B752DPQByRVT", "Change (Taylor's Version)", "Fearless (Taylor's Version)", "f13"), 
    ("spotify:track:2m3ObD945KvpE5y9A1eUWm", "Jump Then Fall (Taylor's Version)", "Fearless (Taylor's Version)", "f14"),
    ("spotify:track:0tQ9vBYpldCuikPsbgOVKA", "Untouchable (Taylor's Version)", "Fearless (Taylor's Version)", "f15"),
    ("spotify:track:01QdEx6kFr78ZejhQtWR5m", "Forever & Always (Piano Version) (Taylor's Version)", "Fearless (Taylor's Version)", "f16"), 
    ("spotify:track:1n2wszmJyVkw6FHqyLnQsY", "Come In With The Rain (Taylor's Version)", "Fearless (Taylor's Version)", "f17"),
    ("spotify:track:51A8eKvvZz9uydvIZ7xRSV", "Superstar (Taylor's Version)", "Fearless (Taylor's Version)", "f18"),
    ("spotify:track:1cSFlSBdpT4F5vb1frQ231", "The Other Side Of The Door (Taylor's Version)", "Fearless (Taylor's Version)", "f19"),
    ("spotify:track:2JoJrsEV15OzbijS47lids", "Today Was A Fairytale (Taylor's Version)", "Fearless (Taylor's Version)", "f20"),
    ("spotify:track:4CHpVfAhuxNJ3ibExe6kxO", "You All Over Me (feat. Maren Morris) (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f21"),
    ("spotify:track:2CYVETnhM9aytqrazYYwrK", "Mr Perfectly Fine (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f22"),
    ("spotify:track:34V9RiEPe8MNdU32qJsJa1", "We Were Happy (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f23"), 
    ("spotify:track:7eResoqEJJAVTkQYSqvO3P", "That's When (feat. Keith Urban) (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f24"), 
    ("spotify:track:4uuEGH5SVuzkkSFjo2DEiY", "Don't You (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f25"),
    ("spotify:track:4qUijfYU8EoIWiY6oSyrgT", "Bye Bye Baby (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f26")
    ;
    
INSERT INTO master_song_list (Spotify_ID, Title, Album, PK_SongID) VALUES
("spotify:track:2gVhfX2Gy1T9kDuS9azrF7", "willow", "evermore (deluxe version)", "e1"),
("spotify:track:1gcyHQpBQ1lfXGdhZmWrHP", "champagne problems", "evermore (deluxe version)", "e2"),
("spotify:track:3Dby3p1m6IOZn2gIIqECgK", "gold rush", "evermore (deluxe version)", "e3"),
("spotify:track:6sQckd3Z8NPxVVKUnavY1F", "'tis the damn season", "evermore (deluxe version)", "e4"),
("spotify:track:6lCvK2AR2uOKkVFCVlAzzm", "tolerate it", "evermore (deluxe version)", "e5"), 
("spotify:track:6uwfVkaOM1mcMkFmSn35ix", "no body, no crime (feat. HAIM)", "evermore (deluxe version)", "e6"),
("spotify:track:55Vf4bimc1Rtfg0PAQRAo2", "happiness", "evermore (deluxe version)", "e7"),
("spotify:track:66tOfHVH3aUrscg8vExRV4", "dorothea", "evermore (deluxe version)", "e8"),
("spotify:track:2awNGIJHodfLZSClB3PYhz", "coney island (feat. The National)", "evermore (deluxe version)", "e9"),
("spotify:track:43Ykum9T72UOPhBN31grpN", "ivy", "evermore (deluxe version)", "e10"),
("spotify:track:52OkpDsU6MmPx1AwGOb6Ap", "cowboy like me", "evermore (deluxe version)", "e11"),
("spotify:track:5VYWxXUpxuxEmCqMLDqICo", "long story short", "evermore (deluxe version)", "e12"), 
("spotify:track:5uICWmZTLkpEVbK22PBP6e", "marjorie", "evermore (deluxe version)", "e13"), 
("spotify:track:6a8aUhYbaQBUI8PcJ5ZmQ6", "closure", "evermore (deluxe version)", "e14"),
("spotify:track:6Wlq9rqkxrqj5Kls4Kw14H", "evermore (feat. Bon Iver)", "evermore (deluxe version)", "e15"),
("spotify:track:3zwMVvkBe2qIKDObWgXw4N", "right where you left me - bonus track", "evermore (deluxe version)", "e16"),
("spotify:track:1kdWw77ZpYOkhxeuhzU1j6", "it's time to go - bonus track", "evermore (deluxe version)", "e17"),
("spotify:track:4pfrrhvplbJZAIsfosGWQP", "the 1", "folklore (deluxe version)", "fo1"), 
("spotify:track:0KRYCBwIpWYFNrXOmXbyUh", "cardigan", "folklore (deluxe version)", "fo2"),
("spotify:track:2olxzvoFI9IpxqFeUv7WOX", "the last great american dynasty", "folklore (deluxe version)", "fo3"),
("spotify:track:5S4aYQAJOwJMAamANWlICO", "exile (feat. Bon Iver)", "folklore (deluxe version)", "fo4"),
("spotify:track:5P2bHCDM2tsgIaYWsZMhu5", "my tears ricochet", "folklore (deluxe version)", "fo5"),
("spotify:track:2I8YAEA1VmCuP1wkJHMpTw", "mirrorball", "folklore (deluxe version)", "fo6"), 
("spotify:track:76mOLcXOjOEhyY4mMF1l3r", "seven", "folklore (deluxe version)", "fo7"),
("spotify:track:6nK2pIKFcRc5frrZKHgsiT", "august", "folklore (deluxe version)", "fo8"), 
("spotify:track:7cm50Lw03k6VvRauJtkyTj", "this is me trying", "folklore (deluxe version)", "fo9"),
("spotify:track:6DrLROM5MG9bxWHeEG5elq", "illicit affairs", "folklore (deluxe version)", "fo10"),
("spotify:track:2ehRU518I0hYqMGQnk4lDY", "invisible string", "folklore (deluxe version)", "fo11"),
("spotify:track:0RP1kqoSPkVXsKiQNhMKzV", "mad woman", "folklore (deluxe version)", "fo12"),
("spotify:track:1EXa37LpSvi3OQ9UYQ28rD", "epiphany", "folklore (deluxe version)", "fo13"), 
("spotify:track:3IhtE4fkytdrtEfV34UzkD", "betty", "folklore (deluxe version)", "fo14"),
("spotify:track:6JlI8Ay77m4nJvZTHvfT1J", "peace", "folklore (deluxe version)", "fo15"),
("spotify:track:0YeDG5HnKnG7jpArkzsSPa", "hoax", "folklore (deluxe version)", "fo16"),
("spotify:track:0eFQWVz0qIxDOvhLpZ40P7", "the lakes - bonus track", "folklore (deluxe version)", "fo17")
; 

select * from master_song_list;

CREATE TABLE song_subject (
	SubjectID VARCHAR(10) NOT NULL,
    Subject_description VARCHAR(20),
    PRIMARY KEY (SubjectID)
	);
    
INSERT INTO song_subject (SubjectID, Subject_description) VALUES
("EX", "Ex partner"),
("CP", "Current partner"),
("ND", "Never dated but..."),
("ME", "Me"),
("F", "Friend");

CREATE TABLE Vibe (
VibeID VARCHAR(10) NOT NULL,
Vibe_description VARCHAR(20),
    PRIMARY KEY (VibeID)
	);
  
INSERT INTO Vibe (VibeID, Vibe_description) VALUES
("P", "Possitive"),
("N", "Negative"),
("IC", "It's complicated")
;

CREATE TABLE time (
TimeID VARCHAR(10) NOT NULL,
Time_description VARCHAR(20),
    PRIMARY KEY (TimeID)
	);
    
INSERT INTO Time (TimeID, Time_description) VALUES
("L", "Long"),
("S", "Short")
;


CREATE TABLE Key_words (
FK_SongID varchar(10) NOT NULL,
VibeID VARCHAR(10),
SubjectID VARCHAR (10),
TimeID VARCHAR (10),
FOREIGN KEY (FK_SongID) REFERENCES master_song_list (PK_SongID),
FOREIGN KEY (VibeID) REFERENCES Vibe (VibeID),
FOREIGN KEY (SubjectID) REFERENCES song_subject (SubjectID),
FOREIGN KEY (TimeID) REFERENCES time (TimeID)
);

INSERT INTO Key_words (FK_SongID, VibeID, SubjectID, TimeID) VALUES
("r1", "P", "CP", "L"),
("r1", "P", "CP", "S"),
("r2", "IC", "EX", "L"),
("r2", "IC", "EX", "S"),
("r2", "P", "EX", "L"),
("r2", "P", "EX", "S"),
("r3", "P", "ND", "L"),
("r3", "P", "ND", "S"),
("r3", "P", "CP", "S"),
("r4", "N", "EX", "L"),
("r4", "N", "EX", "S"),
("r4", "N", "ND", "L"),
("r4", "N", "ND", "S"),
("r5", "IC", "EX", "L"),
("r5", "N", "EX", "L"),
("r6", "P", "ME", NULL),
("r6", "P", "F", NULL),
("r7", "IC", "EX", "L"),
("r7", "IC", "ND", "L"),
("r7", "IC", "EX", "S"),
("r8", "N", "EX", "L"),
("r9", "P", "CP", "L"),
("r10", "N", "CP", "L"),
("r10", "N", "ND", "L"),
("r10", "N", "EX", "L"),
("r10", "IC", "EX", "L"),
("r10", "IC", "ND", "L"),
("r11", "P", "CP", "L"),
("r11", "P", "EX", "L"),
("r11", "P", "EX", "S"),
("r12", "IC", "EX", "S"),
("r12", "P", "EX", "S"),
("r12", "IC", "ND", "S"),
("r12", "P", "ND", "S"),
("r13", "P", "F", "S"),
("r13", "P", "F", "L"),
("r14", "P", "CP", "S"),
("r14", "P", "ND", "S"),
("r15", "P", "EX", "S"),
("r15", "P", "EX", "L"),
("r16", "P", "CP", "S"),
("r16", "N", "EX", "L"),
("r16", "N", "EX", "S"),
("r16", "N", "ND", "L"),
("r16", "N", "ND", "S"),
("r17", "N", "CP", "L"),
("r17", "N", "EX", "L"),
("r17", "N", "CP", "S"),
("r17", "N", "EX", "S"),
("r18", "IC", "ND", "S"),
("r18", "IC", "EX", "S"),
("r19", "N", "ND", "S"),
("r20", "P", "CP", "L"),
("r20", "P", "CP", "S"),
("r21", NULL, NULL, NULL),
("r22", "N", "EX", "L"),
("r22", "IC", "EX", "L"),
("r22", "N", "EX", "S"),
("r22", "IC", "EX", "S"),
("r23", NULL, "ME", NULL),
("r24", "N", "EX", "L"),
("r24", "N", "CP", "L"),
("r25", "P", "ND", "S"),
("r26", "N", "EX", "L"),
("r26", "IC", "EX", "L"),
("r27", "IC", "CP", "L"),
("r27", "IC", "EX", "L"),
("r28", "P", "CP", "S"),
("r28", "P", "ND", "L"),
("r28", "P", "ND", "S"),
("r29", "P", "EX", "L"),
("r29", "IC", "ND", "L"),
("r29", "IC", "EX", "L"),
("r29", "P", "ND", "L"),
("r29", "P", "EX", "S"),
("r29", "IC", "ND", "S"),
("r29", "IC", "EX", "S"),
("r29", "P", "ND", "S"),
("r30", "IC", "EX", "L"),
("r30", "N", "EX", "L")
;

INSERT INTO Key_words (FK_SongID, VibeID, SubjectID, TimeID) VALUES
("f1", "P", "ND","S"),
("f1", "P", "CP","S"),
("f2", "N", "ME",NULL),
("f2", "N", "EX","S"),
("f2", NULL, "F",NULL),
("f3", "P", "CP","L"),
("f3", "P", "CP","S"),
("f4", "P", "ND","L"),
("f4", "P", "ND","S"),
("f5", "N", "EX","L"),
("f6", "P", "ND","L"),
("f7", "IC", "EX","L"),
("f8", "N", "EX","L"),
("f8", "N", "ND","L"),
("f8", "N", "CP","L"),
("f9", "N", "EX","L"),
("f9", "N", "CP","L"),
("f10", "IC", "EX","L"),
("f10", "IC", "CP","L"),
("f10", "IC", "EX","S"),
("f10", "IC", "CP","S"),
("f11", "N", "EX","L"),
("f12", "P", "F",NULL),
("f13", "P", "ME",NULL),
("f13", "P", "F",NULL),
("f14", "P", "ND","S"),
("f14", "P", "ND","L"),
("f14", "P", "CP","S"),
("f15", "IC", "ND","L"),
("f15", "P", "ND","L"),
("f16", "N", "EX","L"),
("f17", "IC", "EX","L"),
("f17", "IC", "ND","L"),
("f18", "P", "ND","S"),
("f18", "P", "ND","L"),
("f19", "IC", "CP","L"),
("f19", "IC", "EX","L"),
("f19", "IC", "CP","S"),
("f19", "IC", "EX","S"),
("f20", "P", "CP","S"),
("f20", "P", "ND","S"),
("f20", "P", "ND","L"),
("f21", "N", "EX","S"),
("f21", "N", "EX","L"),
("f21", "N", "ND","L"),
("f22", "N", "EX","L"),
("f22", "N", "EX","S"),
("f23", "P", "EX","L"),
("f23", "IC", "EX","L"),
("f24", "P", "CP","L"),
("f24", "P", "CP","S"),
("f25", "IC", "EX","L"),
("f25", "IC", "EX","S"),
("f26", "IC", "EX","L"),
("f26", "N", "CP","L")
;

INSERT INTO Key_words (FK_SongID, VibeID, SubjectID, TimeID) VALUES
("e1", "P", "CP","S"),
("e1", "P", "ND","S"),
("e2", "IC", "EX","L"),
("e3", "P", "ND","L"),
("e3", "IC", "ND","L"),
("e3", "P", "ND","S"),
("e3", "IC", "ND","S"),
("e4", "IC", "EX","L"),
("e4", "P", "EX","L"),
("e5", "N", "CP","L"),
("e5", "N", "CP","S"),
("e6", NULL, "F",NULL),
("e7", "IC", "EX","L"),
("e8", "P", "EX","L"),
("e8", "P", "ND","L"),
("e8", "P", "EX","S"),
("e8", "P", "ND","S"),
("e9", "IC", "EX","L"),
("e9", "N", "EX","L"),
("e10", "IC", "ND","S"),
("e10", "IC", "ND","L"),
("e11", "IC", "ND","S"),
("e11", "N", "ND","L"),
("e12", "P", "CP","L"),
("e13", NULL, NULL,NULL),
("e14", "N", "EX","L"),
("e14", "N", "EX","S"),
("e14", "N", "ND","L"),
("e15", "IC", "EX","L"),
("e15", "IC", "EX","S"),
("e16", "N", "EX","L"),
("e16", "N", "EX","S"),
("e16", "IC", "EX","L"),
("e17", "N", "CP","L"),
("e17", "N", "CP","S"),
("e17", "IC", "CP","L"),
("e17", "IC", "EX","L")
;

INSERT INTO Key_words (FK_SongID, VibeID, SubjectID, TimeID) VALUES
("fo1", "IC", "EX","L"),
("fo1", "IC", "EX","S"),
("fo1", "P", "EX","L"),
("fo1", "P", "EX","S"),
("fo2", "N", "EX","S"),
("fo2", "IC", "EX","S"),
("fo2", "N", "EX","L"),
("fo2", "IC", "EX","L"),
("fo3", "P", "ME",NULL),
("fo3", "P", "F",NULL),
("fo4", "N", "EX","L"),
("fo5", "N", "EX","L"),
("fo5", "N", "EX","S"),
("fo6", "IC", "ND","S"),
("fo6", NULL, "ME",NULL),
("fo7", NULL, "F",NULL),
("fo8", "N", "ND","L"),
("fo8", "IC", "ND","S"),
("fo8", "N", "ND","S"),
("fo9", "IC", "CP","L"),
("fo9", "IC", "CP","S"),
("fo9", NULL, "ME",NULL),
("fo10", "N", "ND","S"),
("fo10", "IC", "ND","S"),
("fo10", "N", "ND","L"),
("fo10", "IC", "ND","L"),
("fo11", "P", "CP","L"),
("fo12", NULL, "ME",NULL),
("fo12", "N", "EX","S"),
("fo12", "N", "ND","S"),
("fo12", "N", "EX","L"),
("fo12", "N", "ND","L"),
("fo13", NULL, "F",NULL),
("fo14", "P", "EX","S"),
("fo14", "IC", "EX","S"),
("fo15", "P", "CP","L"),
("fo15", "P", "F",NULL),
("fo16", "IC", "EX","S"),
("fo16", "N", "EX","S"),
("fo16", "N", "F",NULL),
("fo16", "IC", "EX","L"),
("fo16", "N", "EX","L"),
("fo17", "P", "CP","L"),
("fo17", NULL, "ME",NULL)
;


select * from key_words;

use taylor_swift_project;

 -- Beleow select statement returns  random 8 songs where subject = EX and Vibe = It's complicated. 
SELECT m.Title from master_song_list m 
INNER JOIN key_words k on m.PK_SongID=k.FK_SongID 
where k.vibeID  = "P" and k.SubjectID = "ND" and k.TimeID = "L"
ORDER BY RAND() LIMIT 8; 



