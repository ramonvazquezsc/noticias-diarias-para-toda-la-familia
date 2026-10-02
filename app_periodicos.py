import streamlit as st

st.set_page_config(
    page_title="Mis periódicos",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Estilo móvil
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: #f4f5f8;
    }

    /* Oculta la barra superior de Streamlit para aprovechar toda la pantalla */
    header[data-testid="stHeader"] {
        display: none;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 1.0rem;
        padding-bottom: 2rem;
    }

    .saludo {
        font-size: 1.65rem;
        font-weight: 750;
        color: #20242d;
        margin-bottom: .15rem;
    }

    .fecha {
        color: #6b7280;
        font-size: .98rem;
        margin-bottom: 1rem;
        text-transform: capitalize;
    }

    .titulo {
        font-size: 2.1rem;
        font-weight: 750;
        color: #20242d;
        margin-bottom: .2rem;
    }

    .subtitulo {
        color: #6b7280;
        font-size: 1rem;
        margin-bottom: 1.2rem;
    }

    .periodico-card {
        background: white;
        border: 1px solid #e2e5ea;
        border-radius: 18px;
        padding: 18px 16px 16px 16px;
        min-height: 205px;
        box-shadow: 0 2px 8px rgba(0,0,0,.05);
        margin-bottom: 12px;
        text-align: center;
    }

    .logo-wrap {
        height: 82px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 8px;
    }

    .logo-wrap img {
        max-width: 170px;
        max-height: 72px;
        object-fit: contain;
    }

    .nombre-periodico {
        font-size: 1.08rem;
        font-weight: 700;
        color: #20242d;
        margin: 4px 0 2px 0;
    }

    .categoria {
        color: #737985;
        font-size: .82rem;
        margin-bottom: 13px;
    }

    .pais-tag {
        display: inline-block;
        background: #f0f2f5;
        color: #626a76;
        border-radius: 999px;
        padding: 3px 9px;
        font-size: .72rem;
        margin-bottom: 5px;
    }

    .contador {
        color: #6b7280;
        font-size: .84rem;
        margin: 0 0 .8rem .1rem;
    }

    .boton {
        display: inline-block;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 12px;
        border-radius: 10px;
        background: #20242d;
        color: white !important;
        text-decoration: none !important;
        font-weight: 650;
        font-size: .94rem;
    }

    .boton:hover {
        background: #111318;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: .8rem .7rem 1.5rem .7rem;
        }

        .saludo {
            font-size: 1.35rem;
            line-height: 1.25;
        }

        .fecha {
            font-size: .88rem;
            margin-bottom: .8rem;
        }

        .titulo {
            font-size: 1.75rem;
        }

        .subtitulo {
            font-size: .92rem;
            margin-bottom: .9rem;
        }

        .periodico-card {
            min-height: 185px;
            padding: 14px 12px 13px 12px;
            border-radius: 15px;
        }

        .logo-wrap {
            height: 65px;
        }

        .logo-wrap img {
            max-width: 145px;
            max-height: 58px;
        }

        .nombre-periodico {
            font-size: .98rem;
        }

        .categoria {
            font-size: .76rem;
        }

        .boton {
            font-size: .9rem;
            padding: 9px 10px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Catálogo de prensa
# -----------------------------
periodicos = [
    # ESPAÑA
    {"nombre":"MARCA", "categoria":"Deportes", "pais":"España", "url":"https://www.marca.com/", "dominio":"marca.com"},
    {"nombre":"AS", "categoria":"Deportes", "pais":"España", "url":"https://as.com/", "dominio":"as.com"},
    {"nombre":"Mundo Deportivo", "categoria":"Deportes", "pais":"España", "url":"https://www.mundodeportivo.com/", "dominio":"mundodeportivo.com"},
    {"nombre":"SPORT", "categoria":"Deportes", "pais":"España", "url":"https://www.sport.es/", "dominio":"sport.es"},
    {"nombre":"EL MUNDO", "categoria":"General", "pais":"España", "url":"https://www.elmundo.es/", "dominio":"elmundo.es"},
    {"nombre":"EL PAÍS", "categoria":"General", "pais":"España", "url":"https://elpais.com/", "dominio":"elpais.com"},
    {"nombre":"ABC", "categoria":"General", "pais":"España", "url":"https://www.abc.es/", "dominio":"abc.es"},
    {"nombre":"La Vanguardia", "categoria":"General", "pais":"España", "url":"https://www.lavanguardia.com/", "dominio":"lavanguardia.com"},
    {"nombre":"20minutos", "categoria":"General", "pais":"España", "url":"https://www.20minutos.es/", "dominio":"20minutos.es"},
    {"nombre":"La Razón", "categoria":"Política y actualidad", "pais":"España", "url":"https://www.larazon.es/", "dominio":"larazon.es"},
    {"nombre":"Público", "categoria":"Política y actualidad", "pais":"España", "url":"https://www.publico.es/", "dominio":"publico.es"},
    {"nombre":"EXPANSIÓN", "categoria":"Economía", "pais":"España", "url":"https://www.expansion.com/", "dominio":"expansion.com"},
    {"nombre":"Cinco Días", "categoria":"Economía", "pais":"España", "url":"https://cincodias.elpais.com/", "dominio":"cincodias.elpais.com"},
    {"nombre":"elEconomista", "categoria":"Economía", "pais":"España", "url":"https://www.eleconomista.es/", "dominio":"eleconomista.es"},
    {"nombre":"EL CONFIDENCIAL", "categoria":"Economía y actualidad", "pais":"España", "url":"https://www.elconfidencial.com/", "dominio":"elconfidencial.com"},
    {"nombre":"¡HOLA!", "categoria":"Corazón y entretenimiento", "pais":"España", "url":"https://www.hola.com/", "dominio":"hola.com"},
    {"nombre":"Diez Minutos", "categoria":"Corazón y entretenimiento", "pais":"España", "url":"https://www.diezminutos.es/", "dominio":"diezminutos.es"},
    {"nombre":"Lecturas", "categoria":"Corazón y entretenimiento", "pais":"España", "url":"https://www.lecturas.com/", "dominio":"lecturas.com"},
    {"nombre":"Semana", "categoria":"Corazón y entretenimiento", "pais":"España", "url":"https://www.semana.es/", "dominio":"semana.es"},

    # PORTUGAL
    {"nombre":"Público", "categoria":"General", "pais":"Portugal", "url":"https://www.publico.pt/", "dominio":"publico.pt"},
    {"nombre":"Expresso", "categoria":"Política y actualidad", "pais":"Portugal", "url":"https://expresso.pt/", "dominio":"expresso.pt"},
    {"nombre":"Observador", "categoria":"Política y actualidad", "pais":"Portugal", "url":"https://observador.pt/", "dominio":"observador.pt"},
    {"nombre":"Jornal de Notícias", "categoria":"General", "pais":"Portugal", "url":"https://www.jn.pt/", "dominio":"jn.pt"},
    {"nombre":"Diário de Notícias", "categoria":"General", "pais":"Portugal", "url":"https://www.dn.pt/", "dominio":"dn.pt"},
    {"nombre":"Jornal de Negócios", "categoria":"Economía", "pais":"Portugal", "url":"https://www.jornaldenegocios.pt/", "dominio":"jornaldenegocios.pt"},
    {"nombre":"A Bola", "categoria":"Deportes", "pais":"Portugal", "url":"https://www.abola.pt/", "dominio":"abola.pt"},
    {"nombre":"Record", "categoria":"Deportes", "pais":"Portugal", "url":"https://www.record.pt/", "dominio":"record.pt"},

    # REINO UNIDO
    {"nombre":"BBC News", "categoria":"General", "pais":"Reino Unido", "url":"https://www.bbc.com/news", "dominio":"bbc.com"},
    {"nombre":"The Guardian", "categoria":"General", "pais":"Reino Unido", "url":"https://www.theguardian.com/uk", "dominio":"theguardian.com"},
    {"nombre":"The Telegraph", "categoria":"Política y actualidad", "pais":"Reino Unido", "url":"https://www.telegraph.co.uk/", "dominio":"telegraph.co.uk"},
    {"nombre":"Financial Times", "categoria":"Economía", "pais":"Reino Unido", "url":"https://www.ft.com/", "dominio":"ft.com"},
    {"nombre":"The Times", "categoria":"General", "pais":"Reino Unido", "url":"https://www.thetimes.com/", "dominio":"thetimes.com"},
    {"nombre":"The Independent", "categoria":"General", "pais":"Reino Unido", "url":"https://www.independent.co.uk/", "dominio":"independent.co.uk"},

    # ESTADOS UNIDOS
    {"nombre":"The New York Times", "categoria":"General", "pais":"Estados Unidos", "url":"https://www.nytimes.com/", "dominio":"nytimes.com"},
    {"nombre":"The Washington Post", "categoria":"Política y actualidad", "pais":"Estados Unidos", "url":"https://www.washingtonpost.com/", "dominio":"washingtonpost.com"},
    {"nombre":"The Wall Street Journal", "categoria":"Economía", "pais":"Estados Unidos", "url":"https://www.wsj.com/", "dominio":"wsj.com"},
    {"nombre":"USA Today", "categoria":"General", "pais":"Estados Unidos", "url":"https://www.usatoday.com/", "dominio":"usatoday.com"},
    {"nombre":"Los Angeles Times", "categoria":"General", "pais":"Estados Unidos", "url":"https://www.latimes.com/", "dominio":"latimes.com"},
    {"nombre":"The Washington Times", "categoria":"Política y actualidad", "pais":"Estados Unidos", "url":"https://www.washingtontimes.com/", "dominio":"washingtontimes.com"},

    # BRASIL
    {"nombre":"Folha de S.Paulo", "categoria":"General", "pais":"Brasil", "url":"https://www.folha.uol.com.br/", "dominio":"folha.uol.com.br"},
    {"nombre":"O Globo", "categoria":"General", "pais":"Brasil", "url":"https://oglobo.globo.com/", "dominio":"oglobo.globo.com"},
    {"nombre":"Estadão", "categoria":"General", "pais":"Brasil", "url":"https://www.estadao.com.br/", "dominio":"estadao.com.br"},
    {"nombre":"Valor Econômico", "categoria":"Economía", "pais":"Brasil", "url":"https://valor.globo.com/", "dominio":"valor.globo.com"},
    {"nombre":"Lance!", "categoria":"Deportes", "pais":"Brasil", "url":"https://www.lance.com.br/", "dominio":"lance.com.br"},
]

# -----------------------------
# Filtros
# -----------------------------
if "f_paises_prensa" not in st.session_state:
    st.session_state.f_paises_prensa = sorted({p["pais"] for p in periodicos})
if "f_categorias_prensa" not in st.session_state:
    st.session_state.f_categorias_prensa = sorted({p["categoria"] for p in periodicos})

with st.sidebar:
    st.markdown("## 📰 Filtros")
    st.caption("Elige qué prensa quieres ver")
    paises = sorted({p["pais"] for p in periodicos})
    categorias = sorted({p["categoria"] for p in periodicos})

    seleccion_paises = st.multiselect(
        "País",
        paises,
        default=st.session_state.f_paises_prensa,
        key="selector_paises_prensa",
    )
    seleccion_categorias = st.multiselect(
        "Tipo de prensa",
        categorias,
        default=st.session_state.f_categorias_prensa,
        key="selector_categorias_prensa",
    )

    st.divider()
    if st.button("Mostrar todos", use_container_width=True):
        st.session_state.f_paises_prensa = paises
        st.session_state.f_categorias_prensa = categorias
        st.rerun()

    if st.button("Limpiar filtros", use_container_width=True):
        st.session_state.f_paises_prensa = []
        st.session_state.f_categorias_prensa = []
        st.rerun()

filtrados = [
    p for p in periodicos
    if p["pais"] in seleccion_paises and p["categoria"] in seleccion_categorias
]

# -----------------------------
# Cabecera dinámica
# -----------------------------
from datetime import date

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
hoy = date.today()
fecha_hoy = f"{DIAS[hoy.weekday()]}, {hoy.day} de {MESES[hoy.month - 1]} de {hoy.year}"

st.markdown(
    f'<div class="saludo">Hola Moncho, tu prensa diaria te está esperando</div>',
    unsafe_allow_html=True,
)
st.markdown(
    f'<div class="fecha">{fecha_hoy}</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="titulo">📰 Mis periódicos</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitulo">Acceso directo a tu prensa favorita</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="contador">{len(filtrados)} publicaciones disponibles</div>',
    unsafe_allow_html=True,
)

# -----------------------------
# Tarjetas
# -----------------------------
if not filtrados:
    st.info("No hay periódicos que coincidan con los filtros seleccionados. Abre la barra lateral y cambia la selección.")
else:
    cols = st.columns(2, gap="medium")
    for i, p in enumerate(filtrados):
        with cols[i % 2]:
            logo = f"https://www.google.com/s2/favicons?domain={p['dominio']}&sz=128"
            st.markdown(
                f"""
                <div class="periodico-card">
                    <div class="pais-tag">{p['pais']}</div>
                    <div class="logo-wrap">
                        <img src="{logo}" alt="Logo de {p['nombre']}" loading="lazy">
                    </div>
                    <div class="nombre-periodico">{p['nombre']}</div>
                    <div class="categoria">{p['categoria']}</div>
                    <a class="boton" href="{p['url']}" target="_blank" rel="noopener noreferrer">
                        Abrir periódico
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.caption("Los enlaces llevan a las páginas web oficiales de cada medio. La clasificación es una categorización práctica por temática principal.")


