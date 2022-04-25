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
	("SOG_RED", "State of Grace (Taylor's Version)", "Red (Taylor's Version)", "r1"),
	("R_RED", "Red (Taylor's Version)", "Red (Taylor's Version)", "r2"),
	("T_RED", "Treacherous (Taylor's Version)", "Red (Taylor's Version)", "r3"),
    ("IKYWT_RED", "I Knew You Were Trouble (Taylor's Version)", "Red (Taylor's Version)", "r4"),
    ("ATW_RED", "All Too Well (Taylor's Version)", "Red (Taylor's Version)", "r5"),
    ("22_RED", "22 (Taylor's Version)", "Red (Taylor's Version)", "r6"),
    ("IAD_RED", "I Almost Do (Taylor's Version)", "Red (Taylor's Version)", "r7"),
    ("WANEGBT_RED", "We Are Never Ever Getting Back Together (Taylor's Version)", "Red (Taylor's Version)", "r8"),
    ("SSS_RED", "Stay Stay Stay (Taylor's Version)", "Red (Taylor's Version)", "r9"),
    ("TLT_RED", "The Last Time (feat. Gary Lightbody of Snow Patrol) (Taylor's Version)", "Red (Taylor's Version)", "r10"),
    ("HG_RED", "Holy Groud (Taylor's Version)", "Red (Taylor's Version)", "r11"), 
    ("SBT_RED", "Sad Beautiful Tragic (Taylor's Version)", "Red (Taylor's Version)", "r12"),
    ("TLO_RED", "The Lucky One (Taylor's Version)", "Red (Taylor's Version)", "r13"),
    ("EHC_RED", "Everything Has Changed (feat. Ed Sheeran) (Taylor's Version)", "Red (Taylor's Version)", "r14"),
    ("S_RED", "Starlight (Taylor's Version)", "Red (Taylor's Version)", "r15"), 
    ("BA_RED", "Begin Again (Taylor's Version)", "Red (Taylor's Version)", "r16"),
    ("TMIK_RED", "The Moment I Knew (Taylor's Version)", "Red (Taylor's Version)", "r17"),
    ("CBBH_RED", "Come Back...Be Here (Taylor's Version)", "Red (Taylor's Version)", "r18"),
    ("GAH_RED", "Girl At Home (Taylor's Version)", "Red (Taylor's Version)", "r19"),
    ("SOGAV_RED", "State of Grace (Acoustic Version) (Taylor's Version)", "Red (Taylor's Version)", "r20"),
    ("RO_RED", "Ronan (Taylor's Version)", "Red (Taylor's Version)", "r21"),
    ("BM_RED", "Better Man (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r22"),
    ("NN_RED", "Nothing New (feat. Phoebe Bridgers) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r23"),
    ("B_RED", "Babe (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r24"),
    ("MIAB_RED", "Message In A Bottle (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r25"),
    ("IBYTAM_RED", "I Bet You Think About Me (feat. Chris Stapleton) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r26"),
    ("FW_RED", "Forever Winter (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r27"),
    ("RU_RED", "Run (feat. Ed Sheeran) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r28"),
    ("TVFN_RED", "The Very First Night (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r29"),
    ("ATW10_RED", "All Too Well (10 Minute Version) (Taylor's Version) (From The Vault)", "Red (Taylor's Version)", "r30"),
    ("FEAR_F", "Fearless (Taylor's Version)", "Fearless (Taylor's Version)", "f1"),
    ("FIF_F", "Fifteen (Taylor's Version)", "Fearless (Taylor's Version)", "f2"), 
    ("LS_F", "Love Story (Taylor's Version)", "Fearless (Taylor's Version)", "f3"),
    ("HS_F", "Hey Stephen (Taylor's Version)", "Fearless (Taylor's Version)", "f4"), 
    ("WH_F", "White Horse (Taylor's Version)", "Fearless (Taylor's Version)", "f5"), 
    ("YBWM_F", "You Belong With Me (Taylor's Version)", "Fearless (Taylor's Version)", "f6"),
    ("B_F", "Breath (feat. Colbie Caillate) (Taylor's Version)", "Fearless (Taylor's Version)", "f7"),
    ("TMW_F", "Tell Me Why (Taylor's Version)", "Fearless (Taylor's Version)", "f8"), 
    ("YNS_F", "You're Not Sorry (Taylor's Version)", "Fearless (Taylor's Version)", "f9"), 
    ("TWILY_F", "They Way I Loved You (Taylor's Version)", "Fearless (Taylor's Version)", "f10"),
    ("FA_F", "Forever & Always (Taylor's Version)", "Fearless (Taylor's Version)", "f11"),
    ("TBD_F", "The Best Day (Taylor's Version)", "Fearless (Taylor's Version)", "f12"),
    ("C_F", "Change (Taylor's Version)", "Fearless (Taylor's Version)", "f13"), 
    ("JTF_F", "Jump Then Fall (Taylor's Version)", "Fearless (Taylor's Version)", "f14"),
    ("U_F", "Untouchable (Taylor's Version)", "Fearless (Taylor's Version)", "f15"),
    ("FAP_F", "Forever & Always (Piano Version) (Taylor's Version)", "Fearless (Taylor's Version)", "f16"), 
    ("CIWTR_F", "Come In With The Rain (Taylor's Version)", "Fearless (Taylor's Version)", "f17"),
    ("S_F", "Superstar (Taylor's Version)", "Fearless (Taylor's Version)", "f18"),
    ("TOSOTD_F", "The Other Side Of The Door (Taylor's Version)", "Fearless (Taylor's Version)", "f19"),
    ("TWAF_F", "Today Was A Fairytale (Taylor's Version)", "Fearless (Taylor's Version)", "f20"),
    ("YAOM_F", "You All Over Me (feat. Maren Morris) (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f21"),
    ("MPF_F", "Mr Perfectly Fine (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f22"),
    ("WWH_F", "We Were Happy (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f23"), 
    ("TW_F", "That's When (feat. Keith Urban) (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f24"), 
    ("DY_F", "Don't You (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f25"),
    ("BBB_F", "Bye Bye Baby (Taylor's Version) (From The Vault)", "Fearless (Taylor's Version)", "f26")
    ;
    
