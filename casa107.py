import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Título de la aplicación y configuración de la página
st.set_page_config(
    page_title="Control Ciudadano Condominio",
    page_icon="🏢",
    layout="wide"
)

# --- CABECERA Y SALUDO (TONO CONSERVADO SEGÚN SOLICITUD DEL USUARIO) ---
st.title("🏡Análisis de Gestión y Finanzas")

st.markdown("""
Nos dirigimos a ustedes para compartir un **análisis** sobre la gestión dentro de la Privada Parma.

La preocupación central, y la más grave, es la persistente **ausencia de la Asociación Civil (AC)** legalmente constituida para la Mesa Directiva. 
""")
st.warning('Como resultado, de acuerdo a las reglas del desarrollador **hemos perdido el Fondo Convive**.', icon="🛑")
            
st.markdown("""La cuenta bancaria de la Privada Parma, cuyo saldo ha crecido considerablemente, permanece bajo la **titularidad exclusiva de la Administración**—cuya gestión, cabe destacar, ha 'brillado' por su opacidad e irregularidades. 
""")
st.warning('Esto nos expone a un riesgo inaceptable de pérdida total del capital.', icon="🛑")
st.markdown("""Se realizó un análisis de los Estados Financieros y de comentarios recabados de varios vecinos, con el propósito de presentar una **evaluación objetiva** de la gestión administrativa y financiera reciente, centrando en las **desviaciones legales y normativas** y las **inconsistencias operativas** en la Privada Parma.
""")

st.markdown("""
**Nota de Metodología:** La totalidad de los datos e información financiera citada en este informe ha sido extraída de la sección *Documentos → Estados Financieros* de la plataforma administrativa **Neivor** con los Estados Financieros de Enero 2024 a Junio 2025 que es lo que se cuenta.""")

# --- 1. RESERVA PATRIMONIAL ---
with st.expander("💰 Análisis de la Reserva Patrimonial y la Revaluación de la Cuota"):
    st.markdown(f"""
    * **Crecimiento de Capital:** Se documenta un crecimiento constante en el saldo de las cuentas, con una acumulación promedio mensual de aproximadamente **$35,000** desde octubre de 2024.
    * Se considera que el nivel actual de capitalización de reserva **obliga a una revisión del pago mensual de la cuota de mantenimiento**. Se exige la presentación formal de un plan de inversión o una justificación presupuestaria específica que demuestre la necesidad de mantener este superávit de capital no programado. 
    """)
    st.warning('Este excedente representa un **ahorro estimado de $280** por propietario al mes tomando en cuenta la media de gastos fijos de Diciembre 2024 a Junio 2025,', icon="🛑")
    st.markdown("""
    **Adicionalmente, se requiere que la nueva estructura de cuotas asegure que el pago mensual no sea utilizado para cubrir los adeudos o impagos de aquellos vecinos que presenten morosidad ya que el capital excedente debe cubrir casos extraordinarios unicamente, manteniendo una estricta separación entre la tesorería operativa y la gestión de cobranza.**
    """)

    # Datos proporcionados por el usuario
    data = {
        'report_date': ['30/09/24','31/10/24', '30/11/24', '31/12/24', '31/01/25', '28/02/25', '31/03/25', '30/04/25', '31/05/25'],
        'total_incomes': [199110.73, 98953.00, 135121.00, 84747.50, 99044.50, 103502.91, 95864.81, 91449.99, 109351.66],
        'ending_balance': [125816.38, 178279.38, 223518.38, 247926.88, 270112.87, 301470.79, 333063.10, 353948.09, 338189.75]
    }
    df = pd.DataFrame(data)
    # Convertir a datetime
    df['report_date'] = pd.to_datetime(df['report_date'], format='%d/%m/%y')

    # La función de formateo para números con dos decimales y separador de miles
    def format_currency(x):
        return f'{x:,.2f}'

    # --- CREACIÓN DEL GRÁFICO COMBINADO CON UN SOLO EJE Y ---
    # Nota: Inicializamos make_subplots SIN secondary_y=True, o simplemente usamos go.Figure()
    fig_combined = go.Figure()

    # 1. Agregar la Gráfica de Barras (Saldo Final - Eje Y Único)
    fig_combined.add_trace(
        go.Bar(
            x=df['report_date'],
            y=df['ending_balance'],
            marker_color='rgba(230, 126, 34, 0.7)', # Naranja para Saldo
            opacity=0.8,
            name='Saldo Final (Mensual)',
            # MOSTRAR DATOS EN BARRAS (Saldo)
            text=df['ending_balance'].apply(format_currency), 
            textposition='outside' 
        )
    )

    # 2. Agregar la Gráfica de Línea (Ingresos Totales - Eje Y Único)
    fig_combined.add_trace(
        go.Scatter(
            x=df['report_date'],
            y=df['total_incomes'],
            mode='lines+markers+text', # Se añade 'text' al modo
            line=dict(color='rgba(46, 204, 113, 1)', width=3), # Verde para Ingresos
            marker=dict(size=7),
            name='Ingresos Totales (Mensual)',
            # MOSTRAR DATOS EN PUNTOS (Ingresos)
            text=df['total_incomes'].apply(format_currency),
            textposition='top center' # Coloca el texto encima del punto
        )
    )

    # 3. Actualizar el diseño y los títulos de los ejes
    fig_combined.update_layout(
        title_text='Flujo de Ingresos (Línea) y Saldo Acumulado (Barras)',
        height=500, 
        margin=dict(l=20, r=20, t=50, b=20),
        hovermode="x unified",
        # Definimos el título del único Eje Y
        yaxis_title="<b>Monto Total ($)</b>", 
        yaxis=dict(tickformat="$,.0f") # Formato de moneda para el eje Y
    )

    # Configurar el Eje X
    fig_combined.update_xaxes(
        title_text="Fecha de Reporte"
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_combined, use_container_width=True)

