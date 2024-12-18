import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
from fpdf import FPDF
import mysql.connector
import datetime

st.sidebar.image(image='img/LogoPerla.png',caption="")
st.sidebar.caption("Bienvenido!.")

with st.sidebar:
        beta_sign = """
        <span style="
        font-size: 12px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff5733;
        padding: 20px;
        border-radius: 10px;
        ">
            BETA
        </span>
        """
        seleccion_menu = option_menu(
            menu_title="Seleccione su Rol",
            options=["","Jefe de grupo","Administrador"]
        )

if seleccion_menu == "":
        st.image(image='img/LogoUnixd.png', caption="", use_column_width=True)
        st.write("\n")
        st.title("Bienvenidos a nuestro proyecto :)")
        st.write("\n")
        st.write("Este proyecto tiene como objetivo crear un programa para que un jefe de grupo pueda asignar las asistencias de los maestros dependiendo de su carrera")
        st.write("\n")
        st.write("Tambien puede realizar 3 tipos de reportes como: Reporte por profesor, Reporte por materia Y reporte global que ese realize un calculo para que te de el pocentaje de asistencias en las 2 carreras")
        st.write("\n")
        st.write("Para el administrador, lo unico que puede hacer es añadir nuevos datos o eliminar datos de la base de datos")
        st.write("\n")
        st.write("A lo largo de esta página, encontrarás información sobre nuestro trabajo, ideas y logros a lo largo del proceso. Esperamos que disfrutes navegando por nuestra página y descubras más sobre este proyecto.")

