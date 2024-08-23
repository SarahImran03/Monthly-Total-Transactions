import pandas as pd

def calculate(data_sheet):
    data_sheet['date'] = pd.to_datetime(data_sheet['date'], errors='coerce')
    data_sheet = data_sheet.dropna(subset=['date'])

    deduction_types = ['withdraw', 'stake']

    data_sheet.loc[:, 'amount for calculation'] = data_sheet.apply(
        lambda row: (-1 * row['amount']) if row['transaction_type'] in deduction_types
        else (0 if row['transaction_type'] == 'swap' else row['amount']), axis=1)

    data_sheet['month-year'] = data_sheet['date'].dt.to_period('M')
    monthly_total_amount = data_sheet.groupby('month-year')['amount for calculation'].sum()

    dictionary_result = monthly_total_amount.to_dict()
    return dictionary_result

def main():
    data_sheet = pd.read_csv('AI Research & Development Fellowship - Assessment Datasets - Question 1 - Coding.csv')
    result = calculate(data_sheet)
    print(result)

    return 0

if __name__ == "__main__":
    main()