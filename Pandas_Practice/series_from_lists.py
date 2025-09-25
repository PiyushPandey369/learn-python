import pandas as pd

# string
country=["Nepal","India","New Zealands","Spain","China","Germany"]
country_series=pd.Series(country)
print(country_series)

# integer
runs=[3,67,5,33,80,110,0,145]
runs_series=pd.Series(runs)
print(runs_series)

# custom index
marks=[70,46,90,78]
subjects=["Physic","English","Maths","Computer"]
marks_series=pd.Series(marks,index=subjects)
print(marks_series)

# setting a name
marks_series_name=pd.Series(marks,index=subjects,name="Marks Scored")
print(marks_series_name)

# series from dict -> Better than Custom Indexing
marks_dict={"Maths":91,"Science":68,"Computer":78,"Biology":14}
marks_dict_series=pd.Series(marks_dict)
print(marks_dict_series)