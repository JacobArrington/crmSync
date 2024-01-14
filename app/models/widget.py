from .db import db,environment,SCHEMA, add_prefix_for_prod

class Widget(db.Model):
    __tablename__ ="widgets"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


        id = db.Column(db.integer, primary_key = True)
        user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
        widget_type = db.Column(db.String(255))

        user = db.relationship('User', back_populates= 'widgets' )


        def widget_to_dict(self):
            return{
                'id': self.id,
                'userId': self.user_id,
                'type': self.type

            }
