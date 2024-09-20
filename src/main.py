import pandas as pd
from data_processing import get_data_from_csv
from recommender_system import generate_genre_dictionary, clean_data, recommend_based_on_genre, print_recommendations, suggest_new_songs

def main():
    # Cargar datos
    spotify_songs_df = pd.read_csv('./data/spotify_songs.csv')
    genre_dictionary = generate_genre_dictionary()
    spotify_songs_df = clean_data(spotify_songs_df, genre_dictionary)

    # Lectura de información del usuario
    print('Nombre de usuario: ')
    path_user = input()
    recently_listened_df = get_data_from_csv('./data/'+ path_user +'.csv')
    recently_listened_ids = recently_listened_df['Id'].tolist()
    filtered_songs_df = spotify_songs_df[spotify_songs_df['track_id'].isin(recently_listened_ids)]
    filtered_songs_df.drop_duplicates(subset=['track_id']).to_csv('./data/filtered_data/filtered_songs_info.csv', index=False)

    # Generar recomendaciones
    recommendations_df = recommend_based_on_genre(spotify_songs_df, filtered_songs_df)
    print_recommendations(recommendations_df)
    
    suggest_new_songs(spotify_songs_df,filtered_songs_df)

if __name__ == "__main__":
    main()
