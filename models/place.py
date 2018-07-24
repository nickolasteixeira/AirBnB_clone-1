#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship(
        "Review",
        backref='place',
        cascade='all, delete-orphan')
    amenities = relationship(
        "Aemnity", secondary='place_amenity', viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        ''' Getters for properties'''
        get_all = models.storage.all('Reviews')
        return [obj for obj in get_all if obj.place_id == self.id]

    @property
    def amenities(self):
        ''' Getters for amenities'''
        get_all = models.storage.all('Amenities')
        return [obj for obj in get_all if obj.amenity_ids == Amenity.id]

    @amenities.setter
    def amenities(self, obj):
        ''' Setter for amenities'''
        if isinstance(obj, 'Amenities'):
            self.amenity_ids.append(obj.id)