if seleccion_menu == "Jefe de grupo":
        beta_sign = """
        <span style="
        font-size: 10px;
        font-weight: bold;
        color: #ffffff;
        background-color: blue;
        padding: 5px 10px;
        border-radius: 4px;
        ">
                BETA
        </span>
        """
        st.caption("Bienvenido Jefe de grupo!")
        seleccion_jefe = option_menu(
                menu_title="Apartado de Asistencias",
                options=["Asignar Asistencia","Modificar Asistencia"]
        )
        if seleccion_jefe == "Asignar Asistencia":
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                cursorxdxdd = conexion.cursor()
                cursorlol = conexion.cursor()
                cursorxdxdd.execute("SELECT * FROM materiaprofe WHERE Asistencia IS NULL")
                clases_programadas = cursorxdxdd.fetchall()
                if clases_programadas:
                        MostrarClasesXD = [f"{clase[0]} - {clase[1]} - {clase[2]} - {clase[3]} - {clase[4]} - {clase[5]}" for clase in clases_programadas]
                        clase_seleccionada = st.selectbox("Selecciona la clase pendiente:", MostrarClasesXD)
                        JAJAJAXDXD = clases_programadas[MostrarClasesXD.index(clase_seleccionada)][0]
                        st.write("\n")
                        st.info("El Profesor asistió a la clase?")
                        
                        izquierdaXD, DerechaXD = st.columns(2)
                        if izquierdaXD.button("Si asistió", use_container_width=True):
                                cursorlol.execute("UPDATE materiaprofe SET Asistencia=1 WHERE ID= ?", (JAJAJAXDXD,))
                                conexion.commit()
                                st.success("Asistencia asignada exitosamente!.")
                                conexion.close()
                                
                        if DerechaXD.button("No asistió", use_container_width=True):
                                cursorlol.execute("UPDATE materiaprofe SET Asistencia=0 WHERE ID= ?", (JAJAJAXDXD,))
                                conexion.commit()
                                st.success("Asistencia asignada exitosamente!.")
                                conexion.close()
                        

                else:
                        st.info("No hay clases pendientes.")
                        st.write("\n")
     


                        
        if seleccion_jefe == "Modificar Asistencia":
                st.title("Modificar asistencias")
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                cursorxdxdd = conexion.cursor()
                cursorlol = conexion.cursor()
                cursorxdxdd.execute("SELECT * FROM materiaprofe WHERE (Asistencia=1 OR Asistencia=0)")
                clases_programadas = cursorxdxdd.fetchall()
                if clases_programadas:
                        MostrarClasesXD = [f"{clase[0]} - {clase[1]} - {clase[2]} - {clase[3]} - {clase[4]} - {clase[5]}" for clase in clases_programadas]
                        clase_seleccionada = st.selectbox("Selecciona la clase a modificar:", MostrarClasesXD)
                        JAJAJAXDXD = clases_programadas[MostrarClasesXD.index(clase_seleccionada)][0]
                        st.write("\n")
                        st.info("El Profesor asistió a la clase?")
                        izquierdaXD, DerechaXD = st.columns(2)
                        if izquierdaXD.button("Si asistió", use_container_width=True):
                                cursorlol.execute("UPDATE materiaprofe SET Asistencia=1 WHERE ID= ?", (JAJAJAXDXD,))
                                conexion.commit()
                                st.success("Asistencia asignada exitosamente!.")
                                conexion.close()
                                
                        if DerechaXD.button("No asistió", use_container_width=True):
                                cursorlol.execute("UPDATE materiaprofe SET Asistencia=0 WHERE ID= ?", (JAJAJAXDXD,))
                                conexion.commit()
                                st.success("Asistencia asignada exitosamente!.")
                                conexion.close()
                        

                else:
                        st.info("No hay clases pendientes.")
                        st.write("\n")





        
                

        
        beta_sign = """
        <span style="
        font-size: 10px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff5733;
        padding: 5px 10px;
        border-radius: 4px;
        ">
                BETA
        </span>
        """
        seleccion_reporte = option_menu(
                menu_title="Apartado de Reportes",
                options=["Reporte por profesor","Reporte por materia", "Reporte global"]
        )


        
        if seleccion_reporte == "Reporte por profesor":
                st.title("Reporte por profesor")
                # Conectar a la base de datos
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                df = pd.read_sql("SELECT DISTINCT Profesor FROM materiaprofe;", conexion)
                st.write("  \n")
                seleccion_profeexd = st.selectbox('Selecciona un profesor:', df['Profesor'])
                cursor = conexion.cursor()
                conexion.close()
                # Función para generar el PDF
                def generar_pdf():
                        # Conectar a la base de datos
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursor = conexion.cursor()
                        cursor2 = conexion.cursor()
                        cursor3 = conexion.cursor()
                        cursor4 = conexion.cursor()
                        cursor5 = conexion.cursor()
                        cursor6 = conexion.cursor()
                        cursor.execute("SELECT * FROM materiaprofe WHERE Profesor=? AND (Asistencia=0 OR Asistencia=1)",(seleccion_profeexd,))
                        cursor2.execute("SELECT COUNT(Materia) FROM materiaprofe WHERE Profesor=?",(seleccion_profeexd,))
                        cursor3.execute("SELECT COUNT(Asistencia) FROM materiaprofe WHERE Profesor=? AND Asistencia=1",(seleccion_profeexd,))
                        cursor4.execute("SELECT COUNT(Asistencia) FROM materiaprofe WHERE Profesor=? AND Asistencia=0",(seleccion_profeexd,))
                        cursor5.execute("SELECT MIN(Fecha) FROM materiaprofe WHERE Profesor =?",(seleccion_profeexd,))
                        cursor6.execute("SELECT MAX(Fecha) FROM materiaprofe WHERE Profesor =?",(seleccion_profeexd,))
                        # Recuperar todos los registros
                        materiaprofe = cursor.fetchall()
                        Cantidadmateriasprofe = cursor2.fetchall()
                        Asistidamateriaprofe = cursor3.fetchall()
                        Faltamateriaprofe = cursor4.fetchall()
                        FechaMax = cursor6.fetchall()
                        FechaMin = cursor5.fetchall()
                        # Extraer el primer valor si es una tupla
                        ConvertioXD_numero = str(Cantidadmateriasprofe[0]) if isinstance(Cantidadmateriasprofe, (tuple, list)) else str(Cantidadmateriasprofe)
                        ConvertioXD_Asistencia = str(Asistidamateriaprofe[0]) if isinstance(Asistidamateriaprofe, (tuple, list)) else str(Asistidamateriaprofe) 
                        ConvertioXD_Falta = str(Faltamateriaprofe[0]) if isinstance(Faltamateriaprofe, (tuple, list)) else str(Faltamateriaprofe) 
                        
                        ConvertioXD_FCHMX = str(FechaMax[0]) if isinstance(FechaMax, (tuple, list)) else str(FechaMax) 
                        ConvertioXD_FCHMN = str(FechaMin[0]) if isinstance(FechaMin, (tuple, list)) else str(FechaMin) 
                        # Crear una instancia de FPDF
                        pdf = FPDF()
                        pdf.set_auto_page_break(auto=True, margin=15)
                        # Agregar una página
                        pdf.add_page()
                        pdf.set_font('Arial', 'B', 16)
                        # Título del reporte
                        pdf.cell(200, 10, 'Reporte de Profesor', ln=True, align='C')
                        pdf.ln(10)
                        #tipo de fuente para el contenido 
                        pdf.set_font('Arial', '', 12)

                        # Encabezados de la tabla
                        pdf.cell(10, 10, 'ID', 1)     
                        pdf.cell(45, 10, 'Profesor', 1)  
                        pdf.cell(40, 10, 'Materia', 1)    
                        pdf.cell(40, 10, 'Carrera', 1)  
                        pdf.cell(30, 10, 'Fecha', 1)      
                        pdf.cell(25, 10, 'Horario', 1)   
                        pdf.cell(20, 10, 'Asistencia', 1) 
                        pdf.ln()
                        
                        # Agregar los registros de materias al PDF
                        for materia in materiaprofe:
                            pdf.cell(10, 10, str(materia[0]), 1)   
                            pdf.cell(45, 10, materia[1], 1)        
                            pdf.cell(40, 10, materia[2], 1)        
                            pdf.cell(40, 10, str(materia[3]), 1)    
                            pdf.cell(30, 10, materia[4], 1)        
                            pdf.cell(25, 10, materia[5], 1)        
                            pdf.cell(20, 10, str(materia[6]), 1)    
                            pdf.ln()
                        # Guardar el archivo PDF
                        pdf.cell(200, 10, '', ln=True)
                        pdf.cell(200, 10, 'El profesor ' + materia[1]+ ' imparte un total de ' +ConvertioXD_numero+ '  materias, cubriendo diferentes áreas', ln=True)
                        pdf.cell(200, 10, 'de estudio que son de gran relevancia para los estudiantes en su desarrollo académico', ln=True)
                        pdf.cell(200, 10, 'Durante el periodo de tiempo desde: ' +ConvertioXD_FCHMN+ ' - '+ConvertioXD_FCHMX+' , el profesor ha', ln=True)
                        pdf.cell(200, 10, 'demostrado un alto nivel de compromiso con su trabajo, asistiendo a '+ConvertioXD_Asistencia+' clases de las programadas.', ln=True)
                        pdf.cell(200, 10, 'No obstante, ha tenido '+ConvertioXD_Falta+' ausencias, lo cual puede deberse a diversas circunstancias, como asuntos', ln=True)
                        pdf.cell(200, 10, 'personales o imprevistos, que en ocasiones son inevitables. ya que permite la continuidad', ln=True) 
                        pdf.cell(200, 10, 'de los contenidos y facilita el progreso de los estudiantes en las  materias impartidas. ', ln=True) 
                        pdf.cell(200, 10, 'Sin embargo, las ausencias también son comprensibles en ciertos contextos,siempre que no afecten', ln=True) 
                        pdf.cell(200, 10, 'significativamente el desarrollo académico de los alumnos. ', ln=True)  
                        pdf.output('Reporte_profe.pdf')

                        
                        # Cerrar la conexión
                        conexion.close()
                        # Retornar el contenido del PDF en bytes
                        return pdf.output(dest='S').encode('latin1')
                # Botón para generar el PDF
                if st.button("Generar Reporte"):
                        # Generar el PDF
                        pdf_content = generar_pdf()
                        st.caption("100% completado...")
                        # Crear un botón de descarga
                        st.download_button(
                                label="Descargar Reporte en PDF",
                                data=pdf_content,
                                file_name="Reporte_Profe.pdf",
                                mime="application/pdf"
                        )














                        
        if seleccion_reporte == "Reporte por materia":
                st.title("Reporte por materia")
                # Conectar a la base de datos
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                df = pd.read_sql("SELECT DISTINCT Materia FROM materiaprofe;", conexion)
                st.write("  \n")
                seleccion_materiaxd = st.selectbox('Selecciona un materia:', df['Materia'])
                cursor = conexion.cursor()
                conexion.close()
                # Función para generar el PDF
                def generar_pdf():
                        # Conectar a la base de datos
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursor = conexion.cursor()
                        cursor.execute("SELECT * FROM materiaprofe WHERE Materia=? AND (Asistencia=0 OR Asistencia=1)",(seleccion_materiaxd,))
                        # Recuperar todos los registros
                        materiaprofe = cursor.fetchall()
                        # Crear una instancia de FPDF
                        pdf = FPDF()
                        pdf.set_auto_page_break(auto=True, margin=15)
                        # Agregar una página
                        pdf.add_page()
                        # Establecer el tipo de fuente
                        pdf.set_font('Arial', 'B', 16)
                        # Título del reporte
                        pdf.cell(200, 10, 'Reporte de Profesor', ln=True, align='C')
                        # Espacio adicional
                        pdf.ln(10)
                        #tipo de fuente para el contenido
                        pdf.set_font('Arial', '', 12)

                        # Encabezados de la tabla
                        pdf.cell(10, 10, 'ID', 1)        
                        pdf.cell(45, 10, 'Profesor', 1)   
                        pdf.cell(40, 10, 'Materia', 1)    
                        pdf.cell(40, 10, 'Carrera', 1)  
                        pdf.cell(30, 10, 'Fecha', 1)     
                        pdf.cell(25, 10, 'Horario', 1)   
                        pdf.cell(20, 10, 'Asistencia', 1)
                        pdf.ln()
                        
                        # Agregar los registros de materias al PDF
                        for materia in materiaprofe:
                            pdf.cell(10, 10, str(materia[0]), 1)   
                            pdf.cell(45, 10, materia[1], 1)        
                            pdf.cell(40, 10, materia[2], 1)        
                            pdf.cell(40, 10, str(materia[3]), 1)    
                            pdf.cell(30, 10, materia[4], 1)         
                            pdf.cell(25, 10, materia[5], 1)        
                            pdf.cell(20, 10, str(materia[6]), 1)   
                            pdf.ln()
                        # Guardar el archivo PDF
                        pdf.cell(200, 10, '', ln=True)
                        pdf.cell(200, 10, 'Este informe detalla la impartición de clases de la materia '+materia[2]+ ' indicando si la materia fue enseñada  ', ln=True)
                        pdf.cell(200, 10, 'por diferentes profesores a lo largo del periodo y la asistencia correspondiente de cada uno.', ln=True)
                        pdf.output('Reporte_profe.pdf')
                        pdf.cell(20, 10, 'La materia: ', ln=True, align='C')
                        pdf.cell(20, 10, seleccion_materiaxd, ln=False, align='C')
                        pdf.output('Reporte_profe.pdf')
                        
                        # Cerrar la conexión
                        conexion.close()
                        # Retornar el contenido del PDF en bytes
                        return pdf.output(dest='S').encode('latin1')
                # Botón para generar el PDF
                if st.button("Generar Reporte"):
                        # Generar el PDF
                        pdf_content = generar_pdf()
                        st.caption("100% completado...")
                        #botón de descarga
                        st.download_button(
                                label="Descargar Reporte en PDF",
                                data=pdf_content,
                                file_name="Reporte_Materia.pdf",
                                mime="application/pdf"
                        )
                        
                        
                
        if seleccion_reporte == "Reporte global":
                st.title("Reporte Global")
                # Función para generar el PDF
                def generar_pdf():
                        # Conectar a la base de datos
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursor = conexion.cursor()
                        cursor.execute("SELECT (avg(Asistencia)*100) FROM materiaprofe")
                        # Recuperar todos los registros
                        materiaprofe = cursor.fetchall()
                        # Crear una instancia de FPDF
                        pdf = FPDF()
                        pdf.set_auto_page_break(auto=True, margin=15)
                        # Agregar una página
                        pdf.add_page()
                        # Establecer el tipo de fuente
                        pdf.set_font('Arial', 'B', 16)
                        # Título del reporte
                        pdf.cell(200, 10, 'Reporte Global', ln=True, align='C')
                        # Espacio adicional
                        pdf.ln(10)
                        # el tipo de fuente para el contenido
                        pdf.set_font('Arial', '', 12)

                        # Encabezados de la tabla
                        pdf.cell(60, 10, 'Tasa de cumplimiento', 1)
                        pdf.ln()
                        
                        # Agregar los registros de materias al PDF
                        for materia in materiaprofe:
                            pdf.cell(60, 10, str(materia[0]) + '%', 1)  
                            pdf.ln()
                        pdf.cell(200, 10, 'La tasa de cumplimiento de asistencias de las carreras ICI y ISET es cercana al ' + str(materia[0]) + '%.', ln=True)
                        pdf.cell(200, 10, 'Este porcentaje refleja un compromiso moderado de los docentes con su responsabilidad de asistir a', ln=True)
                        pdf.cell(200, 10, 'clases y cumplir con sus horarios. La asistencia regular de los maestros es fundamental para ', ln=True)
                        pdf.cell(200, 10, 'garantizar la continuidad del proceso educativo y el apoyo a los estudiantes, ya que su presencia es', ln=True)
                        pdf.cell(200, 10, 'crucial para el desarrollo de las actividades académicas')
        
                        pdf.output('Reporte_Global.pdf')
                        
                        # Cerrar la conexión
                        conexion.close()
                        # Retornar el contenido del PDF en bytes
                        return pdf.output(dest='S').encode('latin1')  #Dest 'S' devuelve el contenido como un string
                # Botón para generar el PDF
                if st.button("Generar Reporte"):
                        # Generar el PDF
                        pdf_content = generar_pdf()
                        st.caption("100% completado...")
                        #botón de descarga
                        st.download_button(
                                label="Descargar Reporte en PDF",
                                data=pdf_content,
                                file_name="Reporte_Global.pdf",
                                mime="application/pdf"
                        )
                
        

