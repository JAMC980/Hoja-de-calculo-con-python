from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'C:\Users\jorge\OneDrive\Escritorio\HC\key.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

spreadsheet_id = '1Tuv0YMqvpPK0PO3eTPCfhNDMFgMJaZauryby3_2SvMY'
sheet_name = 'HC'
range_name_a = 'A2:A'  # El rango de la columna A que deseas ordenar
range_name_b = 'B2:C'  # El rango de las columnas B y C que deseas ordenar

# Algoritmo de ordenamiento de burbuja para la columna A
def bubble_sort(columna):
    n = len(columna)
    for i in range(n):
        for j in range(0, n-i-1):
            if columna[j] > columna[j+1]:
                columna[j], columna[j+1] = columna[j+1], columna[j]
    return columna

# Algoritmo de ordenamiento de inserción para la columna B
def insertion_sort(columna):
    for i in range(1, len(columna)):
        actual = columna[i]
        j = i - 1
        while j >= 0 and actual < columna[j]:
            columna[j + 1] = columna[j]
            j -= 1
        columna[j + 1] = actual
    return columna

# Algoritmo de ordenamiento de selección para la columna C
def selection_sort(columna):
    for i in range(len(columna)):
        min_idx = i
        for j in range(i+1, len(columna)):
            if columna[min_idx] > columna[j]:
                min_idx = j
        columna[i], columna[min_idx] = columna[min_idx], columna[i]
    return columna

# Obtiene los valores de la columna A
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=sheet_name + '!' + range_name_a).execute()
columna_a = result.get('values', [])

# Ordena la columna A utilizando el algoritmo de burbuja
columna_a_ordenada = bubble_sort(columna_a)

# Actualiza los valores ordenados de la columna A en la hoja de cálculo
body = {
    'values': columna_a_ordenada
}
result = service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id, range=sheet_name + '!' + range_name_a,
    valueInputOption='RAW', body=body).execute()

# Obtiene los valores de las columnas B y C
result = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id, range=sheet_name + '!' + range_name_b).execute()
columnas_bc = result.get('values', [])

# Separa las columnas B y C en dos listas distintas
columna_b = [fila[0] for fila in columnas_bc]
columna_c = [fila[1] for fila in columnas_bc]

# Ordena las columnas B y C utilizando los algoritmos de inserción y selección, respectivamente
columna_b
