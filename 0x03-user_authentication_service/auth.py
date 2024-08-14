#!/usr/bin/env python3

import bcrypt
"""4. Hash password"""

def _hash_password(password: str) -> str:
    """hash password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