# --- 2. ASOCIACIÓN CIVIL ---
with st.expander("🐢 Revisión de Plazos y Presupuesto para la Asociación Civil (AC)"):
    st.markdown(f"""
    * **Perdida Fondo Convive:** La demora de más de quince (15) meses por parte de la Mesa Directiva en la constitución de la Asociación Civil (AC), atribuida a normativas internas del desarrollador, resulta en la **pérdida de acceso al Fondo Convive**. Debemos estar felices de perder ese fondo. Lo mejor es seguir pagando de más cuotas mensuales y tener cuotas extraordinarias.
    """)
    st.warning('Esta situación implica la lamentable renuncia a un recurso de 265,000.00 pesos destinado a mejoras en nuestra privada.', icon="⚠️")
    st.markdown("""* **Discrepancia Presupuestaria:** El capital solicitado hasta el momento ha sido de **76,827.86 pesos** para la creación de la AC. Dado que los costos notariales promedio son de 15,000.00 pesos, se requiere la **desagregación detallada y justificación** de los más de **$60,000 adicionales** solicitados, así como el cronograma de trabajo para finalizar el trámite.
    """)

# --- 8. RIESGO FIDUCIARIO ---
with st.expander("⚠️ Riesgo Fiduciario por Estructura de Titularidad de Cuentas"):
    st.markdown("""
    * **Titularidad a Nombre de Tercero:** Los fondos del condominio están, por decisión administrativa, a nombre de la **Administración** (un tercero).
    * **Riesgo Declarado:** Un vecino documentó la declaración de La Mesa Directiva  sugiriendo que la Administración **"buscaría perjudicarnos"** en caso de conflicto. Mantener los activos bajo la titularidad de un tercero con un riesgo de conflicto declarado es una violación de la **sana gestión** y expone innecesariamente el patrimonio de los propietarios.
    """)

