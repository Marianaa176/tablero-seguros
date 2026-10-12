import os, sqlite3
import pandas as pd

def ruta_parquet():
    for r in ["datos.parquet",
              "../../Modulo_4/m4t2_sesion1/datos/datos.parquet"]:
        if os.path.exists(r):
            return r
    raise FileNotFoundError("No encuentro datos.parquet")

df  = pd.read_parquet(ruta_parquet())
con = sqlite3.connect("cartera.db")                 # crea el archivo de la BD
df.to_sql("cartera", con, if_exists="replace", index=False)   # vuelca el DataFrame a una tabla
con.close()
print(f"cartera.db creada: {len(df):,} filas en la tabla 'cartera'")
# %%
