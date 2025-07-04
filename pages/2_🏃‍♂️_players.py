import streamlit as st

st.set_page_config(
    page_title='Players',
    page_icon='🏃‍♂️',
    layout='wide'
)

df_data = st.session_state['data']

#Filtrando pelos clubes e criando uma selectbox na sidebar
clubes = df_data['Club'].value_counts().index
clube=st.sidebar.selectbox('Clube',clubes)
df_players = df_data[(df_data['Club']==clube)]

#aplicando o mesmo fitro para os jogadores de cada clube.
players = df_players['Name'].unique()
player=st.sidebar.selectbox('Jogador',players)

player_stats=df_data[df_data['Name']==player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

col1,col2,col3 =st.columns(3)
col1.markdown(f"**Clube:** {player_stats['Club']}")
col2.markdown(f"**Pé dominante:** {player_stats['Preferred Foot']}")
col3.markdown(f"**Posição:** {player_stats['Position']}")



col1,col2,col3 =st.columns(3)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
#formatação :.2f para ficar apenas com 2 casas decimais
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"**Overall:** {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1,col2,col3 =st.columns(3)
col1.metric(label="Valor de Mercado:", value=f"£{player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal:", value=f"£{player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de recisão:", value=f"£{player_stats['Release Clause(£)']:,}")
