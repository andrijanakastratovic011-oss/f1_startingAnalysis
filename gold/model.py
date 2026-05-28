import sqlalchemy as db
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class dim_race(Base):
    __tablename__='dim_race'
    raceId=db.Column(db.Integer, primary_key=True)
    year=db.Column(db.Integer)
    round=db.Column(db.Integer)
    name_x=db.Column(db.String(200))
    date=db.Column(db.Date)
    time_races=db.Column(db.String(200))
    url_x=db.Column(db.String(200))
    fp1_date=db.Column(db.Date)
    fp1_time=db.Column(db.String(200))
    fp2_date=db.Column(db.Date)
    fp2_time=db.Column(db.String(200))
    fp3_date=db.Column(db.Date)
    fp3_time=db.Column(db.String(200))
    quali_date=db.Column(db.Date)
    quali_time=db.Column(db.String(200))
    sprint_date=db.Column(db.Date)
    sprint_time=db.Column(db.String(200))


class dim_driver(Base):
    __tablename__='dim_driver'
    driverId=db.Column(db.Integer, primary_key=True)
    driverRef=db.Column(db.String(200))
    number_drivers=db.Column(db.Integer)
    code=db.Column(db.String(200))
    forename=db.Column(db.String(200))
    surname=db.Column(db.String(200))
    dob=db.Column(db.Date)
    nationality=db.Column(db.String(200))
    url=db.Column(db.String(200))


class dim_status(Base):
    __tablename__='dim_status'
    statusId=db.Column(db.Integer, primary_key=True)
    status=db.Column(db.String(200))


class dim_date(Base):
    __tablename__='dim_date'
    dateId=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date)
    year=db.Column(db.Integer)
    month=db.Column(db.Integer)
    day=db.Column(db.Integer)


class dim_constructor(Base):
    __tablename__='dim_constructor'
    constructorId=db.Column(db.Integer, primary_key=True)
    constructorRef=db.Column(db.String(200))
    name=db.Column(db.String(200))
    nationality_constructors=db.Column(db.String(200))
    url_constructors=db.Column(db.String(200))


class dim_circuit(Base):
    __tablename__='dim_circuit'
    circuitId=db.Column(db.Integer, primary_key=True)
    name_y=db.Column(db.String(200))
    location=db.Column(db.String(200))
    country=db.Column(db.String(200))
    lat=db.Column(db.Float)
    lng=db.Column(db.Float)
    alt=db.Column(db.Float)
    url_y=db.Column(db.String(200))


class dim_driverstandings(Base):
    __tablename__='dim_driverstandings'
    driverstandingsId=db.Column(db.Integer, primary_key=True)
    points_driverstandings=db.Column(db.Float)
    position_driverstandings=db.Column(db.Integer)
    position_text_driverstandings=db.Column(db.String(200))
    wins=db.Column(db.Integer)


class dim_constructorstandings(Base):
    __tablename__='dim_constructorstandings'
    constructorstandingsId=db.Column(db.Integer, primary_key=True)
    points_constructorstandings=db.Column(db.Float)
    position_constructorstandings=db.Column(db.Integer)
    position_text_constructorstandings=db.Column(db.String)
    wins_constructorstandings=db.Column(db.Integer)


class fact(Base):
    __tablename__='fact'
    resultId=db.Column(db.Integer, primary_key=True)
    raceId=db.Column(db.Integer, db.ForeignKey('dim_race.raceId'))
    driverId=db.Column(db.Integer, db.ForeignKey('dim_driver.driverId'))
    constructorId=db.Column(db.Integer, db.ForeignKey('dim_constuctor.constructorId'))
    statusId=db.Column(db.Integer, db.ForeignKey('dim_status.statusId'))
    circuitId=db.Column(db.Integer, db.ForeignKey('dim_circuit.circuitId'))
    driverstandingsId=db.Column(db.Integer, db.ForeignKey('dim_driverstandings.driverstandingsId'))
    constructorstandingsId=db.Column(db.Integer, db.ForeignKey('dim_constuctorstandings.constructorstandingsId'))
    dateId=db.Column(db.Integer, db.ForeignKey('dim_date.date_id'))
    number=db.Column(db.Integer)
    grid=db.Column(db.Integer)
    postion=db.Column(db.Integer)
    position_text=db.Column(db.String(200))
    position_order=db.Column(db.Integer)
    points=db.Column(db.Float)
    time=db.Column(db.String(200))
    milliseconds=db.Column(db.Integer)
    laps=db.Column(db.Integer)
    fastest_lap=db.Column(db.Integer)
    fastest_lap_time=db.Column(db.String(200))
    fastest_lap_speed=db.Column(db.String(200))
    rank=db.Column(db.Integer)


class fact_lap(Base):
    __tablename__='fact_lap'
    raceId=db.Column(db.Integer,  db.ForeignKey('dim_race.raceId'), primary_key=True)
    driverId=db.Column(db.Integer, db.ForeignKey('dim_driver.driverId'), primary_key=True)
    lap=db.Column(db.Integer)
    position_laptimes=db.Column(db.Integer)
    time_laptimes=db.Column(db.String(200))
    milliseconds_laptimes=db.Column(db.Integer)


class fact_pitstops(Base):
    __tablename__='fact_pitstops'
    raceId=db.Column(db.Integer,  db.ForeignKey('dim_race.raceId'), primary_key=True)
    driverId=db.Column(db.Integer, db.ForeignKey('dim_driver.driverId'), primary_key=True)
    stop=db.Column(db.Integer)
    lap_pitstops=db.Column(db.Integer)
    time_pitstops=db.Column(db.String(200))
    duration=db.Column(db.Float)
    milliseconds_pitstops=db.Column(db.Integer)