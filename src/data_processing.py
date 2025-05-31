import pandas as pd

def load_users():
    return pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5],
        'gender': ['M', 'F', 'F', 'M', 'F'],
        'age': [25, 34, 29, 40, 22]
    })

def load_checkins():
    checkins = pd.DataFrame({
        'user_id': [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5],
        'checkin_time': [
            '2025-06-01 10:00', '2025-07-15 12:00',
            '2025-12-05 09:00', '2025-12-10 10:00', '2026-01-05 08:00',
            '2025-03-01 09:00', '2025-04-02 09:00',
            '2025-09-01 18:00',
            '2025-06-05 15:00', '2025-06-07 16:00', '2025-08-01 20:00', '2025-12-01 22:00'
        ]
    })
    checkins['checkin_time'] = pd.to_datetime(checkins['checkin_time'])
    return checkins
