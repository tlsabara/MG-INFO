import json
from datetime import datetime

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from db_creation import Experiences, HardSkills, PersonalData


def fn_insert_personal_data(data_list: list, engi: Engine) -> bool:
    try:
        Session = sessionmaker(engi)
        for i in data_list:
            with Session.begin() as session:
                session.add(PersonalData(
                    pdata_name=i["pdata_name"],
                    pdata_description=i["pdata_description"],
                    pdata_value=i["pdata_value"]
                ))
                session.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True


def fn_insert_experiences(data_list: list, engi: Engine) -> bool:
    try:
        Session = sessionmaker(engi)
        for i in data_list:
            with Session.begin() as session:
                session.add(Experiences(
                    exp_ini_date=datetime.strptime(i["exp_ini_date"], '%Y-%m-%d'),
                    exp_end_date=datetime.strptime(i["exp_end_date"], '%Y-%m-%d'),
                    exp_company_name=i["exp_company_name"],
                    exp_company_role=i["exp_company_role"],
                    exp_description=i["exp_description"],
                ))
                session.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True


def fn_insert_hard_skills(data_list: list, engi: Engine) -> bool:
    try:
        Session = sessionmaker(engi)
        for i in data_list:
            with Session.begin() as session:
                session.add(HardSkills(
                    hskill_name=i["hskill_name"],
                    hskill_descripion=i["hskill_descripion"],
                    hskill_time=i["hskill_time"],
                    hskill_type1=i["hskill_type1"],
                    hskill_type2=i["hskill_type2"],
                ))
                session.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True


def fn_load_json(path_to_file: str):
    with open(path_to_file, encoding='utf-8', errors='ignore') as json_data:
        return json.load(json_data, strict=False)
