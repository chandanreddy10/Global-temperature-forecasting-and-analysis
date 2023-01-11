import streamlit as st
import helper_functions

st.set_page_config(page_title='Project report',layout='wide')
st.title(":blue[Effects of Global Temperature rise on regions.]")

#text container
with st.container():
    st.markdown(
        """#### In this part we will look at how the rise in temperature affects the different regions in the world.The factors that are considered would be **mean sea level** rise and the **glacier mass balance**..  \n"""
        """  \n"""
        """#### Mean Sea level is the sea level measured in different years, if the values are positive the sea level has increased. if the value is negative the sea level has decreased.  \n"""
        """  \n"""
        """#### Mass balance is the total sum of all the accumulation (snow, ice, freezing rain) and melt or ice loss (from calving icebergs, melting, sublimation) across the entire glacier.  \n""")

#plot container
with st.container():
    
    col1, col2 = st.columns(2, gap="large")
    plots = helper_functions.get_plot
    u_parent = './plots/affects_on_regions/'
    with col1:
        st.image(plots("temperature_increase_since_1950",u_parent), caption="temperature increase since 1950",width=650)
    with col2:
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.markdown(
            """### The map describes the increase in temperature of various regions since 1960.  \n""" 
        """### This maximum increase is been in canada, greenland, iran and russia.""")

#glacier plots
with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        title = '<p style="font-family:Sans-Serif; color:#2B3467; font-size: 30px;text-align:center;">Glaciers count in each region.</p>'
        st.markdown(title,unsafe_allow_html=True)
        st.image(plots("glaciers_count",u_parent),caption="glaciers count by region",width=600)

    with col2:
        title2 = '<p style="font-family:Sans-Serif; color:#2B3467; font-size: 30px;text-align:center;">Regions with highest glacier area.</p>'
        st.markdown(title2,unsafe_allow_html=True)
        st.image(plots("glacier_by_area",u_parent),caption="glacier by area",width=600)

#info about the plots
with st.container():
    st.text("")
    st.text("")
    st.markdown("""### The above plots show the glacier count and the glacier area by region.The plot shows that china has the highest glacier count but based on the area greenland wins, this is very important because glacier count hardly matter, greenland comes in the artic region and is largely covered with ice sheets.  \n"""
    """### Now it is clear that area matters lets compare the area plot to the temperature plot. The shocking revelation is that they both are approx same if we remove iran.this is alarming and thus the ice sheet melts and thus we will see an increase in the sea levels.  \n"""
    """### Let's see the mean sea level increase with the glacier mass balance. if glacier mass balance is decreasing, then the the accumulation is less and vice versa.  \n""")
    st.image(plots("sea_level_vs_glacier_mass_balance",u_parent),caption="sea level vs glacier mass balance",width=1000)
    st.markdown("""### From the above it is clear that the rise in sea level is rightly visible as the glacier mass balance increases.Below are the examples of a capital city and a small place in pacific ocean facing the effect of the rising sea levels.""")


#examples

with st.container():
    st.header("The :red[sinking] capital city of indonesia")
    
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.image("./plots/images/jakarta_in_map.png",caption="jakarata location",width=600)

    with col2:
        st.markdown("""Jakarta officially the Special Capital Region of Jakarta  is the capital and largest city of Indonesia. Lying on the northwest coast of Java, the world's most populous island, 
        Jakarta is the largest city in Southeast Asia and serves as the diplomatic capital of ASEAN.The city is the economic, cultural, and political centre of Indonesia. It possesses a province-level 
        status and has a population of 10,562,088 as of mid 2021""")
        st.text("")
        st.text("")
        st.markdown("""A sprawling city of more than 30 million people, Jakarta sits on a low, flat alluvial plain through which 13 rivers flow, all of which are prone to flooding during Monsoon season. 
        Forty per cent of the city is below sea level leaving it exposed to rising sea levels.""")
        st.markdown("""And with sea levels predicted to rise , without a reduction in emissions, global seal levels could rise and the Indonesian capital is in a precarious situation.""")
with st.container():

    st.header("First country to be :red[swallowed] by the rising sea levels")
    col1, col2 = st.columns(2,gap="large")

    with col1:
        st.image("./plots/images/kiribati_map.png",caption="kiribati location",width=600)
        st.text("")
        st.text("")

    with col2:
        st.markdown("""A typical postcard paradise. A group of 33 atolls located in the central Pacific between Hawaii and Australia. Stilt houses on the beach. Twelve different words for coconut, depending on their level of ripeness. Fishermen in sarongs collect shellfish at low tide.This is Kiribati. 
        The first country that will be swallowed up by the sea as a result of climate change.
        Global warming is melting the polar icecaps, glaciers and the ice sheets that cover Greenland, causing sea levels to rise. It is estimated sea levels have risen an average of 3.2 mm per year since 1993, according to the Fifth Assessment Report of the United Nations Intergovernmental Panel on Climate Change""")

        st.markdown("""Half of Kiribati's more than 100,000 inhabitants live in the capital, South Tarawa, a narrow strip of land that lies between the Pacific and an enormous lagoon that depends on a freshwater lens.
        Life in Kiribati has always revolved around water.It's everywhere you look, always on the horizon. Children play in the water from a young age. It provides them with fish and a means to water their crops. But now, all they can do is look on as the marawa (sea in Gilbertese) turns against them for the first time.  \n"""
        """  \n"""
        """Kiribatians have already begun to emigrate in response to what they believe to be an unavoidable situation. Others cling on to their land, looking for temporary solutions: residents have begun building walls out of coral rocks which are then destroyed by the high tide. Some towns have shifted a few metres inland, 
        and mangroves have been planted to protect the soil from erosion and mitigate storm surges. 
        If the predictions are accurate, the atoll of Tarawa will be uninhabitable within a generation.""")