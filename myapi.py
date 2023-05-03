import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('9bE2uBS0Fr0r2c6GE4VY2Qqq4VVHW2Xd0ebKj0GDUxI')

    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response

    def named_entity_recognition(self,text):
        response=paralleldots.ner(text)
        return response