# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Machine(db.Model):
    __tablename__ = 'machine'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False, server_default=db.FetchedValue())
    ip = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    user = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    password = db.Column(db.String(50), nullable=False, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())


class Monitor(db.Model):
    __tablename__ = 'monitor'

    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.String(50), nullable=False, index=True)
    cpu = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    memory = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
