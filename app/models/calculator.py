from .db import db,environment,SCHEMA, add_prefix_for_prod

class Calculator(db.Model):
    __tablename__ = 'calculators'

    if environment == "production":
        __table_args__={'schema': SCHEMA}

        id = db.Column(db.Integer, primary_key=True)
        widgetId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('widgets.id')), default=1)
        balance = db.Column(db.Numeric(precision=10, scale=2))
        lump_sum = db.Column(db.Numeric(precision=10, scale=2))
        remainder_after_lump = db.Column(db.Numeric(precision=10, scale=2))
        interest_rate = db.Column(db.Numeric(precision=4, scale=2))
        installment_options = db.Column(db.Integer)
        custom_installment = db.Column(db.Integer)
        installment_amount = db.Column(db.Numeric(precision=10, scale=2))
        discount = db.Column(db.Numeric(precision=3, scale=2))
        custom_discount = db.Column(db.Numeric(precision=3, scale=2))
        total_after_discount =db.Column(db.Numeric(precision=10, scale=2))
        custom_monthly_payment =db.Column(db.Numeric(precision=10, scale=2))
        custom_months_to_pay =db.Column(db.Integer)


        widget = db.relationship('Widget',
                                primaryjoin='Widget.id ==Calculator.widgetId',
                                back_populates='calculator',
                                useList=False,
                                viewonly=True,
                                )
