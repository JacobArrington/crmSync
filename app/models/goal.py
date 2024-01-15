from .db import db,environment,SCHEMA, add_prefix_for_prod


class Goal(db.Model):
    __tablename__ ='goals'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    widgetId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('widgets.id')), default=3)
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))
    time_frame = db.Column(db.String(255))



    widget = db.relationship('Widget',
                                primaryjoin='Widget.id == Goal.widgetId',
                                back_populates='goals',
                                uselist=False,
                                viewonly=True,
                                )

    def to_goal_dict(self):
        return{
            'id':self.id,
            'widgetId': self.widgetId,
            'title': self.title,
            'note': self.note,
            'time_frame':self.time_frame,
            'widget': self.widget.to_dict() if self.widget else None
            
    }
