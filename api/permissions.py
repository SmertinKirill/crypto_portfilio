# from rest_framework import permissions
# from portfolio.models import Portfolio


# class IsAuthor(permissions.BasePermission):
#     def has_permission(self, request, view):
#         blocked = Portfolio.objects.filter(user=request.user).exists()
#         return not blocked

#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         elif request.method in ['PUT', 'PATCH', 'DELETE']:
#             return obj.author == request.user
