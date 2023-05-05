from sqlalchemy import create_engine
from sqlalchemy import text

from db_creation import Base
from db_functions import fn_insert_personal_data, fn_load_json, fn_insert_experiences, fn_insert_hard_skills

engine = create_engine("sqlite+pysqlite:///thiago_data.db", echo=True)
Base.metadata.create_all(engine, checkfirst=True)

dados_pessoais = fn_load_json('src_data/dados_pessoais.json')
experiences = fn_load_json('src_data/experiences.json')
hard_skills = fn_load_json('src_data/hard_skills.json')


fn_insert_personal_data(dados_pessoais, engine)
fn_insert_experiences(experiences, engine)
fn_insert_hard_skills(hard_skills, engine)

with engine.connect() as conn:
    result = conn.execute(text("select 'finalizado'"))
    conn.commit()
    print(result.all())
    conn.close()
