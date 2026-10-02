
from datetime import date

st.set_page_config(
    page_title="Mis periódicos",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# ESTILO RESPONSIVE: pensado primero para móvil
# ============================================================
st.markdown(
    """
    <style>
    .stApp {
        background: #eef0f4;
        position: relative;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        z-index: 0;
        background-image:
            linear-gradient(rgba(18,25,38,.48), rgba(18,25,38,.64)),
            url("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?auto=format&fit=crop&w=2200&q=80");
        background-size: cover;
        background-position: center;
        filter: blur(5px);
        transform: scale(1.04);
        pointer-events: none;
    }

    .stApp > * { position: relative; z-index: 1; }

    /* Dejamos la barra de Streamlit disponible para que el usuario
       siempre pueda recuperar la interfaz si alguna vez abre la sidebar. */
    header[data-testid="stHeader"] {
        background: rgba(12,16,24,.18) !important;
    }

    header[data-testid="stHeader"] button {
        color: white !important;
    }

    .block-container {
        max-width: 1180px;
        padding: 1.0rem 1.1rem 2.5rem 1.1rem;
    }

    /* Cabecera */
    .saludo {
        display: inline-block;
        max-width: 100%;
        box-sizing: border-box;
        font-size: 1.55rem;
        line-height: 1.25;
        font-weight: 800;
        color: #fff;
        background: rgba(16,22,34,.60);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,.16);
        border-radius: 18px;
        padding: 11px 16px;
        margin: .15rem 0 .35rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,.18);
    }

    .fecha {
        color: #f4f6f8;
        font-size: .98rem;
        font-weight: 600;
        margin: .1rem 0 .85rem .2rem;
        text-transform: capitalize;
        text-shadow: 0 1px 8px rgba(0,0,0,.35);
    }

    .titulo {
        font-size: 2.25rem;
        line-height: 1.1;
        font-weight: 850;
        color: #fff;
        text-shadow: 0 2px 14px rgba(0,0,0,.38);
        margin-bottom: .2rem;
    }

    .subtitulo {
        color: rgba(255,255,255,.9);
        font-size: 1rem;
        margin-bottom: .75rem;
        text-shadow: 0 1px 8px rgba(0,0,0,.3);
    }

    /* Filtro SIEMPRE accesible desde el contenido principal */
    div[data-testid="stExpander"] {
        background: rgba(255,255,255,.93) !important;
        border: 1px solid rgba(255,255,255,.8) !important;
        border-radius: 16px !important;
        box-shadow: 0 10px 28px rgba(0,0,0,.14);
        margin: .25rem 0 .9rem 0;
        overflow: hidden;
    }

    div[data-testid="stExpander"] summary {
        min-height: 52px;
    }

    /* Tarjetas responsive */
    .periodicos-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 16px;
        width: 100%;
        margin-top: .2rem;
    }

    .periodico-card {
        background: rgba(255,255,255,.95);
        border: 1px solid rgba(255,255,255,.75);
        border-radius: 20px;
        padding: 16px;
        min-height: 205px;
        box-sizing: border-box;
        box-shadow: 0 14px 35px rgba(0,0,0,.18);
        text-align: center;
    }

    .logo-wrap {
        height: 72px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 4px 0 7px 0;
    }

    .logo-wrap img {
        max-width: 165px;
        max-height: 62px;
        width: auto;
        height: auto;
        object-fit: contain;
    }

    .nombre-periodico {
        font-size: 1.08rem;
        line-height: 1.15;
        font-weight: 800;
        color: #20242d;
        margin: 3px 0 4px 0;
    }

    .categoria {
        color: #737985;
        font-size: .8rem;
        margin-bottom: 11px;
    }

    .pais-tag {
        display: inline-block;
        background: #eef1f5;
        color: #596273;
        border-radius: 999px;
        padding: 4px 9px;
        font-size: .7rem;
        font-weight: 700;
    }

    .boton {
        display: block;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 12px;
        border-radius: 12px;
        background: linear-gradient(135deg, #20242d, #394150);
        color: white !important;
        text-decoration: none !important;
        font-weight: 700;
        font-size: .92rem;
    }

    .contador {
        display: inline-block;
        color: #fff;
        background: rgba(16,22,34,.50);
        border: 1px solid rgba(255,255,255,.14);
        border-radius: 999px;
        padding: 6px 11px;
        font-size: .83rem;
        margin: 0 0 .75rem .1rem;
        backdrop-filter: blur(8px);
    }

    .sin-resultados {
        background: rgba(255,255,255,.94);
        border-radius: 18px;
        padding: 18px;
        color: #303641;
        box-shadow: 0 10px 25px rgba(0,0,0,.12);
        text-align: center;
    }

    @media (max-width: 700px) {
        .stApp::before {
            background-position: 62% center;
            filter: blur(4px);
        }

        .block-container {
            padding: .55rem .65rem 1.6rem .65rem;
        }

        .saludo {
            display: block;
            font-size: 1.18rem;
            line-height: 1.25;
            padding: 10px 12px;
            border-radius: 15px;
        }

        .fecha {
            font-size: .82rem;
            margin-bottom: .7rem;
        }

        .titulo {
            font-size: 1.72rem;
        }

        .subtitulo {
            font-size: .88rem;
            margin-bottom: .55rem;
        }

        div[data-testid="stExpander"] {
            margin-bottom: .75rem;
        }

        .periodicos-grid {
            grid-template-columns: 1fr;
            gap: 12px;
        }

        .periodico-card {
            min-height: 0;
            padding: 14px 12px 13px 12px;
            border-radius: 16px;
        }

        .logo-wrap {
            height: 62px;
        }

        .logo-wrap img {
            max-width: 145px;
            max-height: 54px;
        }

        .nombre-periodico {
            font-size: 1rem;
        }

        .categoria {
            font-size: .75rem;
            margin-bottom: 9px;
        }

        .boton {
            min-height: 42px;
            padding: 10px;
            font-size: .9rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CATÁLOGO
# ============================================================
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
    {"nombre":"EL CONFIDENCIAL", "categoria":"General", "pais":"España", "url":"https://www.elconfidencial.com/", "dominio":"elconfidencial.com"},
    {"nombre":"¡HOLA!", "categoria":"Corazón y entretenimiento", "pais":"España", "url":"https://www.hola.com/", "dominio":"hola.com"},
