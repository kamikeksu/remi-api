import json, jwt

from notasquare.urad_api import *
from application.models import *
from application import constants
from django.db.models import Q
from django.core.management import call_command
from django.conf import settings

class List(handlers.standard.ListHandler):
    def create_query(self, data):
        query = Product.objects
        if 'name' in data:
            query= query.filter(name__contains= data['name'])
        if 'category_id' in data:
            query= query.filter(category_id= data['category_id'])
        return query
    def serialize_entry(self, product):
        return {
            'id':                  product.id,
            'name':                product.name,
            'image':               product.image,
            'price':               product.price,
            'category_id':         product.category_id,
            'category_name':       product.category.name
        }

class GetTest(handlers.standard.GetHandler):
    def get_data(self, data):
        product = Product.objects.all().first()
        arr = []
        for i in range(0,10):
            arr.append({
                'id':                  product.id,
                'name':                product.name,
                'image':               product.image,
                'price':               product.price,
                'category_id':         product.category_id,
                'category_name':       product.category.name
            })
        return arr

class Get(handlers.standard.GetHandler):
    def get_data(self, data):
        product = Product.objects.get(pk=data['id'])
        product_image = ProductImage.objects.filter(product_id= product.id)
        more_images= []
        for val in product_image:
            more_images.append(val.image)
        return {
            'id':                  product.id,
            'name':                product.name,
            'image':               product.image,
            'price':               product.price,
            'description':         product.description,
            'category_id':         product.category_id,
            'category_name':       product.category.name,
            'list_image':          more_images
        }

class Create(handlers.standard.CreateHandler):
    def create(self, data):
        product = Product()
        product.name = data.get('name', '')
        product.image = data.get('image', '')
        product.price = data.get('price', '')
        product.category_id = data.get('category_id', '')
        product.save()
        return product

class Update(handlers.standard.UpdateHandler):
    def update(self, data):
        product = Product.objects.get(pk=data['id'])
        product.name = data.get('name', '')
        product.image = data.get('image', '')
        product.price = data.get('price', '')
        product.category_id = data.get('category_id', '')
        product.save()

        return product

class Delete(handlers.standard.DeleteHandler):
    def delete(self, data):
        product = Product.objects.get(pk=data['id'])
        product.delete()
        return 1
