# import dash
# from dash import dcc, html, Input, Output
# import dash_bootstrap_components as dbc
# import pandas as pd
# import plotly.express as px
# from sqlalchemy import create_engine

# # Load data from the database
# engine = create_engine('mysql+pymysql://root:@localhost/esunscope')
# employees_df = pd.read_sql('SELECT * FROM Employees', engine)

# # Load each yearly work report and add a Year column
# work_report_year1_df = pd.read_sql('SELECT * FROM WorkReports_Year1', engine)
# work_report_year1_df['Year'] = 1

# work_report_year2_df = pd.read_sql('SELECT * FROM WorkReports_Year2', engine)
# work_report_year2_df['Year'] = 2

# work_report_year3_df = pd.read_sql('SELECT * FROM WorkReports_Year3', engine)
# work_report_year3_df['Year'] = 3

# work_report_year4_df = pd.read_sql('SELECT * FROM WorkReports_Year4', engine)
# work_report_year4_df['Year'] = 4

# # Concatenate all yearly work reports
# work_reports_df = pd.concat([work_report_year1_df, work_report_year2_df, work_report_year3_df, work_report_year4_df])

# # Merge with employee details
# merged_df = work_reports_df.merge(employees_df, on='EmployeeID', how='left')

# # Initialize the Dash app with a Bootstrap theme
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO])

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
#                 multi=True,  # Allows selection of multiple locations
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
#     ], justify="center", className="mb-4", style={'backgroundColor': '#f8f9fa', 'padding': '20px', 'border-radius': '10px'}),

#     # Charts row
#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardHeader("Projects Completed by Department", className="bg-primary text-white"),
#                 dbc.CardBody(
#                     dcc.Graph(id='projects-completed-bar', config={'displayModeBar': False}),
#                     style={'padding': '10px'}
#                 )
#             ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
#         ], width=12, lg=6, className="mb-4"),
        
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardHeader("Department Distribution", className="bg-primary text-white"),
#                 dbc.CardBody(
#                     dcc.Graph(id='department-distribution-pie', config={'displayModeBar': False}),
#                     style={'padding': '10px'}
#                 )
#             ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
#         ], width=12, lg=6, className="mb-4")
#     ]),

#     # Employee details table
#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardHeader("Employee Details", className="bg-primary text-white"),
#                 dbc.CardBody(
#                     html.Div(id="employee-details")
#                 )
#             ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
#         ], width=12)
#     ], className="mb-4"),

#     # Position and Work Report Details
#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardHeader("Position and Work Report Details", className="bg-primary text-white"),
#                 dbc.CardBody(
#                     html.Div(id="position-details")
#                 )
#             ], style={'box-shadow': '0 4px 12px rgba(0, 0, 0, 0.1)', 'border-radius': '15px', 'margin': '10px'})
#         ], width=12)
#     ], className="mb-4")
# ], fluid=True)

# @app.callback(
#     [Output('projects-completed-bar', 'figure'),
#      Output('department-distribution-pie', 'figure'),
#      Output('employee-details', 'children'),
#      Output('position-details', 'children')],
#     [Input('year-dropdown', 'value'),
#      Input('location-dropdown', 'value'),
#      Input('department-dropdown', 'value')]
# )
# def update_charts(selected_year, selected_location, selected_department):
#     # Filter the data based on the selected year, location, and department
#     filtered_df = merged_df[merged_df['Year'].isin(selected_year)]

#     # Ensure selected_location is a list (even if only one location is selected)
#     if isinstance(selected_location, str):
#         selected_location = [selected_location]
    
#     # Apply location filter
#     if selected_location:
#         filtered_df = filtered_df[filtered_df['Location'].isin(selected_location)]

#     # Apply department filter
#     if selected_department:
#         filtered_df = filtered_df[filtered_df['Department'].isin(selected_department)]
    
#     # Check if there’s data to display; otherwise, show a blank figure
#     if filtered_df.empty:
#         return {}, {}, html.P("No employee data available for the selected filters.", className="text-center"), html.P("No position details available.")

#     # Bar chart for Projects Completed with Employee ID in hovertemplate
#     bar_fig = px.bar(filtered_df, x='Department', y='ProjectsCompleted', color='Department',
#                      title='Projects Completed for Selected Years and Departments', 
#                      hover_data={'EmployeeID': True, 'ProjectsCompleted': True, 'Department': True})
    
#     bar_fig.update_layout(
#         title={'x': 0.5, 'xanchor': 'center'},
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         font=dict(color="#333"),
#         yaxis=dict(showgrid=False)  # Disable y-axis grid lines
#     )
    
#     # Customize the hover information to include EmployeeID
#     bar_fig.update_traces(hovertemplate='Employee ID: %{customdata[0]}<br>Department: %{x}<br>Projects Completed: %{y}')

#     # Pie chart for Department Distribution
#     pie_fig = px.pie(filtered_df, names='Department', title='Department Distribution for Selected Filters')
#     pie_fig.update_layout(
#         title={'x': 0.5, 'xanchor': 'center'},
#         plot_bgcolor='rgba(0,0,0,0)',
#         paper_bgcolor='rgba(0,0,0,0)',
#         font=dict(color="#333")
#     )
#     pie_fig.update_traces(textinfo='percent+label', hovertemplate='%{label}: %{percent}')

#     # Employee details table
#     employee_table = dbc.Table.from_dataframe(
#         filtered_df[['EmployeeID', 'Name', 'Location', 'Department', 'ProjectsCompleted', 'HoursWorked', 'PerformanceScore', 'FeedbackScore']],
#         striped=True,
#         bordered=True,
#         hover=True,
#         responsive=True,
#         className="table-hover table-striped"
#     )

#     # Position and Work Report Details by Department and Position
#     position_details = []
#     grouped = filtered_df.groupby(['Department', 'Position'])
#     for (department, position), group in grouped:
#         position_details.append(html.H5(f"{department} - {position}"))
#         position_table = dbc.Table.from_dataframe(
#             group[['EmployeeID', 'Name', 'ProjectsCompleted', 'HoursWorked', 'PerformanceScore', 'FeedbackScore']],
#             striped=True,
#             bordered=True,
#             hover=True,
#             responsive=True,
#             className="table-hover table-striped"
#         )
#         position_details.append(position_table)
#         position_details.append(html.Hr())  # Divider between different positions

#     return bar_fig, pie_fig, employee_table, position_details

# # Run the Dash app
# if __name__ == '__main__':
#     app.run_server(debug=True)