if seleccion_menu == "Administrador":
        beta_sign = """
        <span style="
        font-size: 10px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff5733;
        padding: 5px 10px;
        border-radius: 4px;
        ">
                BETA
        </span>
        """
        st.caption("Bienvenido admin!")
        seleccion_admin = option_menu(
                menu_title="Que desea hacer?",
                options=["Agregar Datos","Eliminar Datos"]
        )

        if seleccion_admin == "Agregar Datos":
                st.write("Agregar Datos")
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                df1 = pd.read_sql("SELECT DISTINCT Profesor FROM materiaprofe;", conexion)
                df2 = pd.read_sql("SELECT DISTINCT Materia FROM materiaprofe;", conexion)
                df3 = pd.read_sql("SELECT DISTINCT Carrera FROM materiaprofe;", conexion)
                conexion.close()
                st.write("  \n")
                seleccion_profeexdd = st.selectbox('Selecciona un profesor:', df1['Profesor'])
                seleccion_materiaxdd = st.selectbox('Selecciona una materia:', df2['Materia'])
                seleccion_carreraxdd = st.selectbox('Selecciona la carrera:', df3['Carrera'])
                Hoy = datetime.datetime.now()
                Anosiguiente = Hoy.year + 1
                XD = datetime.date(Anosiguiente, 12, 31)
                
                fecha = st.date_input(
                    "Seleccione la fecha",
                    (Hoy),
                    Hoy,
                    format="MM.DD.YYYY",
                )
 
                hora = st.time_input("Selecciona la hora de la clase:")
        
                if st.button("Agregar Clase"):
                        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                        cursorxd = conexion.cursor()
                        cursorxd.execute(
                            "INSERT INTO materiaprofe (Profesor, Materia, Carrera, Fecha, Horario, Asistencia) VALUES (?, ?, ?, ?, ?, NULL)",
                            (seleccion_profeexdd, seleccion_materiaxdd, seleccion_carreraxdd, str(fecha), str(hora))
                        )
                        conexion.commit()
                        st.success(f"Clase programada para el profesor {seleccion_profeexdd} con la materia {seleccion_materiaxdd} de la carrera {seleccion_carreraxdd} con fecha {fecha} a las: {hora} ha sido agregada exitosamente.")
                        conexion.close()


                        
        
        if seleccion_admin == "Eliminar Datos":

                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                cursorxdxdd = conexion.cursor()
                cursorlol = conexion.cursor()
                st.write("Eliminar Clases Programadas")
                cursorxdxdd.execute("SELECT * FROM materiaprofe ")
                clases_programadas = cursorxdxdd.fetchall()
                if clases_programadas:
                        MostrarClasesXD = [f"{clase[0]} - {clase[1]} - {clase[2]} - {clase[3]} - {clase[4]} - {clase[5]}" for clase in clases_programadas]
                        clase_seleccionada = st.selectbox("Selecciona la clase a eliminar:", MostrarClasesXD)
                        JAJAJAXDXD = clases_programadas[MostrarClasesXD.index(clase_seleccionada)][0]
                        if st.button("Eliminar Clase"):
                                cursorlol.execute("DELETE FROM materiaprofe WHERE ID=?", (JAJAJAXDXD,))
                                conexion.commit()
                                st.success("Clase eliminada exitosamente.")
                                conexion.close()
                        else:
                                st.info("No hay clases programadas para eliminar.")
               




               
        
               
