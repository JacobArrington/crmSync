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
                            uselist=False,
                            viewonly=True,
                                )

    def to_calc_dict(self):
        return{
            'id':self.id,
            'balance':str(self.balance),
            'lump_sum':str(self.lump_sum),
            'remainder_after_lump':str(self.remainder_after_lump),
            'interest_rate':str(self.interest_rate),
            'installment_options': self.installment_options,
            'custom_installment': self.custom_installment,
            'installment_amount':str(self.installment_amount),
            'discount':str(self.discount),
            'custom_discount':str(self.custom_discount),
            'total_after_discount':str(self.total_after_discount),
            'custom_monthly_payment':str(self.custom_monthly_payment),
            'custom_months_to_pay': self.custom_months_to_pay,
            'widgetId': self.widgetId,
            'widget': self.widget.to_dict() if self.widget else None
            }
