import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Home',
    page_icon='🏠',
)


if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data=df_data[df_data['Contract Valid Until']>=2023]
    df_data=df_data[df_data['Value(£)']>0]
    df_data=df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data']=df_data
    


st.markdown('# FIFA23 OFFICIAL DATASET! ⚽')

st.sidebar.markdown('Desenvolvido por [creb](https://github.com/CalebMarins)')

btn = st.link_button("Acesse os dados do Kaggle", 'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    '''
    O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, estatísticas do jogo, detalhes do contrato e afiliações de clubes.

    Com **mais de 17mil registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos de jogadroes, métricas de desempenho, avaliação de mercado, análises de clubes, posicionamento de jogadores e desenvolvimento do jogador ao longo do tempo.
    '''
)
