#!/usr/bin/env python3
'''
SESSION DB AUTH MODULE
'''
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    '''
    SessionDBAuth class
    '''

    def create_session(self, user_id: str = None) -> str:
        '''
        create_session function
        '''
        if session_id is None:
            return None
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            user_session = []
        if len(user_session) == 0:
            return None
        if self.session_duration <= 0:
            return user_session[0].user_id
        create_at = user_session[0].created_at
        create_at += timedelta(0, self.session_duration)
        if create_at < datetime.now():
            return None
        return user_session[0].user_id
    
    def destroy_session(self, request=None):
        '''
        destroy_session function
        '''
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        try:
            user = UserSession.search({'session_id': session_id})
        except Exception:
            user = []
        if len(users) == 0:
            return None
        user[0].remove()
