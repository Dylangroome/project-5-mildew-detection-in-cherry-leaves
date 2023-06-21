import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects many plant species.\n "
        f"* An employee takes a few samples of tree leaves and verifying visually if the "
        f"leaf tree is healthy or has powdery mildew. If there is powdery mildew, the "
        f"employee applies a specific compound to kill the fungus. The time spent applying "
        f"this compound is 1 minute.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset contains +4 thousand images taken from the  "
        f"client's crop fields. The images show healthy cherry leaves and cherry leaves "
        f"that have powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Dylangroome/project-5-mildew-detection-in-cherry-leaves/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a parasitized and uninfected cell visually.\n"
        f"* 2 - The client is interested in telling whether a given cell contains a malaria parasite or not. "
    )