CREATE TABLE song_subject (
	SubjectID VARCHAR(10) NOT NULL,
    Subject_description VARCHAR(20),
    PRIMARY KEY (SubjectID)
	);
    
INSERT INTO song_subject (SubjectID, Subject_description) VALUES
("EX", "Ex partner"),
("CP", "Current partner"),
("ND", "Never dated but...") 
;

INSERT INTO song_subject (SubjectID, Subject_description) VALUES
("ME", "Me")
;

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


CREATE TABLE Key_words (
FK_SongID varchar(10) NOT NULL,
VibeID VARCHAR(10),
SubjectID VARCHAR (10),
FOREIGN KEY (FK_SongID) REFERENCES master_song_list (PK_SongID),
FOREIGN KEY (VibeID) REFERENCES Vibe (VibeID),
FOREIGN KEY (SubjectID) REFERENCES song_subject (SubjectID)
);

INSERT INTO Key_words (FK_SongID, VibeID, SubjectID) VALUES
("r1", "P", "CP"),
("r2", "IC", "EX"),
("r2", "P", "EX"),
("r3", "P", "ND"),
("r3", "P", "CP"),
("r4", "N", "EX"),
("r4", "N", "ND"),
("r5", "IC", "EX"),
("r5", "N", "EX"),
("r6", "P", "ME"),
("r7", "IC", "EX"),
("r7", "IC", "ND"),
("r8", "N", "EX"),
("r9", "P", "CP"),
("r10", "N", "CP"),
("r10", "N", "ND"),
("r10", "N", "EX"),
("r10", "IC", "EX"),
("r10", "IC", "ND"),
("r11", "P", "CP"),
("r12", "IC", "EX"),
("r12", "P", "EX"),
("r12", "IC", "ND"),
("r12", "P", "ND"),
("r13", "P", "ND"),
("r14", "P", "CP"),
("r14", "P", "ND"),
("r15", "P", "EX"),
("r16", "P", "CP"),
("r16", "N", "EX"),
("r16", "N", "ND"),
("r17", "N", "CP"),
("r17", "N", "EX"),
("r18", "IC", "ND"),
("r18", "IC", "EX"),
("r19", "N", "ND"),
("r20", "P", "CP"),
("r21", NULL, NULL),
("r22", "N", "EX"),
("r22", "IC", "EX"),
("r23", NULL, "ME"),
("r24", "N", "EX"),
("r24", "N", "CP"),
("r25", "P", "ND"),
("r26", "N", "EX"),
("r26", "N", "ND"),
("r27", "IC", "CP"),
("r27", "IC", "EX"),
("r28", "P", "CP"),
("r29", "P", "EX"),
("r29", "IC", "ND"),
("r29", "IC", "EX"),
("r29", "P", "ND"),
("r30", "IC", "EX"),
("r30", "N", "EX"),
("f1", "P", "ND"),
("f1", "P", "CP"),
("f2", "N", "ME"),
("f2", "N", "EX"),
("f3", "P", "CP"),
("f4", "P", "ND"),
("f5", "N", "EX"),
("f6", "P", "ND"),
("f7", "IC", "EX"),
("f8", "N", "EX"),
("f8", "N", "ND"),
("f8", "N", "CP"),
("f9", "N", "EX"),
("f9", "N", "CP"),
("f10", "IC", "EX"),
("f10", "IC", "CP"),
("f11", "N", "EX"),
("f12", "P", "ME"),
("f13", "IC", "ME"),
("f13", "P", "ME"),
("f14", "P", "ND"),
("f15", "IC", "ND"),
("f15", "P", "ND"),
("f16", "N", "EX"),
("f17", "IC", "EX"),
("f17", "IC", "ND"),
("f18", "P", "ND"),
("f19", "IC", "CP"),
("f19", "IC", "EX"),
("f20", "P", "CP"),
("f20", "P", "ND"),
("f21", "N", "EX"),
("f21", "N", "ND"),
("f22", "N", "EX"),
("f23", "P", "EX"),
("f23", "IC", "EX"),
("f24", "P", "CP"),
("f25", "IC", "EX"),
("f26", "IC", "EX")
;
 
SELECT  m.PK_SongID, m.Title from master_song_list m 
INNER JOIN key_words k on m.PK_SongID=k.FK_SongID 
where k.vibeID  = "IC" and k.SubjectID = "EX"
ORDER BY RAND() LIMIT 8; 