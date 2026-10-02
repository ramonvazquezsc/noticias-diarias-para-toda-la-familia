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
# Periódicos
# -----------------------------
periodicos = [
    {
        "nombre": "MARCA",
        "categoria": "Deportes",
        "url": "https://www.marca.com/",
        "dominio": "marca.com",
    },
    {
        "nombre": "AS",
        "categoria": "Deportes",
        "url": "https://as.com/",
        "dominio": "as.com",
    },
    {
        "nombre": "Mundo Deportivo",
        "categoria": "Deportes",
        "url": "https://www.mundodeportivo.com/",
        "dominio": "mundodeportivo.com",
    },
    {
        "nombre": "SPORT",
        "categoria": "Deportes",
        "url": "https://www.sport.es/",
        "dominio": "sport.es",
    },
    {
        "nombre": "EL MUNDO",
        "categoria": "Información general",
        "url": "https://www.elmundo.es/",
        "dominio": "elmundo.es",
    },
    {
        "nombre": "EL PAÍS",
        "categoria": "Información general",
        "url": "https://elpais.com/",
        "dominio": "elpais.com",
    },
    {
        "nombre": "EXPANSIÓN",
        "categoria": "Economía",
        "url": "https://www.expansion.com/",
        "dominio": "expansion.com",
    },
    {
        "nombre": "EL CONFIDENCIAL",
        "categoria": "Información general y economía",
        "url": "https://www.elconfidencial.com/",
        "dominio": "elconfidencial.com",
    },
]

st.markdown('<div class="titulo">📰 Mis periódicos</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitulo">Acceso directo a tus diarios favoritos</div>',
    unsafe_allow_html=True,
)

# Dos columnas en escritorio y móvil. Cada tarjeta ocupa una columna.
cols = st.columns(2, gap="medium")

for i, p in enumerate(periodicos):
    with cols[i % 2]:
        # Favicon/logo del dominio. Se carga directamente desde Google.
        logo = f"https://www.google.com/s2/favicons?domain={p['dominio']}&sz=128"
        st.markdown(
            f"""
            <div class="periodico-card">
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

st.caption("Los enlaces llevan a las páginas web oficiales de cada medio.")
