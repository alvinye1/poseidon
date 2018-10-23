#!/usr/bin/python3
#==============================================
#This is an financial alpha test program.
#programmed by Alvin.Ye copy right reserved
#==============================================
from jqdatasdk import *
auth('13581701555','yelun007')
a=get_all_securities()
#b=jd.macro.run_query()

q = query(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR
        ).filter(macro.MAC_INDUSTRY_AREA_AGR_OUTPUT_VALUE_YEAR.stat_year=='2014')
df = macro.run_query(q)
print(df)