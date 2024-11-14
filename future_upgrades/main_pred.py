# import dash
# from dash import dcc, html, Input, Output, State, callback_context
# import dash_bootstrap_components as dbc
# import pandas as pd
# import plotly.express as px
# from sqlalchemy import create_engine
# import joblib

# # Load data from the database
# engine = create_engine('mysql+pymysql://root:@localhost/esunscope')
# employees_df = pd.read_sql('SELECT * FROM Employees', engine)

# # Load each yearly work report and add a Year column
# work_report_year1_df = pd.read_sql('SELECT * FROM WorkReports_Year1', engine)
# work_report_year1_df['Year'] = 1
# work_report_year2_df = pd.read_sql('SELECT * FROM WorkReports_Year2', engine)
# work_report_year2_df['Year'] = 2
# work_report_year3_df = pd.read_sql('SELECT * FROM WorkReports_Year3', engine)
# work_report_year4_df = pd.read_sql('SELECT * FROM WorkReports_Year4', engine)
# work_report_year4_df['Year'] = 4

# # Concatenate all yearly work reports
# work_reports_df = pd.concat([work_report_year1_df, work_report_year2_df, work_report_year3_df, work_report_year4_df])

# # Merge with employee details
# merged_df = work_reports_df.merge(employees_df, on='EmployeeID', how='left')

# # Load the trained model
# model = joblib.load('employee_performance_model.pkl')  # Update with the actual model path

# # Initialize the Dash app with a Bootstrap theme
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

# # Chart options for user selection
# chart_options = {
#     "Line Chart (Performance Over Time)": "line_chart",
#     "Stacked Bar Chart (Projects by Department and Location)": "stacked_bar_chart",
#     "Heatmap (Hours Worked vs. Performance Score)": "heatmap",
#     "Bubble Chart (Feedback vs. Performance)": "bubble_chart",
#     "Sunburst Chart (Department-Position Breakdown)": "sunburst_chart",
#     "Histogram (Feedback Score Distribution)": "histogram",
#     "Box Plot (Performance by Position)": "box_plot",
#     "Radar Chart (Employee Progress)": "radar_chart"
# }

# # App layout
# app.layout = dbc.Container([
#     dbc.Row([
#         dbc.Col(html.H1("Employee Work Reports Dashboard", className="text-center text-primary my-4"), width=12)
#     ]),

#     # Filters row
#     dbc.Row([
#         dbc.Col([
#             html.Label("Select Year(s)", style={'font-weight': 'bold'}),
#             dcc.Dropdown(
#                 id='year-dropdown',
#                 options=[{'label': f'Year {i}', 'value': i} for i in range(1, 5)],
#                 value=[1],  # Default year
#                 clearable=False,
#                 multi=True,
#                 style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             )
#         ], width=6, lg=3, className="mb-3"),
        
#         dbc.Col([
#             html.Label("Select Location(s)", style={'font-weight': 'bold'}),
#             dcc.Dropdown(
#                 id='location-dropdown',
#                 options=[{'label': loc, 'value': loc} for loc in merged_df['Location'].unique()],
#                 value=['New York'],
#                 clearable=True,
#                 multi=True,
#                 style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             )
#         ], width=6, lg=3, className="mb-3"),

#         dbc.Col([
#             html.Label("Select Department(s)", style={'font-weight': 'bold'}),
#             dcc.Dropdown(
#                 id='department-dropdown',
#                 options=[{'label': dept, 'value': dept} for dept in merged_df['Department'].unique()],
#                 value=[],
#                 placeholder="Select Department(s)",
#                 clearable=True,
#                 multi=True,
#                 style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             )
#         ], width=6, lg=3, className="mb-3"),

#         dbc.Col([
#             html.Label("Select Position(s)", style={'font-weight': 'bold'}),
#             dcc.Dropdown(
#                 id='position-dropdown',
#                 options=[],  # Options will be populated based on selected department
#                 placeholder="Select Position(s)",
#                 clearable=True,
#                 multi=True,
#                 style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             )
#         ], width=6, lg=3, className="mb-3"),
#     ], justify="center", className="mb-4", style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'border-radius': '10px'}),

#     # Prediction input section
#     dbc.Row([
#         dbc.Col([
#             html.H3("Predict Employee Performance", className="text-center text-info mb-4")
#         ], width=12),
#         dbc.Col([
#             dcc.Dropdown(
#                 id='employee-id-dropdown',
#                 options=[{'label': emp_id, 'value': emp_id} for emp_id in employees_df['EmployeeID'].unique()],
#                 placeholder="Select Employee ID",
#                 style={'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             ),
#         ], width=4, className="mb-3"),
#         dbc.Col([
#             dcc.Input(
#                 id='hours-worked-input',
#                 type='number',
#                 placeholder="Hours Worked",
#                 style={'width': '100%', 'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             )
#         ], width=4, className="mb-3"),
#         dbc.Col([
#             dcc.Input(
#                 id='performance-score-input',
#                 type='number',
#                 placeholder="Performance Score",
#                 style={'width': '100%', 'border-radius': '5px', 'box-shadow': '0px 0px 4px #b0c4de'}
#             )
#         ], width=4, className="mb-3"),
#         dbc.Col([
#             html.Button("Predict", id='predict-button', n_clicks=0, className="btn btn-primary")
#         ], width=12, className="text-center"),
#         dbc.Col([
#             html.Div(id="prediction-output", className="text-center text-success mt-3")
#         ], width=12)
#     ], className="mb-4", style={'backgroundColor': '#f0f8ff', 'padding': '20px', 'border-radius': '10px'}),
    
#     # Add other chart components as needed
# ])

# # Prediction callback with error handling for missing columns
# @app.callback(
#     Output("prediction-output", "children"),
#     Input("predict-button", "n_clicks"),
#     State("employee-id-dropdown", "value"),
#     State("hours-worked-input", "value"),
#     State("performance-score-input", "value")
# )
# def predict_performance(n_clicks, employee_id, hours_worked, performance_score):
#     if n_clicks > 0 and employee_id and hours_worked is not None and performance_score is not None:
#         # Fetch employee-specific details with error handling for missing columns
#         employee_data = employees_df[employees_df['EmployeeID'] == employee_id].iloc[0]

#         # Check for 'FeedbackScore' or provide a default value
#         feedback_score = employee_data.get('FeedbackScore', 0)  # Use 0 or another default if FeedbackScore is missing

#         # Prepare input for prediction
#         input_data = {
#             'HoursWorked': hours_worked,
#             'PerformanceScore': performance_score,
#             'FeedbackScore': feedback_score,
#             'Department': employee_data['Department'],
#             'Position': employee_data['Position'],
#             'Year': 4,  # Assuming prediction is for the latest year
#             'Month': 'Sep'  # Assume September as a generic month
#         }

#         # Convert categorical features to dummies
#         input_df = pd.DataFrame([input_data])
#         input_df = pd.get_dummies(input_df, columns=['Department', 'Position', 'Month'])

#         # Ensure input_df columns match those the model was trained on
#         model_columns = model.feature_names_in_
#         for col in model_columns:
#             if col not in input_df.columns:
#                 input_df[col] = 0
#         input_df = input_df[model_columns]

#         # Make prediction
#         predicted_projects = model.predict(input_df)[0]
        
#         # Display prediction result
#         return f"Predicted Projects Completed: {predicted_projects:.2f}"
#     return "Please provide all inputs and click 'Predict'."


# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)
