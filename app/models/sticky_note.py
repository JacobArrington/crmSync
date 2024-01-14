from .db import db,environment,SCHEMA, add_prefix_for_prod


class StickyNote(db.Model):
    __tablename__ ='sticky_note'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    widgetId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('widgets.id')), default=3)
    title = db.Column(db.String(255))
    note = db.Column(db.String(255))



    widget = db.relationship('Widget',
                                primaryjoin='Widget.id == StickyNote.widgetId',
                                back_populates='sticky_note',
                                useList=False,
                                viewonly=True,
                                )

    def to_sticky_dict(self):
        return{
            'id':self.id,
            'widgetId': self.widgetId,
            'title': self.title,
            'note': self.note,
            'widget': self.widget.to_dict() if self.widget else None
    }
