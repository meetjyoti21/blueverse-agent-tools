from langchain_core.tools import tool
import pandas as pd

def get_simple_tool_with_parameter(config_pack: dict):
    @tool
    def read_esg_data(parameter_1: str = "", parameter_2: str = ""):
        """
        Reads ESG data from the GitHub-hosted CSV file.
        :param parameter_1: Filter by Asset Type (optional)
        :param parameter_2: Filter by Location (optional)
        """
        file_url = config_pack.get(
            "config_value_1",
            "https://github.com/Harsh-026/Sustainomaly/raw/refs/heads/main/esg_asset_data.csv"
        )
        try:
            df = pd.read_csv(file_url)
            if parameter_1:
                df = df[df["Asset Type"] == parameter_1]
            if parameter_2:
                df = df[df["Location"] == parameter_2]
            return df.to_dict(orient="records")
        except Exception as e:
            return {"error": str(e)}

    return read_esg_data
