from .db import db,environment,SCHEMA, add_prefix_for_prod


class HotList(db.Model):
    __tablename__ ='hot_list'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    widgetId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('widgets.id')), default=3)
    dt = db.Column(db.String(255))
    account_balance = db.Column(db.String(255))
    note = db.Column(db.String(255))



    widget = db.relationship('Widget',
                                primaryjoin='Widget.id == HotList.widgetId',
                                back_populates='hot_list',
                                uselist=False,
                                viewonly=True,
                                )

    def to_hot_dict(self):
        return{
            'id':self.id,
            'widgetId': self.widgetId,
            'dt': self.dt,
            'note': self.note,
            'account_balance':self.account_balance,
            'widget': self.widget.to_dict() if self.widget else None
            
    }
