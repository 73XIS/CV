import streamlit as st
from PIL import Image


st.set_page_config(page_title="AlexisCV", page_icon=":star:", layout="wide")

# Assets #
base_width = 200
Alexis_picture = Image.open("images/Alexis.jpg")
wpercent = (base_width / float(Alexis_picture.size[0]))
hsize = int((float(Alexis_picture.size[1]) * float(wpercent)))
Alexis_picture = Alexis_picture.resize((base_width, hsize), Image.Resampling.LANCZOS)
Alexis_picture.save("Alexis.jpg")


# Header #
with st.container():
	left_column, right_column = st.columns([1, 3])
	with left_column:
		st.image(Alexis_picture)
	with right_column:
		st.title("Alexis Szedlacsek")
		st.subheader("About me:")
		st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
		    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
		    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\
			nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\
			reprehenderit in voluptate velit esse cillum dolore eu fugiat\
			nulla pariatur. Excepteur sint occaecat cupidatat non proident,\
			sunt in culpa qui officia deserunt mollit anim id est laborum.")


# Body #
with st.container():
	st.divider()
	left_column, right_column = st.columns([1, 3])
	with right_column:
		with st.expander("**EXPERIENCE**"):
			st.markdown("#")
			st.caption("Location: Cluj-Napoca, Cluj")
			st.markdown(
				"""
				February 2023 - June 2023\n
				- **Barista at *Meron***\n
				October 2019 - November 2023\n
				- **Volunteer at *Societatea Studentilor Europenisti***\n
				July 2022 - August 2022\n
				- **Warehouse Operative at *Untold***\n
				May 2022 - July 2022\n
				- **Waiter at *Bruto***\n
				July 2021 - October 2021\n
				- **Waiter at */Form***\n
				August 2020 - October 2020\n
				- **Waiter at *O'Peter's Irish Pub***\n
				March 2020 - August 2020\n
				- **Waiter at *Caro Club***\n
				October 2019 - March 2020\n
				- **Volunteer at *Eurostud***\n
				March 2018 - March 2019\n
				- **Sound Engineer at *Corvin Recording Studio***
				"""
			)
		with st.expander("**EDUCATION**"):
			st.markdown("#")
			st.markdown(
				"""
				2024 - **100 Days of Code: The Complete Python Pro Bootcamp**\n
				*Udemy*
				"""
			)
			st.markdown("#")
			st.markdown(
				"""
				2022 - **Bachelor Degree Management**\n
				*Babes-Bolyai University European Studies, Cluj-Napoca*
				"""
			)
			st.markdown("#")
			st.markdown(
				"""
				2019 - **Baccalaureate Bio-Chemistry**\n
				*Onisifor Ghibu High School, Cluj-Napoca*
				"""
			)
			st.markdown("#")
			st.markdown(
				"""
				2015 - **National Evaluation**\n
				*Bathory Istvan School, Cluj-Napoca*
				"""
			)
		with st.expander("**SKILLS**"):
			st.markdown("#")
			st.write(
				"""
				- Multilingual
				- Knowledge of Python , Microsoft Powerpoint , Excel , Adobe Illustrator
				- Great interpersonal skills
				- Fast learner
				- Responsible and reliable
				- Teamwork skills
				- Attention to detail
				- High level of integrity
				"""
			)

	with left_column:
		st.subheader("CONTACT")
		st.markdown("#")
		st.write(
			"""
			:placard: Cluj-Napoca, Cluj\n
			:telephone_receiver: 0721165001\n
			:e-mail: alexis.szedlacsek@yahoo.com\n
			"""
		)
    