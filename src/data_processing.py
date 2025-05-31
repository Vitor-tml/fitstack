import pandas as pd
import random
import datetime

def load_users(num_users=5):
    user_ids = range(1, num_users + 1)
    genders = [random.choice(['M', 'F']) for _ in range(num_users)]
    ages = [random.randint(18, 65) for _ in range(num_users)]
    return pd.DataFrame({
        'user_id': user_ids,
        'gender': genders,
        'age': ages
    })

def load_checkins(num_checkins=12, existing_users=None):
    if existing_users is None:
        existing_users = load_users()
    user_ids = existing_users['user_id'].tolist()
    
    start_date = pd.to_datetime('2025-01-01')
    end_date = pd.to_datetime('2026-01-01')
    
    checkin_times = [pd.to_datetime(start_date + (end_date - start_date) * random.random()) for _ in range(num_checkins)]
    random_user_ids = [random.choice(user_ids) for _ in range(num_checkins)]
    
    checkins = pd.DataFrame({
        'user_id': random_user_ids,
        'checkin_time': checkin_times
    })
    
    checkins['checkin_time'] = pd.to_datetime(checkins['checkin_time'])
    return checkins