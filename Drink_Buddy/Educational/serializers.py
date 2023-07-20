from rest_framework import serializers
from .models import Educational

class EducationalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educational
        # fields = '__all__'
        fields = ['id', 'title', 'description', 'date','url']

class EducationalHyperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Educational
<<<<<<< HEAD
        fields = ['id', 'title', 'description', 'date', 'url']
=======
<<<<<<< HEAD
        fields = ['id', 'title', 'description', 'date', 'url']
=======
        fields = ['id', 'title', 'description', 'date', 'url']
>>>>>>> Raman
>>>>>>> 3bece1c72049cfedf9d630b1e0030670119fa109
