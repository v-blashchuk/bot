import mongoengine as me
import datetime

me.connect('bot_db')


class Category(me.Document):
    title = me.StringField(min_length=1, max_length=512)
    description = me.StringField(min_length=2, max_length=4096)
    subcategories = me.ListField(me.ReferenceField('self'))
    parent = me.ReferenceField('self', default=None)



class Products(me.Document):
    title = me.StringField(min_length=1, max_length=512)
    description = me.StringField(min_length=2 ,max_length=4096)
    created = me.DateField(default=datetime.datetime.now())
    price = me.DecimalField(required=True)
    in_stock = me.BooleanField(default=True)
    discount = me.IntField(min_value=0, max_value=100)
    image = me.FileField(required=True)
    category = me.ReferenceField(Category)


class Text(me.Document):

    TITLES = {
        'greetings': 'Текст приветствия',
        'cart': 'Текст корзины'
    }
    title = me.StringField(min_length=1, max_length=256, choices=TITLES.values(), unique=True)
    body = me.StringField(min_length=1, max_length=4096)