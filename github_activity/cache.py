"""Simple Redis cache module."""

import json
import redis

# Create a single Redis client
redis_client = None
try:
    # Simple connection to localhost Redis
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    redis_client.ping()  # Test connection
except Exception as e:
    print(f"Redis connection failed: {e}")
    redis_client = None

# Cache expiry time (1 hour)
CACHE_EXPIRY = 3600


def get(username):
    """Get cached data for a username."""
    if redis_client is None:
        return None
    
    try:
        # Simple key format
        key = f"github:{username}"
        data = redis_client.get(key)
        
        if data:
            return json.loads(data)
        return None
    except Exception:
        return None


def set(username, data):
    """Cache data for a username."""
    if redis_client is None:
        return
    
    try:
        # Simple key format
        key = f"github:{username}"
        redis_client.setex(key, CACHE_EXPIRY, json.dumps(data))
    except Exception:
        pass 