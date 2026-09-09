
import pandas as pd

as_text = {"CaseNo": str}
offenses = pd.read_csv("data/lapd_nibrs_offenses_k7nn-b2ep.csv", dtype=as_text,
                       usecols=["CaseNo", "NIBR Code", "Crime Against"])
victims = pd.read_csv("data/lapd_nibrs_victims_gqf2-vm2j.csv", dtype=as_text,
                      usecols=["CaseNo", "Victim Type", "Vict Age"])
people = victims[victims["Victim Type"] == "Person"]
age_by_case = people.groupby("CaseNo")["Vict Age"].mean()
joined = offenses.join(age_by_case, on="CaseNo")
print(joined.shape)
print(joined.groupby("Crime Against")["Vict Age"].mean().round(1))
