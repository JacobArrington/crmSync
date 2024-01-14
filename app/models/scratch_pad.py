from .db import db,environment,SCHEMA, add_prefix_for_prod


class ScratchPad(db.Model):
    __tablename__ ='scratch_pad'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    widgetId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('widgets.id')), default=2)
    
    widget = db.relationship('Widget',
                                primaryjoin='Widget.id ==Calculator.widgetId',
                                back_populates='scratch_pad',
                                useList=False,
                                viewonly=True,
                                )

    def to_pad_dict(self):
        return{
            'id':self.id,
            'widgetId': self.widgetId,
            'widget': self.widget.to_dict() if self.widget else None
    }
