from rest_framework.permissions import BasePermission, SAFE_METHODS


# class nay dung cho phuong thuc update
class IsOwnerPermission(BasePermission):
    message = 'Ban ko phai la chu cua post nay'

    def has_permission(self, request, view):
        my_safe_methods = ['GET', 'PUT']
        if request.method in my_safe_methods:
            return True

    # method nay chi lam viec khi has_permission la True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
