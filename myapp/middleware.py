from django.utils import timezone
from .models import UserActivity
import user_agents
import logging
import json

logger = logging.getLogger(__name__)

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        try:
            if hasattr(request, 'user') and request.user.is_authenticated:
                self._log_user_activity(request)
        except Exception as e:
            logger.error(f"Error in UserActivityMiddleware: {str(e)}", exc_info=True)
        
        return response
    
    def _log_user_activity(self, request):
        """Helper method to log user activity"""
        activity_type = self._get_activity_type(request)
        if not activity_type:
            return
            
        try:
            user_agent_string = request.META.get('HTTP_USER_AGENT', '')
            user_agent = user_agents.parse(user_agent_string)
            
            # Get IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
            ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR', '')
            
            # Prepare device info
            device_info = f"{user_agent.device.family or 'Unknown'} / {user_agent.os.family or 'Unknown'}"
            
            # Prepare additional data
            additional_data = {
                'path': request.path,
                'method': request.method,
                'user_agent': str(user_agent)
            }
            
            # Create activity log
            UserActivity.objects.create(
                user=request.user,
                activity_type=activity_type,
                ip_address=ip or None,
                device=device_info[:255],  # Ensure it doesn't exceed max_length
                additional_data=additional_data
            )
            
        except Exception as e:
            logger.error(f"Failed to log user activity: {str(e)}", exc_info=True)
    
    def _get_activity_type(self, request):
        """Determine activity type based on request"""
        path = request.path.lower()
        
        if path.endswith('/login/'):
            return 'LOGIN'
        elif path.endswith('/logout/'):
            return 'LOGOUT'
        elif path.endswith('/register/'):
            return 'REGISTER'
        elif '/cart/' in path:
            return 'ADD_TO_CART'
        elif '/product/' in path and request.method == 'GET':
            return 'PAGE_VIEW'
        return None