# Copyright (c) 2024 Snowflake Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import streamlit as st
import pandas as pd
import numpy as np
from snowflake.snowpark.context import get_active_session

st.title (" Hello Streamlit App :wave:")
session = get_active_session() 

##-- Form

with st.form("Input Form"):
    st.header("Partner details Input Form")
    input_fld1 = st.text_input("Partner Name")
    input_fld2 = st.text_input("Partner Description")
 

    submitted = st.form_submit_button("Submit!")

if submitted:
    st.write(input_fld1)
    st.write(input_fld2)


    sql = f"INSERT INTO BI_DB.REPORTS.PARTNER_INFO(PARTNER_NAME,PARTNER_DESCRIPTION) VALUES ('{input_fld1}','{input_fld2}')"

    session.sql(sql).collect()
    st.success('Success!', icon="✅")
    
    df_comments = session.sql("select * from BI_DB.REPORTS.PARTNER_INFO").to_pandas()
    st.dataframe(df_comments, use_container_width=True)
    