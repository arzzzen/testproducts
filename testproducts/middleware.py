from products.models import Resp

class ResponseMiddleware(object):
    def process_response(self, request, response):
        respon = Resp.objects.create(url = request.path, method = request.method, status_code = response.status_code)
        respon.save
        return response