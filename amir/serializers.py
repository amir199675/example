from rest_framework import serializers
from .models import *


class Bookserializers(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = (
			'name',
			'type',
			'author'

		)
class Authserializers(serializers.ModelSerializer):
	auth = Bookserializers(many=True,read_only=True)
	class Meta:
		model = Author
		fields = (
			'name',
			'auth'

		)
