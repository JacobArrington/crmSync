from .db import db,environment,SCHEMA, add_prefix_for_prod
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base=declarative_base()

class Widget(db.Model):
    __tablename__ ="widgets"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


        id = db.Column(db.integer, primary_key = True)
        user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
        widget_type = db.Column(db.String(255))

         # one to many
        user = db.relationship('User', back_populates= 'widgets' )

        #polymorphic 
        calculator = db.relationship('Calculator', useList=False, back_populates = 'widget')
        scratch_pad = db.relationship('ScratchPad', useList=False, back_populates = 'widget')


        def set_widget_type(self):
            if self.id ==1:
                self.widget_type = "Calculator"
            elif self.id ==2:
                self.widget_type = "Scratchpad"


        def to_widget_dict(self):
            return{
                'id': self.id,
                'userId': self.user_id,
                'widget_type': self.widget_type

            }
