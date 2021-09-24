from rest_framework import permissions

class UserReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        #if request.method in permissions.SAFE_METHODS:
        #    return True
        if obj.ownerTodo == request.user :
            return True
        else : 
            #eturn obj.ownerTodo == request.user
            return False