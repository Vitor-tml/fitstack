import pandas as pd

def get_season(date):
    month = date.month
    if month in [12, 1, 2]:
        return 'Summer'
    elif month in [3, 4, 5]:
        return 'Autumn'
    elif month in [6, 7, 8]:
        return 'Winter'
    else:
        return 'Spring'

def generate_features(users, checkins):
    checkins['season'] = checkins['checkin_time'].apply(get_season)
    today = pd.to_datetime('2026-02-01')

    agg = checkins.groupby('user_id').agg(
        total_checkins=('checkin_time', 'count'),
        recency_days=('checkin_time', lambda x: (today - x.max()).days),
        avg_days_between=('checkin_time', lambda x: x.sort_values().diff().mean().days if len(x) > 1 else 0)
    ).reset_index()

    season_counts = checkins.groupby(['user_id', 'season']).size().unstack(fill_value=0).reset_index()

    features = users.merge(agg, on='user_id', how='left')
    features = features.merge(season_counts, on='user_id', how='left')

    for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
        if season not in features.columns:
            features[season] = 0

    return features
