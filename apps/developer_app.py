import pandas as pd
import streamlit as st

from developer.training_history import show_training_history

MODELS_DIR = "./models/"
TRAINING_CSV_SUFFIX = "_training_history.csv"
EVALUATION_PATH = "./models/evaluation_predictions.csv"


def main():
    st.title("ML Dashboard")

    st.header("Training History")
    show_training_history(MODELS_DIR, TRAINING_CSV_SUFFIX)

    st.header("Evaluation")
    evaluation_df = pd.read_csv(EVALUATION_PATH)
    st.dataframe(evaluation_df)


if __name__ == "__main__":
    main()
