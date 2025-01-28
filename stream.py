import streamlit as st
st.title (" Hello GoMyCode ")


st.header("This is a header")

st.subheader("This is a subheader" )


st.text("this is my page")

st.success("Success")
st.info("Information")

st.warning("Warning")
from PIL import Image
img = Image.open("earthquakes.png")
st.image(img, width=900)
if st.checkbox("Show/Hide"):
	# affiche le texte si la case à cocher renvoie la valeur True

     st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):

	st.success("Male")

else:

	st.success("Female")

hobby = st.selectbox("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)

hobbies = st.multiselect("Hobbies: ",['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')

st.button("Click me for no reason")
if(st.button("About")):

	st.text("Welcome To Gomycode!!!")


name = st.text_input("Enter Your name", "Type Here ...")

if(st.button('Submit')):
	result = name.title()
	st.success(result)

# le premier argument prend le titre du slider
# le deuxième argument prend le début du slider
# le dernier argument prend le numéro de fin
level = st.slider("Select the level", 1, 5)

# imprimer le niveau
# format() est utilisé pour imprimer la valeur d'une variable à une position spécifique
st.text('Selected: {}'.format(level))
