import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

import plotly.express as px
import warnings

import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")
st.title(":blue[AIRBNB DATA ANALYSIS]")
st.write("")

def data():
    df= pd.read_csv("C:/Users/suhii/Downloads/Airbnb.csv")
    return df

df  = data()

with st.sidebar:
    select = option_menu("Main Menu",["Home","Data Exploration"])

if select == "Home":
    st.header(":blue[About Airbnb]")
    st.write("")
    st.write(''' :rainbow[***Airbnb is an online marketplace that connects people who want to rent out")
              their property with people who are looking for accommodations,
              typically for short stays. Airbnb offers hosts a relatively easy way to
              earn some income from their property.Guests often find that Airbnb rentals
              are cheaper and homier than hotels.***]''')
    st.write("")
    st.write(''':rainbow[***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                  The company provides a mobile application (app) that enables users to list,
                  discover, and book unique accommodations across the world.
                  The app allows hosts to list their properties for lease,
                  and enables guests to rent or lease on a short-term basis,
                  which includes vacation rentals, apartment rentals, homestays, castles,
                  tree houses and hotel rooms. The company has presence in China, India, Japan,
                  Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                  Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                  Airbnb is headquartered in San Francisco, California, the US.***]''')
    
if select == "Data Exploration":
    tab1,tab2 ,tab3 ,tab4, tab5 = st.tabs(["***PRICE ANALYSIS***",
                                           "***AVAILIBIBTY ANALYSIS***",
                                           "***LOCATION BASED ANALYSIS***",
                                           "***GEOSPATIAL VISUALIZATION***",
                                           "***TOP CHARTS***"])   
    with tab1:
        st.title("**PRICE**")
        col1,col2 = st.columns(2)

        with col1:

            country= st.selectbox("Select the Country",df["country"].unique())

            df1 = df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            beds = st.selectbox("Select the beds",df1["beds"].unique())
            
            df2 = df1[df1["beds"] == beds]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("price")[["beds","review_scores","bedrooms"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='beds', y= "price", title= "PRICE FOR BEDS",hover_data=["bedrooms","review_scores"],
                            color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)

        with col2:

            st.title("")
            st.write("")
            st.write("")
            st.write("")

            bed_room = st.selectbox("Select the Bed_rooms",df2["bedrooms"].unique())

            df3 = df[df["bedrooms"] == bed_room]
            df3.reset_index(drop=True, inplace = True)

            df_pie = pd.DataFrame(df3.groupby("price")[["beds","review_scores"]].sum()) 
            df_pie.reset_index(inplace=True)

            fig_p = px.pie(df_pie, values="price",names="beds",
                           hover_data=["beds"],
                            
                            color_discrete_sequence= px.colors.sequential.Plasma,
                            title="PRICE DIFFERENCE BASED ON BEDROOMS",
                            width= 600, height= 500)
            st.plotly_chart(fig_p)

    with tab2:
        
        st.title("**AVAILIBIBTY ANALYSIS**")
        col1,col2 = st.columns(2)

        with col1:
             
            country_a = st.selectbox("Select the Country_a",df["country"].unique())

            df1_a= df[df["country"] == country_a]
            df1_a.reset_index(drop= True, inplace= True)

            price_p= st.selectbox("Select the price Type",df1_a["price"].unique())
            
            df2_a= df1_a[df1_a["price"] == price_p]
            df2_a.reset_index(drop= True, inplace= True)

            df_a_s = px.sunburst(df2_a, path=["beds","bedrooms","country"], values="availability_30",
                                       width=900,height=600,title="Availability_30",
                                       color_discrete_sequence=px.colors.sequential.Plasma)
            st.plotly_chart(df_a_s)

        with col2:
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            

            df_a_sunb_60= px.sunburst(df2_a, path=["beds","bedrooms","country"], values="availability_60",
                                      width=900,height=600,title="Availability_60",
                                      color_discrete_sequence=px.colors.sequential.Blues_r)
            st.plotly_chart(df_a_sunb_60)

        col1,col2= st.columns(2)

        with col1:
            
            df_a_sunb_90 = px.sunburst(df2_a, path=["beds","bedrooms","country"], values="availability_90",
                                      width=900,height=600,title="Availability_90",
                                       color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
            st.plotly_chart(df_a_sunb_90)

        with col2:

            df_365= px.sunburst(df2_a, path=["beds","bedrooms","country"],
                                       values="availability_365",
                                       width=900,height=600,title="Availability_365",
                                       color_discrete_sequence=px.colors.sequential.Greens_r)
            st.plotly_chart(df_365)
    
    with tab3:

        st.title("**LOCATION BASED ANALYSIS**")
        st.write("")


        country_l= st.selectbox("Select the Country_l",df["country"].unique())

        df1_l= df[df["country"] == country_l]
        df1_l.reset_index(drop= True, inplace= True)

        beds_ty= st.selectbox("Select the BEDS",df1_l["beds"].unique())

        df2_l= df1_l[df1_l["beds"] == beds_ty]
        df2_l.reset_index(drop= True, inplace= True)

        st.write("")

        dfl = pd.DataFrame(df.groupby("beds")[["price","bedrooms","beds","amenities"]].sum())
        df.reset_index(inplace= True)

        fig_1= px.bar(df, x="beds", y= ["price","bedrooms","beds","amenities"], title="Amenities",
                    hover_data= "amenities", barmode='group',
                    color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_1)


        room_ty_l= st.selectbox("Select the bedrooms", df["bedrooms"].unique())

        df_val_sel_rt= df[df["bedrooms"] == room_ty_l]

        fig_2= px.bar(df_val_sel_rt, x= ["host_id","host_name"],
                      y="host_neighbourhood", title="Host_Neighbourhood",
                    hover_data= ["name","host_name"], 
                    barmode='group',orientation='h',
                      color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_2)

        fig_3= px.bar(df_val_sel_rt, x="host_name", y= ["host_neighbourhood","host_name"], title="Host_Name",
                    hover_data= ["price","country"],
                      barmode='group', 
                      color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
        st.plotly_chart(fig_3)

    with tab4:

        st.title("**GEOSPATIAL VISUALIZATION**")
        st.write("")

        fig_map = px.scatter_mapbox(df, lat="Latitude" , lon="Longitude", color="price",
                                    size="price",color_continuous_scale="Inferno",
                                    hover_name="name",
                                    range_color=(0,49000),mapbox_style="carto-positron",
                                    zoom=1)
        fig_map.update_layout(width = 1150,height=800,title="Geospatial Distribution of Listings")
        st.plotly_chart(fig_map)


    with tab5:

        country_t= st.selectbox("Select the Country_t",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        bedr = st.selectbox("Select the price",df1_t["bedrooms"].unique())

        df2_t= df1_t[df1_t["bedrooms"] == bedr]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="bedrooms")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price = px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                               color="Total_price",title= "PRICE BASED ON HOST_NEIGHBOURHOOD",
                                 width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2 = px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                 color="Avarage_price",
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)
    


