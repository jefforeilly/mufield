from rest_framework import serializers


class ChatsQuerySet(serializers.HyperlinkedModelSerializer):
    pass


'''
from apps.api.v0.models import Chats



    def get_id_by_token(self, chat_token):
        return self.only('id').get(id=ObjectId(chat_token))

    def get_all_by_token(self, chat_token):
        return self.get(id=ObjectId(chat_token))

    def get_active(self, chat_token, user_token, status=None):
        status = status or []
        return self.get(id=ObjectId(chat_token),
                        status__in=status,
                        user_tokens=ObjectId(user_token))

    def get_chat(self, chat_token, user_token):
        return self.get(id=ObjectId(chat_token), user_tokens=ObjectId(user_token))
    class Meta:
        model=Chats
        '''