# --- 3. CONTRATO DE ADMINISTRACIÓN ---
with st.expander("📜 Inconsistencia en la Justificación de la Continuidad del Contrato de Administración"):
    st.markdown("""
    Se han proporcionado **justificaciones inconsistentes** sobre la imposibilidad de sustituir al actual proveedor de Administración:

    * **Contrato Inaccesible:** Se invocó una **cláusula contractual** como impedimento para el cambio. No obstante, el documento contractual clave para la toma de decisiones es **ilocalizable** por el Consejo, quedando bajo la custodia exclusiva de la Administración.
    * **Asociación Civil (AC) Pendiente:** Minutos después, se modificó la justificación, indicando que la falta de constitución de la AC es el factor que impide la contratación de un nuevo proveedor.

    La contradicción entre ambas justificaciones, sumada al contrato no disponible y la demora de **más de quince meses** en la constitución de la AC, sugiere una **inmovilidad administrativa** en el proceso de evaluación y cambio.
                
    Un interesado ha intentado rastrear el contrato, en Ruba solo existe un contrato ya expirado con el cual la administración se intenta amparar.
                
    **¿Ustedes permitirían que el  prestador de servicios sea el único que posea el contrato? Bastante ventajoso de su parte.**
    """)

# --- 5. NUEVA SECCIÓN: COBROS, MORA E INCONSISTENCIAS ---
with st.expander("5. ⚠️ Discrepancias en Cobros, Mora y Conciliación de Saldos en Plataforma Neivor y Estados financieros"):

    st.markdown("""
    Se han detectado **inconsistencias  recurrentes** en la conciliación de los balances financieros. Por lo que se solicita una clarificación y justificación inmediata sobre los siguientes movimientos y saldos reportados en los Estados Financieros, que no son los únicos bajo escrutinio:
    * **La cuenta de Banjio donde se tiene el capital de la Privada Parma no cumple con la Ley de Condominios**, se pide esclarecer este cambio de cuenta ya que la cuenta anterior en Inbursa si cumplía.
    * **Traspaso por Cambio de Cuenta (Sep 2024):** En el reporte de gastos variables de Septiembre 2024, se registra el concepto **"Traspaso por cambio de cuenta"** por **$8,384.24** como un egreso. Se requiere aclarar esta anotación, ya que el proceso de cambio de cuenta (de Inbursa a Banregio) se gestionó realizando gastos desde la cuenta antigua (Inbursa) mientras los nuevos depósitos se dirigían a la cuenta nueva (Banregio). El concepto de "traspaso" por ese monto como **"gasto"** necesita ser justificado. Por cierto, el poco dinero sobrante de la cuenta anterior no fue usado completamente y 'maquillo' para que los Estados Financieros cuadren, les cobraron el Traspaso y se quedaron con su dinero 😂.

    * **Conciliación de Saldos (Ago/Oct 2024 y Abril 2045):** Se han detectado discrepancias en la conciliación de saldos iniciales y finales reportados en los Estados Financieros de **Agosto a Septiembre 2024**, de **Septiembre a Octubre 2024** y de **Marzo a Abril 2025**. Los saldos iniciales de un mes no coinciden con los saldos finales del mes anterior, lo que indica un error fundamental en la cuadratura de los informes.

    * **Doble Asiento de Jardinería:** Se exige la aclaración del concepto **"DEVOLUCION DE PAGO JARDINERA"** en Noviembre 2024, que figura simultáneamente como **ingreso y egreso** en el mismo periodo. Esta transacción coexiste con otro egreso bajo el concepto **"JARDINERIA"**, lo que complica la trazabilidad del gasto real y exige la presentación de documentación de respaldo.

    * **Falta de Información Completa:** Se reitera la necesidad de obtener el **Estado Financiero Completo de Octubre 2024** y los Estados Financieros de Julio 2025 a la fecha para realizar la auditoría de estos periodos.
    """)

    st.image("Jardineria.jpeg", caption="Conceptos de Jardinería")

    st.divider()
    st.markdown("""
    Se han identificado graves inconsistencias entre los cargos reflejados en la plataforma de cobro **Neivor** y los Estados Financieros oficiales, lo que compromete la exactitud del saldo real del condominio.

    * **Inconsistencia entre Neivor y Estados Financieros:** Se ha descubierto que los montos de cobro registrados en la aplicación **Neivor** no cuadran de forma consistente con los reportes de los **Estados Financieros**. Esta disparidad es crítica, ya que sugiere que el dinero recaudado a través del sistema de cobros podría no estar siendo contabilizado completamente en las cuentas formales.
    """)
    st.warning('Lo que representa un riesgo grave de **pérdida o desvío de capital.**', icon="⚠️")
    st.markdown("""
    * **Variabilidad Injustificada en Cuotas:** Los cobros por cada concepto en la aplicación Neivor varían sin justificación aparente mes a mes, y se han encontrado diferencias en las cuotas aplicadas entre vecinos para los mismos conceptos. Esta inconsistencia operativa viola el principio de equidad y estandarización en la recaudación de mantenimiento.
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.image("estado_neivor_1.jpeg", caption="Inconsistencia contable, el cobro por el concepto Seguridad es diferente a otros vecinos")
    with col2:
        st.image("estado_neivor_2.jpeg", caption="Inconsistencia contable, el cobro por el concepto Seguridad es diferente a otros vecinos y los cobros son diferentes")


# --- 4. MANEJO FINANCIERO Y DIVULGACIÓN ---
with st.expander("💸 El dinero se va volando con decisiones poco claras"):
    st.markdown("""
    * **Justifiación del costo de servicio:** Durante el presente año, y a pesar de una notable deficiencia en la prestación de servicios, se ha autorizado un incremento superior al 78% en el costo de los mismos. El interrogante que se plantea es el siguiente: ¿Se ha observado una mejora en la calidad del servicio? Los puntos pendientes de cumplimiento solo comenzaron a ser atendidos tras la exigencia de convocar a una asamblea, que por cierto, tomó más de un mes la solicitud de asamblea.
    ### Evolución del Gasto de Administración (Incremento del 78%)
    """)

    
# Datos de gastos de administración proporcionados por el usuario
    admon_data = {
        'report_date': ['30/11/23', '31/1/24', '29/2/24', '31/3/24', '30/4/24', '31/5/24', '30/6/24', '31/07/24', '31/08/24', '30/09/24', '31/10/24', '30/11/24', '31/12/24', '31/01/25', '28/02/25', '31/03/25', '30/04/25', '31/05/25'],
        'admon_expenses': [0.00, 0.00, 2637.21, 2176.26, 3321.66, 9960.00, 5268.84, 5669.73, 8863.50, 5841.54, 5841.54, 5898.81, 5953.35, 10455.00, 10600.00, 10600.00, 10600.00, 10600.00]
    }
    df_admon = pd.DataFrame(admon_data)
    # Convertir a datetime.
    df_admon['report_date'] = pd.to_datetime(df_admon['report_date'], format='%d/%m/%y')

    # Gráfico de Barras para Gastos de Administración
    fig_admon_expenses = go.Figure()
    fig_admon_expenses.add_trace(go.Bar(
        x=df_admon['report_date'],
        y=df_admon['admon_expenses'],
        marker_color='rgba(192, 57, 43, 0.9)', # Rojo para gastos
        opacity=0.9,
        name='Gasto de Administración',
        # --- CAMBIOS CLAVE AQUÍ ---
        text=df_admon['admon_expenses'].apply(lambda x: f'{x:,.2f}'), # Formatea los números con 2 decimales y separador de miles
        textposition='outside' # Coloca el texto fuera de la barra (arriba)
        # --------------------------
    ))
    fig_admon_expenses.update_layout(
        title_text='Gasto de Administración Mensual (Se observa el aumento del 60%)',
        xaxis_title='Fecha de Reporte',
        yaxis_title='Monto ($)',
        height=400,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig_admon_expenses, use_container_width=True)

# --- 7. SERVICIO DE PORTERÍA Y VIGILANCIA ---
with st.expander("👥 Evaluación del Servicio de Portería"):
    st.markdown("""
    * **Incremento Tarifario No Vinculado al Servicio:** Se confirmó durante asamblea que el servicio de portería entregado fue  **incompleto** durante un periodo de "demo". Cinco meses después de empezar a prestar servicios y con meses de servicio incompletos, se aplicó un ajuste de precio por **"inflación"**. El incremento tarifario desvinculado de la calidad del servicio previamente reconocido como deficiente es una **decisión financiera que requiere ser justificada**.
    * **Vigilancia y Rondines:** La ausencia de la cuatrimoto que fue ofrecida desde un inicio fue justificada por la presencia de **"un vehículo de supervisión para pasar lista"**. Esta explicación sustituye la función de **vigilancia activa** (rondines) por la de **control horario**, lo cual no atiende la necesidad ni la intencion original.
    * **Conflicto de intereses:** Algunos vecinos han observado un conflicto de intereses con la prestación de servicios de portería y mantenimientos correctivos dentro de la Privada Parma.
    """)




# --- 9. PROTOCOLOS OPERACIONALES ---
with st.expander("📄 Incumplimiento en la Entrega de Protocolos Operacionales de Portería"):
    st.markdown("""
    Se reitera la solicitud formal, pendiente desde hace **casi un año**, referente a la entrega y publicación de los protocolos operativos que rigen el servicio de portería.

    * **Compromiso Incumplido:** La Administración se comprometió a formalizar y divulgar las consignas específicas para el control de acceso, manejo de paquetería, registro de visitantes y procedimientos de emergencia. Este compromiso se mantiene sin atender.
    * **Riesgo Operacional:** La ausencia de protocolos operativos escritos y avalados por el Consejo implica que el personal de vigilancia opera bajo directrices informales o variables. Esto genera un **riesgo de seguridad y operacional** al impedir la auditoría de procedimientos y la estandarización del servicio de vigilancia.
    * **Requerimiento:** Se exige la entrega inmediata de los protocolos completos o la documentación oficial que justifique de forma explícita el retraso continuado.
    """)
    
# --- 10. INCUMPLIMIENTO AL ARTÍCULO 31 ---
with st.expander("⚖️ Incumplimiento Sistemático al Marco Legal (Artículo 31)"):
    st.markdown(
        """
        La Administración ha demostrado un **incumplimiento constante y repetido** de sus deberes legales, 
        tal como lo exige el **Artículo 31 de la Ley de Propiedad en Condominio en el Estado de México**. 
        
        Esto afecta gravemente la **transparencia** y la **legalidad** con la que se maneja nuestra comunidad.
        """
    )
    st.divider()

    # --- Sección 1: Documentación ---
    st.subheader("1. 📁 No entregan los documentos (Fracción III)")

    st.markdown(
        """
        **La ley obliga a la Administración a:** * **Guardar y conservar toda la documentación** del condominio para que los propietarios puedan **consultarla en cualquier momento.**
        
        **El incumplimiento:** * La documentación **casi nunca está disponible**, lo que representa una **falta crónica** de transparencia y acceso a la información.
        """
    )

    # --- Sección 2: Convocatorias ---
    st.subheader("2. ⏱️ Las convocatorias son tardías (Fracción VII)")

    st.markdown(
        """
        **La ley obliga a la Administración a:** * **Convocar a todas las asambleas** (generales y extraordinarias) **respetando estrictamente los plazos** y reglas que marca la ley y el reglamento interno.
        
        **El incumplimiento:** * Se han registrado múltiples ocasiones en las que las convocatorias se emitieron **fuera del tiempo reglamentario**, afectando la correcta organización de las reuniones y la participación.
        """
    )

    # --- Sección 3: Actas y Minutas ---
    st.subheader("3. ✍️ Las actas de asamblea son deficientes (Fracción V)")

    st.markdown(
        """
        **La ley obliga a la Administración a:** * **Llevar un "Libro de Actas"** formal, registrar en él todos los acuerdos y **comunicarlos por escrito** a cada propietario.
        
        **El incumplimiento:**
        
        * **Actas Informales:** En lugar de actas formales, se han usado **mensajes informales de WhatsApp**. En el caso de febrero de 2025, el mensaje contenía además **errores de cálculo** en los gastos.
        * **Deslindan su Responsabilidad:** La Mesa Directiva ha aseverado incorrectamente que la obligación de llevar y conservar las actas recae en los asistentes, cuando la ley es **categórica** al asignar esta tarea a la **Administración** (a través de su secretario).
        """
    )
    st.warning('Desde el 13 de Septiembre se solicitaron las minutas faltantes a la Administración y Mesa Directiva, hasta el momento no han podido ser compartidas.', icon="⚠️")
    st.warning('En su caso se puede llegar a desconocer los acuerdos de la Asambleas.', icon="⚠️")

    st.divider()

    # --- Conclusión ---
    st.error(
        """
        **Conclusión:** Este cúmulo de violaciones a la ley y la defensa de procedimientos irregulares 
        por parte de la Mesa Directiva y Administración exige una **corrección inmediata** para restablecer la legalidad en el condominio.
        """
    )

# --- 11. DELEGACIÓN OPERATIVA ---
with st.expander("🛡️ Incumplimiento de Funciones Estatutarias (Delegación Operativa)"):
    st.markdown("""
    Ante las quejas sobre deficiencias de la seguridad del Fraccionamiento Aurea de los vecinos, el Presidente de la Mesa Directiva ha indicado a los vecinos: **"Vayan ustedes a expresar esas inconformidades directamente"**.

    Esta instrucción constituye una **delegación inapropiada** de responsabilidades y un **incumplimiento de las funciones estatutarias** del Consejo Directivo del Fraccionamiento Aurea, las cuales incluyen:
    * Asociación Condominal AUREA, A.C. a través de El Consejo Directivo tiene como objeto vigilar que el Administrador General cumpla con sus obligaciones.
    * El Administrador General también se encarga de la coordinación y dirección de los servicios de Seguridad del Conjunto Urbano.
                
    **Nota: ¿Ustedes ya saben quiénes de la Privada Parma integran el Consejo Directivo? ¿La Administración o la Mesa Directiva informaron cuándo se formó?** 
    
    **💡 Hint**: Es el mismo que los manda a quejarse directamente con la seguridad, ¿Cuándo asumira su responsabilidad y transparencia de sus acciones?
    """)

# --- CONCLUSIÓN ---
st.markdown("---")
st.error("### 🛑 Conclusión Formal y Solicitud de Auditoría Externa:")
st.markdown("""
La combinación de la **pérdida de capital (Fondo Convive)**, las **inconsistencias contables persistentes** (incluyendo las detalladas en la sección de *Aclaraciones Contables Específicas*), el **incremento de gasto no justificado**, el **riesgo fiduciario**, el **incumplimiento en la entrega de protocolos de seguridad** y la **violación de los deberes legales** (Art. 31) configuran una situación de alto riesgo financiero y operacional que exige la acción inmediata.

**Requerimientos Inmediatos:**
1.  **Justificación documentada** de la inacción para ajustar la cuota de mantenimiento.
2.  **Entrega de todos los protocolos documentales** y estados de cuenta para auditoría.
3.  **Auditoría externa** para validar la consistencia de los balances.
4.  **Clarificación exhaustiva y documentación de respaldo** de los movimientos contables detallados en el punto *Aclaraciones Contables Específicas*.
5.  **Entrega inmediata de los Protocolos Operacionales de Portería** (Pendiente por casi un año).
6.  **Apego Inmediato al Artículo 31, Fracciones III, V y VII**, con la regularización de la documentación y minutas.
            
""")


