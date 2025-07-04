import streamlit as st

st.set_page_config(
    page_title='Teams',
    page_icon='⚽',
    layout='wide'
)

df_data = st.session_state["data"]


#Filtrando pelos clubes e criando uma selectbox na sidebar
clubes = df_data['Club'].value_counts().index
clube=st.sidebar.selectbox('Clube',clubes)

df_filtered = df_data[(df_data["Club"]==clube)].set_index("Name")

st.image(df_filtered.iloc[0] ["Club Logo"])
st.markdown(f'## {clube}')

#Selecionando alguns itens do csv para serem apresentados do data frama e apresentando como parâmetro
columns = ['Age', 'Photo', 'Flag', 'Overall', 'Value(£)','Wage(£)', 'Joined', 'Height(cm.)', 'Weight(lbs.)', 'Contract Valid Until', 'Release Clause(£)' ]

#configurando algumas das colunas com alguns aspectos visuais diferentes
st.dataframe(df_filtered[columns],
    column_config={
        "Overall":st.column_config.ProgressColumn(format="%d"), 
        "Wage(£)":st.column_config.ProgressColumn(
            "Weekly Wage", 
            format="£%f",
            #Definindo máximo com base na maior remuneração semanal
            max_value=df_filtered["Wage(£)"].max()
        ),
        "Photo":st.column_config.ImageColumn(),
        "Flag":st.column_config.ImageColumn("Country"),
        

})
