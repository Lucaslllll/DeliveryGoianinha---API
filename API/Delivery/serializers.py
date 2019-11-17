from rest_framework import serializers
from .models import (
    Usuario, Restaurante, Classificacao_Usuario, Classificacao_Restaurante, 
    Fotos_Comida, Fotos_Restaurante, Ingredientes, Tipo, Tamanho, Codimentos,
    Pedido, Pedido_Restaurante, Comentario, Restaurante_Tag, Tags
)
from django.contrib.auth.models import User
from cloudinary.templatetags import cloudinary


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super(UsuarioSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

class RestauranteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def to_representation(self, instance):
        representation = super(RestauranteSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

        

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido_Restaurante
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'



# classificacao

class ClassificacaoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao_Usuario
        fields = '__all__'

class ClassificacaoUsuarioFNSerializer(serializers.Serializer):
    class Meta:
        model = Usuario
        fields = ('id', )

class ClassificacaoRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classificacao_Restaurante
        fields = '__all__'

class ClassificacaoRestauranteFNSerializer(serializers.Serializer):
    class Meta:
        model = Restaurante
        fields = ('id', )
        

# comida

class FotosRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos_Restaurante
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FotosRestauranteSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class FotosComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fotos_Comida
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(FotosComidaSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class IngredientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredientes
        fields = '__all__'

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ComidaSerializer, self).to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

class TamanhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tamanho
        fields = '__all__'

class CodimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Codimentos
        fields = '__all__'


# tags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class TagRestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante_Tag
        fields = '__all__'


class TagRestauranteFiltrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id']

