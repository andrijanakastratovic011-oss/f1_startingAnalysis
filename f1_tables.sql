create table if not exists dimRace(
    raceId int PRIMARY KEY,
    year int,
    round int,
    name_x varchar(255), 
    date date, 
    time_races TIME,
    url_y VARCHAR(255),
    fp1_date date, fp1_time TIME,
    fp2_date date, fp2_time TIME,
    fp3_date date, fp3_time TIME,
    quali_date date, quali_time TIME,
    sprint_date date, sprint_time TIME);

create table if not exists dimDriver(
    driverId int PRIMARY KEY,
    driverRef varchar(255),
    number_drivers int, code varchar(255),
    forname varchar(255),
    surname varchar(255),
    dob date, 
    nationality varchar(255),
    url varchar(255));

create table if not exists dimStatus(
    statusId int PRIMARY KEY,
    
    tatus varchar(255));

create table if not exists dimDate (
    dateId int PRIMARY KEY, 
    date date, 
    year int, 
    month int, 
    day int);

create table IF NOT EXISTS dimConstructor(
    constructorId int PRIMARY KEY,
    constructorRef varchar(255),
    name varchar(255),
    nationality_constructor varchar(255),
    url_constructor varchar(255));

create table if not exists dimCircuit(
    circuitId int primary key,
    circuitRef varchar(255),
    name_y varchar(255),
    location varchar(255),
    country varchar(255),
    lat float, 
    lng float, 
    alt float, 
    url_y varchar(255));

create table if not exists dimDriverStandings(
    driverStandingsId int primary key,
    points_driverStandings float, 
    position_driverStandings int, 
    positionText_driverStandings varchar(255),
    wins int);

create table if not exists dimConstructorStandings(
    constructorStandingsId int primary key,
    points_constructorStandings float, 
    position_constructorStandings int, 
    positionText_constructorStandings varchar(255),
    wins_constructorstandings int);

create table if not exists Fact(
    resultId int primary key,
    raceId int, 
    driverId int, 
    constructorId int, 
    statusId int, 
    circuitId int, 
    driverStandingsId int, 
    constructorStandingsId int, 
    number int, 
    grid int, 
    position int, 
    positionText varchar(255),
    positionOrder int, 
    points float, 
    time time,
    milliseconds float, 
    laps int, 
    fastestLap int, 
    fastestLapTime interval, 
    fastestLapSpeed float, 
    rank int, 
    dateId int, 
    CONSTRAINT fk_race foreign key (raceId) REFERENCES dimRace(raceId),
    CONSTRAINT fk_driver foreign key (driverId) REFERENCES dimDriver(driverId),
    CONSTRAINT fk_constructor foreign key (constructorId) REFERENCES dimConstructor(constructorId),
    CONSTRAINT fk_status foreign key (statusId) REFERENCES dimStatus(statusId),
    CONSTRAINT fk_circuit foreign key (circuitId) REFERENCES dimCircuit(circuitId),
    CONSTRAINT fk_driverStandings foreign key (driverStandingsId) REFERENCES dimDriverStandings(driverStandingsId),
    CONSTRAINT fk_constructorStandings foreign key (constructorStandingsId) REFERENCES dimConstructorStandings(constructorStandingsId),
    CONSTRAINT fk_date foreign key (dateId) REFERENCES dimDate(dateId));

create table if not exists FactLap(
    raceId int, 
    driverId int, 
    lap int, 
    position_laptimes int, 
    time_laptimes time, 
    milliseconds_laptimes int, 
    primary key (raceId, driverId, lap), 
    CONSTRAINT fk_race_lap foreign key (raceId) REFERENCES dimRace(raceId),
     CONSTRAINT fk_driver_lap foreign key (driverId) REFERENCES dimDriver(driverId));

create table if not exists FactPitStops(
    raceId int, 
    driverId int, 
    stop int, 
    lap_pitstops int,
    time_pitstops time,
    duration interval, 
    milliseconds_pitstop int, 
    primary key (raceId, driverId, stop),
    CONSTRAINT fk_race_pitstops foreign key (raceId) REFERENCES dimRace(raceId),
    CONSTRAINT fk_driver_pitstops foreign key (driverId) REFERENCES dimDriver(driverId));

    alter table fact alter column fastestlaptime type time;
    alter table fact alter column milliseconds type int;
    alter table factpitstopst alter column duration type float;
    alter table fact alter column time type varchar(255);
    alter table FactLap alter column time_laptimes type varchar(255);
    alter table FactPitStops alter column time_pitstops type varchar(255);
    alter table FactLap alter column time_laptimes type varchar(255);
    alter table dimRace alter column fp1_time type varchar(255);
    alter table dimRace alter column fp2_time type varchar(255);
    alter table dimRace alter column fp3_time type varchar(255);
    alter table dimRace alter column quali_time type varchar(255);
    alter table dimRace alter column sprint_time type varchar(255);