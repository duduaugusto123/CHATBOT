
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests
import json


psid = "g.a000fwjTakASABkH81w5mKZBo0vq8xCx1kL2RovsfAIz7cyQF3zuJBjBjng5hxZSjgTPI0QiTQACgYKAeISAQASFQHGX2MiT5ohfLSu0mnQO5_-Pm3H6hoVAUF8yKrYNXs6xLbnsb_djG-Fn4Mv0076"
psidts = "sidts-CjIBPVxjSj5PPmiAbXDN1Xs7zYQoMKqHjRP2vWtQs8vrwaVsOz9iToY8LUGjkL4-5pTLIRAA"
psidcc = "ABTWhQHs222KlDoflJ8tN6u8PxNLUTthf49MSQilVVpfzp9S7O1kTbfVNBTXRY_9xsrp0VGQoQ"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado

mockedResponse = '{"content": "blá blá"}'
enableMock = True


#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        bard = None
        answer = json.loads(mockedResponse)

        if enableMock == False:
            bard = BardCookies(cookie_dict=tokenCookies) 
                    
        #pega os dados que veio na requisição
        data = request.data

        #pega o dados da conversationId caso ele seja informado para mander a mesma conversa com o chatbot
        conversationId = data.get("conversationId")

        #verifica se o id da conversa foi recebido
        if(conversationId is not None):

            #informa o bard para responder na conversa desejada
            bard.conversation_id = conversationId
        elif enableMock == False:
            bard.conversation_id = None
        

        # answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

