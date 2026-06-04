import sqlalchemy as db
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class dim_date(Base):
    __tablename__='dim_date'
    dateId=db.Column(db.String(200), primary_key=True)
    date=db.Column(db.Date)
    year=db.Column(db.Integer)
    month=db.Column(db.Integer)
    day=db.Column(db.Integer)

class dim_race(Base):
    __tablename__='dim_race'
    raceId=db.Column(db.Integer, primary_key=True)
    year=db.Column(db.Integer)
    round=db.Column(db.Integer)
    race_name=db.Column(db.String(200))
    date=db.Column(db.Date)
    races_time=db.Column(db.String(200))
    race_url=db.Column(db.String(200))
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
    dateId=db.Column(db.String(200), db.ForeignKey(dim_date.dateId))


class dim_driver(Base):
    __tablename__='dim_driver'
    driverId=db.Column(db.Integer, primary_key=True)
    driverRef=db.Column(db.String(200))
    drivers_number=db.Column(db.Integer)
    code=db.Column(db.String(200))
    forename=db.Column(db.String(200))
    surname=db.Column(db.String(200))
    dob=db.Column(db.Date)
    driver_nationality=db.Column(db.String(200))
    driver_url=db.Column(db.String(200))


class dim_status(Base):
    __tablename__='dim_status'
    statusId=db.Column(db.Integer, primary_key=True)
    status=db.Column(db.String(200))



class dim_constructor(Base):
    __tablename__='dim_constructor'
    constructorId=db.Column(db.Integer, primary_key=True)
    constructorRef=db.Column(db.String(200))
    constructors_name=db.Column(db.String(200))
    constructors_nationality=db.Column(db.String(200))
    constructors_url=db.Column(db.String(200))


class dim_circuit(Base):
    __tablename__='dim_circuit'
    circuitId=db.Column(db.Integer, primary_key=True)
    circuitRef=db.Column(db.String(200))
    circuit_name=db.Column(db.String(200))
    location=db.Column(db.String(200))
    country=db.Column(db.String(200))
    lat=db.Column(db.Float)
    lng=db.Column(db.Float)
    alt=db.Column(db.Float)
    circuit_url=db.Column(db.String(200))


class dim_driverstandings(Base):
    __tablename__='dim_driverstandings'
    driverStandingsId=db.Column(db.Integer, primary_key=True)
    driverstandings_points=db.Column(db.Float)
    driverstandings_position=db.Column(db.Integer)
    driverstandings_positionText=db.Column(db.String(200))
    driverstandings_wins=db.Column(db.Integer)


class dim_constructorstandings(Base):
    __tablename__='dim_constructorstandings'
    constructorStandingsId=db.Column(db.Integer, primary_key=True)
    constructorstandings_points=db.Column(db.Float)
    constructorstandings_position=db.Column(db.Integer)
    constructorstandings_positionText=db.Column(db.String)
    constructorstandings_wins=db.Column(db.Integer)


class fact_results(Base):
    __tablename__='fact_results'
    resultId=db.Column(db.Integer, primary_key=True)
    raceId=db.Column(db.Integer, db.ForeignKey('dim_race.raceId'))
    driverId=db.Column(db.Integer, db.ForeignKey('dim_driver.driverId'))
    constructorId=db.Column(db.Integer, db.ForeignKey('dim_constructor.constructorId'))
    statusId=db.Column(db.Integer, db.ForeignKey('dim_status.statusId'))
    circuitId=db.Column(db.Integer, db.ForeignKey('dim_circuit.circuitId'))
    driverStandingsId=db.Column(db.Integer, db.ForeignKey('dim_driverstandings.driverStandingsId'))
    constructorStandingsId=db.Column(db.Integer, db.ForeignKey('dim_constructorstandings.constructorStandingsId'))
    number=db.Column(db.Integer)
    grid=db.Column(db.Integer)
    position=db.Column(db.Integer)
    positionText=db.Column(db.String(200))
    positionOrder=db.Column(db.Integer)
    points=db.Column(db.Float)
    time=db.Column(db.String(200))
    milliseconds=db.Column(db.Integer)
    laps=db.Column(db.Integer)
    fastestLap=db.Column(db.Integer)
    fastestLapTime=db.Column(db.String(200))
    fastestLapSpeed=db.Column(db.Float)
    rank=db.Column(db.Integer)


class fact_lap(Base):
    __tablename__='fact_lap'
    raceId=db.Column(db.Integer,  db.ForeignKey('dim_race.raceId'), primary_key=True)
    driverId=db.Column(db.Integer, db.ForeignKey('dim_driver.driverId'), primary_key=True)
    lap=db.Column(db.Integer, primary_key=True)
    laptimes_position=db.Column(db.Integer)
    laptimes_time=db.Column(db.String(200))
    laptimes_milliseconds=db.Column(db.Integer)


class fact_pitstops(Base):
    __tablename__='fact_pitstops'
    raceId=db.Column(db.Integer,  db.ForeignKey('dim_race.raceId'), primary_key=True)
    driverId=db.Column(db.Integer, db.ForeignKey('dim_driver.driverId'), primary_key=True)
    stop=db.Column(db.Integer, primary_key=True)
    pitstops_lap=db.Column(db.Integer)
    pitstops_time=db.Column(db.String(200))
    duration=db.Column(db.Float)
    pitstops_milliseconds=db.Column(db.Integer)