import pandas as pd
from prettytable import PrettyTable

def generate_genre_dictionary():
    return {
        'edm': 1, 'rap': 2, 'pop': 3, 'r&b': 4, 'latin': 5, 'rock': 6
    }

def clean_data(spotify_songs_df, genre_dictionary):
    spotify_songs_df['genre_clean'] = spotify_songs_df['playlist_genre'].apply(lambda x: genre_dictionary.get(x, 0))
    spotify_songs_df.astype({'playlist_genre':'category'})
    return spotify_songs_df

def recommend_based_on_genre(spotify_songs_df, filtered_songs_df):
    most_common_genre = filtered_songs_df['genre_clean'].value_counts().idxmax()
    recently_listened_ids = filtered_songs_df['track_id'].tolist()
    recommendations_df = spotify_songs_df[(spotify_songs_df['genre_clean'] == most_common_genre) & (~spotify_songs_df['track_id'].isin(recently_listened_ids))]
    return recommendations_df.sample(n=15, random_state=42)

def print_recommendations(recommendations_df):
    print("Canciones recomendadas basadas en el género más común:")
    table = PrettyTable(['ID', 'Nombre de canción', 'Artista', 'Género'])
    for index, row in recommendations_df.iterrows():
        table.add_row([row['track_id'], row['track_name'], row['track_artist'], row['genre_clean']])
    print(table)

from prettytable import PrettyTable

def suggest_new_songs(spotify_songs_df, filtered_songs_df, n=15, save_to_csv=False):
    # Obtener las IDs de las canciones recientemente escuchadas
    recently_listened_ids = filtered_songs_df['track_id'].tolist()
    
    # Filtrar todas las canciones que no han sido escuchadas
    new_suggestions_df = spotify_songs_df[~spotify_songs_df['track_id'].isin(recently_listened_ids)]
    
    # Seleccionar 15 canciones aleatorias de las no escuchadas
    new_suggestions_df = new_suggestions_df.sample(n=n)
    
    # Mostrar las canciones recomendadas aleatorias
    print("Sugerencias completamente nuevas para el usuario:")
    table = PrettyTable(['ID', 'Nombre de canción', 'Artista', 'Género'])
    for index, row in new_suggestions_df.iterrows():
        table.add_row([row['track_id'], row['track_name'], row['track_artist'], row['genre_clean']])
    print(table)
    
    # Guardar las sugerencias en un archivo CSV si es necesario
    if save_to_csv:
        new_suggestions_df.to_csv('../data/filtered_data/random_recommendations.csv', index=False)
    
    return new_suggestions_df
