# Streamlit hello world app
import streamlit as st
import pandas as pd

def main():
    st.title('Hello World, coding is complicated!')
    st.subheader(' ',divider='rainbow')
    st.write('Hello World, its Julia!')
    st.write('I like roses :rose:')
    st.write(':rose: Ursprung und Geschichte:')
    st.write('Rosen existieren seit mehr als 35 Millionen Jahren. Die ältesten Rosenfossilien stammen aus Nordamerika. Die domestizierte Kulturrose, wie wir sie heute kennen, wurde vor etwa 5.000 Jahren in China entdeckt.')
    st.write(':rose: Vielfalt:')
    st.write('Es gibt über 100 verschiedene Arten von Rosen. Sie werden oft in drei Hauptkategorien unterteilt: Wildrosen, alte Rosen und moderne Rosen.')
    st.write(':rose: Symbolik:')
    st.write('Rosen sind weltweit als Symbole für Liebe, Leidenschaft und Schönheit bekannt. Unterschiedliche Farben haben verschiedene Bedeutungen. Zum Beispiel steht eine rote Rose traditionell für Liebe und Respekt.')
    st.write(':rose: Medizinische Verwendung:')
    st.write('Rosen werden in der traditionellen Medizin aufgrund ihrer möglichen entzündungshemmenden und antioxidativen Eigenschaften geschätzt.')
    st.code('streamlit run hello_world.py')
    st.sidebar.title('Rosen')
    st.sidebar.write('Rosen sind nicht nur atemberaubende Blumen, sondern tragen auch eine reiche Geschichte, tiefgreifende Symbolik und faszinierende Eigenschaften in sich. Mit über 100 verschiedenen Arten, die von wilden Rosen bis zu modernen Züchtungen reichen, haben Rosen weltweit ihren Platz in Gärten, Kunst und Kultur gefunden. Ihre vielfältigen Farben sprechen unterschiedliche Emotionen an, wobei die rote Rose für Liebe und Leidenschaft steht. Neben ihrer ästhetischen Schönheit werden Rosen auch in Parfüms und der traditionellen Medizin geschätzt. Lassen Sie uns einen kurzen Blick auf die zauberhafte Welt der Rosen werfen.')
    
    st.subheader('_Julia_ loves :red[roses] :rose:')
    st.subheader('This is a random Chart',divider='red')
    
if __name__ == '__main__':
    main()

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)
st.subheader('Das ist die jetzige Temperatur',divider='red')
import streamlit as st

st.metric(label="Temperatur", value="5 °C", delta="1.2 °C")

st.write('Rosen sind in Bezug auf die Temperatur recht anpassungsfähige Pflanzen. Die ideale Wachstumstemperatur für die meisten Rosensorten liegt zwischen 18 und 25 Grad Celsius. Sie bevorzugen also gemäßigte bis warme Bedingungen. Heute ist es zu kalt für Rosen.')

import streamlit as st

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')

    import streamlit as st



genre = st.radio(
    "Was ist deine Lieblingsblume?",
    [":rainbow[Tulpen]", "***Kirschblüten***", "Rosen :rose:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == '"Rosen :rose:"':
    st.write('Du wählst Rosen.')
else:
    st.write("You wählst nicht Rosen.")
