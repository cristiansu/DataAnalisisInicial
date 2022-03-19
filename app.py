import os
import streamlit as st 

# EDA Pkgs
import pandas as pd 

# Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 

st.set_page_config(
    page_title = 'DashboardTR',
    page_icon = '📊',
    layout = 'wide'
)

with st.container():
    st.image('logo.png')
    st.write("[< Volver a Machine Learning](https://web-casgroup-capacitacion.herokuapp.com/py-ml)")

def main():
	""" Python Análisis de Datos"""
	st.title("Exploración Inicial de Datos con Python 📊")
	#st.subheader("Exploración de Múltiples Set de Datos")

	html_temp = """
	<div style="background-color:orange; text-align:center;"><p style="color:white;font-size:50px;padding:10px">Múltiples Datasets 📈</p></div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)

	def file_selector(folder_path='./datasets/'):
		filenames = os.listdir(folder_path)
		selected_filename = st.selectbox("Seleccione un Dataset 📖",filenames)
		return os.path.join(folder_path,selected_filename)

	filename = file_selector()
	st.info("Has Seleccionado el Dataset: {}".format(filename))

	# Read Data
	df = pd.read_csv(filename)
	# Show Dataset

	if st.checkbox("Mostrar Dataset"):
		number = st.number_input("Seleccionar Números de Columnas para ver con + o -", value=1, min_value=1, step=1)
		st.dataframe(df.head(number))

	# Show Columns
	if st.button("Nombre de Columnas"):
		st.write(df.columns)

	# Show Shape
	if st.checkbox("Dimensiones del Dataset"):
		data_dim = st.radio("Mostrar Dimensión por: ",("Rows","Columns"))
		if data_dim == 'Rows':
			st.text("Number of Rows")
			st.write(df.shape[0])
		elif data_dim == 'Columns':
			st.text("Number of Columns")
			st.write(df.shape[1])
		else:
			st.write(df.shape)

	# Select Columns
	if st.checkbox("Seleccionar Columnas a Mostrar"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect("Seleccionar",all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df)
	
	# Show Values
	if st.button("Value Counts"):
		st.text("Value Counts By Target/Class")
		st.write(df.iloc[:,-1].value_counts())


	# Show Datatypes
	# if st.button("Data Types"):
	# 	st.write(df.dtypes)



	# Show Summary
	if st.checkbox("Resumen Data"):
		st.write(df.describe().T)

	## Plot and Visualization

	# st.subheader("Data Visualization")
	# Correlation
	# Seaborn Plot
	# if st.checkbox("Correlation Plot[Seaborn]"):
	# 	st.write(sns.heatmap(df.corr(),annot=True))
	# 	st.pyplot()

	
	# Pie Chart
	# if st.checkbox("Pie Plot"):
	# 	all_columns_names = df.columns.tolist()
	# 	if st.button("Generate Pie Plot"):
	# 		st.success("Generating A Pie Plot")
	# 		st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
	# 		st.pyplot()

	# Count Plot
	# if st.checkbox("Plot of Value Counts"):
	# 	st.text("Value Counts By Target")
	# 	all_columns_names = df.columns.tolist()
	# 	primary_col = st.selectbox("Primary Columm to GroupBy",all_columns_names)
	# 	selected_columns_names = st.multiselect("Select Columns",all_columns_names)
	# 	if st.button("Plot"):
	# 		st.text("Generate Plot")
	# 		if selected_columns_names:
	# 			vc_plot = df.groupby(primary_col)[selected_columns_names].count()
	# 		else:
	# 			vc_plot = df.iloc[:,-1].value_counts()
	# 		st.write(vc_plot.plot(kind="bar"))
	# 		st.pyplot()


	# Customizable Plot

	st.subheader("Gráficos Ajustables")
	all_columns_names = df.columns.tolist()
	type_of_plot = st.selectbox("Seleccionar Tipo de Gráfico",["area","bar","line","hist","box","kde"])
	selected_columns_names = st.multiselect("Seleccionar Columnas",all_columns_names)

	if st.button("Generar Gráfico"):
		st.success("Generar Gráfico Ajustable de {} de {}".format(type_of_plot,selected_columns_names))

		# Plot By Streamlit
		if type_of_plot == 'area':
			cust_data = df[selected_columns_names]
			st.area_chart(cust_data)

		elif type_of_plot == 'bar':
			cust_data = df[selected_columns_names]
			st.bar_chart(cust_data)

		elif type_of_plot == 'line':
			cust_data = df[selected_columns_names]
			st.line_chart(cust_data)

		# Custom Plot 
		elif type_of_plot:
			cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()

	if st.button("Fín Exploración"):
		st.balloons()

	# st.sidebar.header("About App")
	# st.sidebar.info("A Simple EDA App for Exploring Common ML Dataset")

	# st.sidebar.header("Get Datasets")
	# st.sidebar.markdown("[Common ML Dataset Repo]("")")

	# st.sidebar.header("About")
	# st.sidebar.info("Jesus Saves@JCharisTech")
	# st.sidebar.text("Built with Streamlit")
	# st.sidebar.text("Maintained by Jesse JCharis")


if __name__ == '__main__':
	main()