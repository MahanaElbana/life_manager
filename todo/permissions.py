from rest_framework import permissions

class UserReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        if obj.ownerTodo == request.user :
            return True
        else : 
            return False
