class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']