from main import db

class Product(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'checkout_system_product'
    product_code = db.Column(
        db.String(10),
        primary_key=True
    )
    product_name = db.Column(
        db.String(64),
        index=False,
        unique=True,
        nullable=False
    )
    price = db.Column(
        db.Integer,
        #index=True,
        #unique=True,
        nullable=False
    )

    def __repr__(self):
        return '<Product {}>'.format(self.product_name)
