import pandas as pd
import streamlit as st

PATH = "../models/"

# 1. Ensure this path points to an actual CSV spreadsheet, NOT a .pt model weights file!
FILE_PATHS = [
    "evaluation_predictions.csv",
    "resnet18_training_history.csv",
    "mobilenet_v3_small_training_history.csv",
    "training_history.csv",
]


def main():
    st.title("My App")

    selected_file = st.selectbox(label="Select a File:", options=FILE_PATHS)

    st.write(f"You selected: **{selected_file}**")

    try:
        # 2. Safely read your data spreadsheet
        df = pd.read_csv(PATH + selected_file)

        # 3. Use st.dataframe() to render it beautifully on the web page
        st.dataframe(df)

        required_cols = ["epoch"]

        # Check if EVERY required column is present in the dataframe
        if all(col in df.columns for col in required_cols):
            # Find the numeric position of 'epoch'
            epoch_index = list(df.columns).index("epoch")

            # Slice the list to grab everything AFTER that position
            metric_cols = list(df.columns)[epoch_index + 1 :]

            selected_col = st.selectbox(label="Select a Column:", options=metric_cols)

            st.line_chart(
                data=df,
                x="epoch",
                y=selected_col,
            )
        else:
            required_cols = ["ground_truth", "pred_mobilenet_v3_small", "pred_resnet18"]

            if all(col in df.columns for col in required_cols):
                model_name = st.selectbox(
                    label="Select a Column:", options=required_cols[1:]
                )

                st.write(f"Confusion Matrix (%): `{model_name}`")

                # Calculate the cross-tabulation table normalized by row (index)
                matrix_pct = pd.crosstab(
                    df["ground_truth"],
                    df[model_name],
                    rownames=["Actual"],
                    colnames=["Predicted"],
                    normalize="index",  # Each row totals 100% (Row Accuracy / Recall)
                )

                # Format numbers cleanly to percentages with 1 decimal place
                st.table(matrix_pct.style.format("{:.1%}"))

            else:
                missing = [col for col in required_cols if col not in df.columns]
                st.error(f"❌ Cannot plot chart. Missing columns from CSV: {missing}")

    except FileNotFoundError:
        st.error(f"❌ Could not find your data file at: {PATH + selected_file}")
        st.info("💡 Creating a temporary preview dataset for you instead:")


if __name__ == "__main__":
    main()
