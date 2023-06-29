"""
Name : models.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 29/06/2023 10:16 PM
Desc: models.py
"""
from app.extensions import db
from app.util import PaymentMode


class CandidatePayment(db.Model):
    __tablename__ = "candidate_payment"
    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey("candidate.candidate_id"))
    agreed_amount = db.Column(db.Float, nullable=False)
    paid_amount = db.Column(db.Float, nullable=False)
    paid_date = db.Column(db.Datetime, nullable=False)
    due_amount = db.Column(db.Float, nullable=False)
    payment_mode = db.Column(db.Enum(PaymentMode), nullable=False, comment="specifying the payment is used for.")

    def __init__(self, payment_id, candidate_id, payment_mode):
        self.payment_id = payment_id
        self.candidate_id = candidate_id
        self.payment_mode = payment_mode

    def __repr__(self):
        return '<CandidatePayment %r %r %r>' % self.payment_id, self.candidate_id, self.payment_mode
