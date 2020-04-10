# import re
#
# from django.utils.deprecation import MiddlewareMixin
# # from django.http import HttpResponse
# from django.shortcuts import HttpResponse, redirect
#
# from yishared import settings
#
# # 方式一：
# class MyMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         current_url = request.path
#         print(current_url)
#         user = request.session.get('user')
#         if current_url in settings.NEEDLOGIN_LIST:
#             if user:
#                 return
#             else:
#                 return redirect(settings.LOGIN_URL)
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         pass
#
#     def process_exception(self, request, exception):
#         if isinstance(exception, ValueError):
#             return HttpResponse("404")
#
#     def process_response(self, request, response):
#         return response
