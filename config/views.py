from django.shortcuts import render
from google.cloud import bigquery
from pathlib import Path
import os


def steam_dashboard(request):
    # Como views.py y google-credentials.json están en la misma carpeta (config)
    # Usamos esta forma para encontrarlo sin fallos:
    directorio_actual = Path(__file__).resolve().parent
    path_to_key = os.path.join(directorio_actual, 'google-credentials.json')

    # 1. Configuramos la credencial
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path_to_key

    try:
        client = bigquery.Client()
        query = """
            SELECT 
                game_id, 
                volumen_comentarios as total_reviews,
                score_popularidad as score
            FROM `poetic-ceremony-472901-c7.steam_data_silver.v_steam_reviews_clean`
            ORDER BY volumen_comentarios DESC
            LIMIT 10
        """
        query_job = client.query(query)
        results = query_job.result()
        return render(request, 'dashboard.html', {'juegos': results})
    except Exception as e:
        # Si algo falla con los permisos de Google, lo veremos aquí
        return render(request, 'dashboard.html', {'error': str(e)})